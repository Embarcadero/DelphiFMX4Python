import setuptools, os, sys, platform, shutil

pkgname = "delphifmx"

#Force platform wheel
try:
  from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
  class bdist_wheel(_bdist_wheel):
    def finalize_options(self):
      _bdist_wheel.finalize_options(self)
      self.root_is_pure = False
except ImportError:
  bdist_wheel = None 
 
#Find sys/machine file
def buildfilepath():
  ossys = platform.system()
  platmac = platform.machine()
  platmacshort = ""
  sfilename = ""
  if ossys == "Windows":
    sfilename = "DelphiFMX.pyd"
    if platmac.endswith('64'):
      #Win x64	
      platmacshort = "Win64"
    else:
      #Win x86
      platmacshort = "Win32"
  elif ossys == "Linux":
    sfilename = "libDelphiFMX.so"
    if platmac == "arm":
      #Linux/Android arm	
      platmacshort = "LinuxArm"
    elif platmac.startswith("arm") or platmac.startswith("aarch"):
      #Linux/Android aarch64
      platmacshort = "LinuxAarch64"
    elif platmac == "x86_64":
      #Linux x86/64
      platmacshort = "Linux8664"    
  elif ossys == "Darwin":
    sfilename = "libDelphiFMX.dylib" 	
    if platmac == "x86_64":
      #Mac x86/64	
      platmacshort = "Darwin8664"
  
  if not platmacshort:
    raise ValueError("Undetermined platform.")
  
  pyversionstrshort = f"{sys.version_info.major}{sys.version_info.minor}"

  return f"DelphiFMX_{platmacshort}_{pyversionstrshort}{os.sep}{sfilename}"

#Copy target file from lib to pkg folder
def copylibfiletopkg(slibfile, spkgfile): 
  spkgdirname = os.path.dirname(spkgfile)
  if not os.path.exists(spkgdirname):
    os.makedirs(spkgdirname)
  shutil.copy(slibfile, spkgfile)

#Validate lib paths
def validatelibpaths(slibdir, slibfile):
  print(f"Check for lib dir: {slibdir}")    
  if not os.path.exists(f"{slibdir}"):
    raise ValueError(f"Invalid lib path: {slibdir}")
    
  print(f"Check for lib path: {slibfile}")
  if not os.path.exists(slibfile):
    raise ValueError(f"File not found: {slibfile}")
  
#Validate pkg paths
def validatepkgpaths(spkgfile):
  print(f"Check for pkg path: {spkgfile}")
  if not os.path.exists(spkgfile):
    raise ValueError(f"File not found {spkgfile}")
    
#Clear pkg files (trash)
def clearpkgtrashfiles():
  sdir = os.path.join(os.curdir, pkgname)
  files = os.listdir(sdir)
  filtered_files = [file for file in files if file.endswith(".so") or file.endswith(".pyd")]
  for file in filtered_files:
    fpath = os.path.join(sdir, file)
    print("Removing trash file:", fpath)
    os.remove(fpath)
    
def finddistfile():
  sdir = os.path.join(os.curdir, pkgname)  
  for fname in os.listdir(sdir):
    if 'DelphiFMX' in fname:
      return os.path.basename(fname)
  return None  
    
def copylibfile():
  spath = buildfilepath()
  sfilename = os.path.basename(spath)

  slibdir = os.path.join(os.curdir, "lib")
  slibfile = os.path.join(slibdir, spath)
  
  spkgdir = os.path.join(os.curdir, pkgname)
  spkgfile = os.path.join(spkgdir, sfilename)
 
  clearpkgtrashfiles()	  
  validatelibpaths(slibdir, slibfile)
  copylibfiletopkg(slibfile, spkgfile)
  validatepkgpaths(spkgfile)     
  
  return sfilename 
  
def get_release_version():
    lcals = locals()
    gbals = globals()
    with open(os.path.join(os.getcwd(), pkgname, "__version__.py"), "rt") as opf:
        opffilecontents = opf.read()
        retvalue = exec(opffilecontents, gbals, lcals)
    versorigstr = lcals["__version__"]
    return versorigstr     
  
extra_args = {}
#We don't want to share the compiled files via sdist (we don't have them)
if not ("sdist" in sys.argv):  
  slibdir = os.path.join(os.curdir, "lib")
  #Binary distribution
  if ("bdist_wheel" in sys.argv) and os.path.exists(slibdir):
    bdata = copylibfile()
    extra_args = {'package_data': {pkgname: [bdata]}}
  else:
    #Final user installation
    bdata = finddistfile()
    if bdata:
      extra_args = {'package_data': {pkgname: [bdata]}}      
    
versnewstr = get_release_version()   

with open("README.md", "r") as fh:
  long_description = fh.read()     

setuptools.setup(
  name=pkgname,
  version=versnewstr,
  description="Delphi FMX for Python",
  author="Lucas Belo, Jim McKeeth",
  author_email="lucas.belo@live.com",
  long_description=long_description,
  long_description_content_type="text/markdown",
  packages=["delphifmx"],
  classifiers=[
            'Development Status :: 1 - Planning',
            'Intended Audience :: Developers',
            'Topic :: Software Development',
            'License :: OSI Approved :: BSD License',
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
