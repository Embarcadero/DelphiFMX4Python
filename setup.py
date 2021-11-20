import setuptools, os, sys, platform, shutil
import logging
logger = logging.getLogger(__name__)
# Force platform wheel
try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False
    print("created 'bdist_wheel' class")

except ImportError:
    bdist_wheel = None
    print("Unable to create 'bdist_wheel' class")

# Find sys/machine file
def buildfilepath():
    command_options = command_line_options()
    ossys = platform.system()
    platmac = platform.machine()
    plat_name = command_options.get("plat-name", f"{ossys}_{platmac}")
    print(f"platforms {ossys};{platmac}-{plat_name}")
    platmacshort = ""
    sfilename = ""
    plat_name_lower = plat_name.lower()
    if plat_name_lower.startswith("win"):
        sfilename = "DelphiFMX.pyd"
        if plat_name.endswith('64'):
            # Win x64
            platmacshort = "Win64"
        else:
            # Win x86
            platmacshort = "Win32"
    elif plat_name_lower.startswith("linux") or plat_name.startswith("manylinux"):
        plat_name_parts = plat_name.split("_", 1)
        sfilename = "libDelphiFMX.so"
        if plat_name_parts[1] == "arm":
            # Linux/Android arm
            platmacshort = "LinuxArm"
        elif plat_name_parts[1].startswith("arm") or platmac.startswith("aarch"):
            # Linux/Android aarch64
            platmacshort = "LinuxAarch64"
        elif plat_name_parts[1] == "x86_64":
            # Linux x86/64
            platmacshort = "Linux8664"
    elif plat_name.startswith("macosx") or plat_name.startswith("Darwin"):
        sfilename = "libDelphiFMX.dylib"
        if plat_name.endswith("x86_64"):
            # Mac x86/64
            platmacshort = "Darwin8664"
  
    if not platmacshort:
        raise ValueError(f"Undetermined platform: {plat_name}.")
  
    pyversionstrshort = f"{sys.version_info.major}{sys.version_info.minor}"

    return f"DelphiFMX_{platmacshort}_{pyversionstrshort}{os.sep}{sfilename}"


# Copy target file from lib to pkg folder
def copylibfiletopkg(slibfile, spkgfile): 
    spkgdirname = os.path.dirname(spkgfile)
    if not os.path.exists(spkgdirname):
        os.makedirs(spkgdirname)
    shutil.copy(slibfile, spkgfile)


# Gets the platform we are BUILDING FOR
def command_line_options():
    #Only extracts the words after a --option
    dct = {}
    sargvp1 = sys.argv[1:]
    for (ielement, element) in enumerate(sargvp1):
        if element.startswith("--") and ielement < (len(sargvp1) - 1):
            element_cut = element[2:]
            dct[element_cut] = sargvp1[ielement + 1]
    return dct

# Validate lib paths
def validatelibpaths(slibdir, slibfile):
    print(f"Check for lib dir: {slibdir}")
    if not os.path.exists(f"{slibdir}"):
        raise ValueError(f"Invalid lib path: {slibdir}")
    
    print(f"Check for lib path: {slibfile}")
    if not os.path.exists(slibfile):
        raise ValueError(f"File not found: {slibfile}")


# Validate pkg paths
def validatepkgpaths(spkgfile):
    print(f"Check for pkg path: {spkgfile}")
    if not os.path.exists(spkgfile):
        raise ValueError(f"File not found {spkgfile}")


# Clear pkg files (trash)
def clearpkgtrashfiles():
    sdir = os.path.join(os.curdir, "delphifmx")
    files = os.listdir(sdir)
    filtered_files = [file for file in files if file.endswith(".so") or file.endswith(".pyd")]
    for file in filtered_files:
        fpath = os.path.join(sdir, file)
        print("Removing trash file:", fpath)
        os.remove(fpath)


def finddistfile():
    sdir = os.path.join(os.curdir, "delphifmx")
    for fname in os.listdir(sdir):
        if 'DelphiFMX' in fname:
            return os.path.basename(fname)
    return None


def copylibfile():
    spath = buildfilepath()
    sfilename = os.path.basename(spath)

    slibdir = os.path.join(os.curdir, "lib")
    slibfile = os.path.join(slibdir, spath)

    spkgdir = os.path.join(os.curdir, "delphifmx")
    spkgfile = os.path.join(spkgdir, sfilename)
 
    clearpkgtrashfiles()
    validatelibpaths(slibdir, slibfile)
    copylibfiletopkg(slibfile, spkgfile)
    validatepkgpaths(spkgfile)

    return sfilename


def get_release_version():
    """Gets the version from the delphifmx/__version__.py file, or from the FORCE_VERSION
    environment variable (this planned for develpoment only)."""
    if "FORCE_VERSION" in os.environ:
        return os.environ["FORCE_VERSION"]
    lcals = locals()
    gbals = globals()
    with open(os.path.join(os.getcwd(), "delphifmx", "__version__.py"), "rt") as opf:
        opffilecontents = opf.read()
        retvalue = exec(opffilecontents, gbals, lcals)
    version_orig_str = lcals["__version__"]
    return version_orig_str

extra_args = {}
# We don't want to share the compiled files via sdist (we don't have them)
if not ("sdist" in sys.argv):  
  slibdir = os.path.join(os.curdir, "lib")
  # Binary distribution
  if ("bdist_wheel" in sys.argv) and os.path.exists(slibdir):
    bdata = copylibfile()
    extra_args = {'package_data': {"delphifmx": [bdata]}}
  else:
    #Final user installation
    bdata = finddistfile()
    if bdata:
      extra_args = {'package_data': {"delphifmx": [bdata]}}
    
versnewstr = get_release_version()   

with open("README.md", "r") as fh:
  long_description = fh.read()     

package_name = os.environ.get("PACKAGE_NAME", "delphifmx")

setuptools.setup(
    name=package_name,
    version=versnewstr,
    description="Delphi FMX for Python",
    author="Lucas Belo, Lucio Montero, Jim McKeeth",
    author_email="lucas.belo@live.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Other/Proprietary License",
    license_files=["LICENSE.md"],
    url = "https://github.com/Embarcadero/DelphiFMX4Python",
    packages=["delphifmx"],
    classifiers=[
            'Development Status :: 1 - Planning',
            'Intended Audience :: Developers',
            'Topic :: Software Development',
            'License :: Other/Proprietary License',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3 :: Only',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Operating System :: Unix',
            'Operating System :: MacOS',
            'Operating System :: Android',                        
        ],		
    cmdclass={'bdist_wheel': bdist_wheel},
    **extra_args
)
