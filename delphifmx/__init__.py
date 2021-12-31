import sys, os, sys, platform
from os import environ
import importlib, importlib.machinery, importlib.util
from delphifmx import moduledefs

def findmodule():
  ossys = platform.system()
  platmac = platform.machine()  
  libdir = None
  if ossys == "Windows":
    if (sys.maxsize > 2**32):
      #Win x64	
      libdir = "Win64"
    else:
      #Win x86
      libdir = "Win32"
  elif ossys == "Linux":
    #Check if the current platform is Android
    if "ANDROID_ARGUMENT" in environ:       
      if (sys.maxsize > 2**32):
        #Android x64	
        libdir = "Android64" 
      else:
        #Android x32
        libdir = "Android" 
    else:
      if platmac == "x86_64":
        #Linux x86/64
        libdir = "Linux64"    
  elif ossys == "Darwin":
    if platmac == "x86_64":
      #Mac x86/64	
      libdir = "OSX64"  
  if libdir:
    sdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), libdir) 
    if not os.path.exists(sdir):
      raise ValueError("DelphiFMX module not found. Try to reinstall the delphifmx package or check for support compatibility.")        
    for fname in os.listdir(sdir):      
      if 'DelphiFMX' in fname:        
        return os.path.join(sdir, os.path.basename(fname))
    raise ValueError("DelphiFMX module not found. Try to reinstall the delphifmx package.") 
  else:
    raise ValueError("Unsupported platform.")  

def new_import():  
    modulefullpath = findmodule()   
    loader = importlib.machinery.ExtensionFileLoader("DelphiFMX", modulefullpath)
    spec = importlib.util.spec_from_file_location("DelphiFMX", modulefullpath,
        loader=loader, submodule_search_locations=None)
    ld = loader.create_module(spec)
    package = importlib.util.module_from_spec(spec)
    sys.modules["delphifmx"] = package
    spec.loader.exec_module(package)
    return package
    
#Setup moduledefs.json
if moduledefs.get_auto_load_defs():
  moduledefs.try_load_defs(False)
#Import the shared lib
package = new_import()