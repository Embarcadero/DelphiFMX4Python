import setuptools, os, sys, platform, shutil

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
    sfilename = "DelphiFMX.dylib" 	
    if platmac == "x86_64":
      #Mac x86/64	
      platmacshort = "Darwin8664"
  
  pyversionstrshort = f"{sys.version_info.major}{sys.version_info.minor}"

  return f"DelphiFMX_{platmacshort}_{pyversionstrshort}{os.sep}{sfilename}"

#Copy target file from lib to pkg folder
def copylibfiletopkg(slibfile, spkgfile): 
  spkgdirname = os.path.dirname(spkgfile)
  if not os.path.exists(spkgdirname):
    os.makedirs(spkgdirname)
  shutil.copy(slibfile, spkgfile)
  
  #libdirname = os.path.dirname(slibfile)
  #shutil.rmtree(libdirname)
  
#Validate lib paths
def validatelibpaths(slibdir, slibfile):
  print(f"Check for lib dir: {slibdir}")    
  if not os.path.exists(f"{slibdir}"):
    raise ValueError(f"Invalid lib path: {slibdir}")
    
  print(f"Check for lib path: {slibfile}")
  if not os.path.exists(slibfile):
    raise ValueError(f"Invalid lib path: {slibfile}")
  
#Validate pkg paths
def validatepkgpaths(spkgfile):
  print(f"Check for pkg path: {spkgfile}")
  if not os.path.exists(spkgfile):
    raise ValueError(f"Invalid pkg path: {spkgfile}")
    
def isdistprocess():
  sdir = os.path.join(os.curdir, "delphifmx")
  for fname in os.listdir(sdir):
    if 'DelphiFMX' in fname:
      return True
  return False
  
def distprocess():
  sdir = os.path.join(os.curdir, "delphifmx")  
  for fname in os.listdir(sdir):
    if 'DelphiFMX' in fname:
      return os.path.basename(fname)
  return None    
    
def buildprocess():
  spath = buildfilepath()
  sfilename = os.path.basename(spath)
  
  slibdir = os.path.join(os.curdir, "lib")
  slibfile = os.path.join(slibdir, spath)

  spkgdir = os.path.join(os.curdir, "delphifmx")
  spkgfile = os.path.join(spkgdir, sfilename)
 
  validatelibpaths(slibdir, slibfile)
  copylibfiletopkg(slibfile, spkgfile)
  validatepkgpaths(spkgfile)     
  
  return sfilename
     
sfilename = None  
print("Check for process type") 
if isdistprocess():
  print("Found a distribution process")
  sfilename = distprocess()
else: 
  print("Found a build process")
  sfilename = buildprocess()
  
print("Working with file: ", sfilename)  
  
"""def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
            
list_files(f"{os.curdir}")"""  

def get_release_version():
    """Creates a new version incrementing by 1 the number of build specified in the
    DelphiFMX-0-01/__version__.py file."""
    lcals = locals()
    gbals = globals()
    with open(os.path.join(os.getcwd(), "delphifmx", "__version__.py"), "rt") as opf:
        opffilecontents = opf.read()
        retvalue = exec(opffilecontents, gbals, lcals)
    versorigstr = lcals["__version__"]
    return versorigstr
    
versnewstr = get_release_version()         

setuptools.setup(
  name="delphifmx",
  version=versnewstr,
  description="Delphi FMX for Python",
  packages=["delphifmx"],
  package_data={"delphifmx": [sfilename]},
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
)
