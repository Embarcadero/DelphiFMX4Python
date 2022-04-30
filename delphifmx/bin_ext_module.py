import sys, os, sys, platform
from os import environ
import importlib, importlib.machinery, importlib.util

class PyVerNotSupported(Exception):
  pass

def findmodule():
  is_conda = os.path.exists(os.path.join(sys.prefix, 'conda-meta'))
  pyver = f"{sys.version_info.major}.{sys.version_info.minor}"
  ossys = platform.system()
  platmac = platform.machine()  
  libdir = None
  libext = None

  if not (pyver in ["3.6", "3.7", "3.8", "3.9", "3.10"]):
    raise PyVerNotSupported(f"DelphiFMX doesn't support Python{pyver}.")

  if ossys == "Windows":
    if (sys.maxsize > 2**32):
      #Win x64	
      libdir = "Win64"
    else:
      #Win x86
      libdir = "Win32"

    libext = ".pyd"
  elif ossys == "Linux":
    #Check if the current platform is Android
    if "ANDROID_BOOTLOGO" in environ:       
      if (sys.maxsize > 2**32):
        #Android x64	
        libdir = "Android64" 
      else:
        #Android x32
        libdir = "Android" 
    else:
      if platmac == "x86_64":
        #Linux x86_64
        libdir = "Linux64"

    libext = ".so"
  elif ossys == "Darwin":
    if platmac == "x86_64":
      #macOS x86_64
      libdir = "OSX64"
    elif platmac == "arm64":
       #macOS arm64
      libdir = "OSXARM64"

    libext = ".dylib"
  if libdir:
    sdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), libdir) 
    # print(sdir)
    if not os.path.exists(sdir):
      raise ValueError("DelphiFMX module not found. Try to reinstall the delphifmx package or check for support compatibility.")        
    for fname in os.listdir(sdir):      
      if ('DelphiFMX' in fname) and (fname.endswith(libext)):
        return os.path.join(sdir, os.path.basename(fname))
    raise ValueError("DelphiFMX module not found. Try to reinstall the delphifmx package.") 
  else:
    raise ValueError("Unsupported platform.")  

def import_ext_module():  
    modulefullpath = findmodule()   
    loader = importlib.machinery.ExtensionFileLoader("DelphiFMX", modulefullpath)
    spec = importlib.util.spec_from_file_location("DelphiFMX", modulefullpath,
        loader=loader, submodule_search_locations=None)
    fmx_ext_module = loader.create_module(spec)
    # package = importlib.util.module_from_spec(spec)
    # sys.modules["delphifmx"] = package
    # spec.loader.exec_module(package)
    return fmx_ext_module
    
#Import the shared lib
fmx_ext_module = import_ext_module()
