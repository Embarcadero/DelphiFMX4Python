import sys, platform, os, sys, io
import importlib, importlib.machinery, importlib.util

def init_module_defs():
    pyversionstrshort = f"{sys.version_info.major}.{sys.version_info.minor}"
    dirbname_full = os.path.dirname(os.path.abspath(__file__))
    with io.open(os.path.join(dirbname_full, "moduledefs.json"), "w+") as moduledefs:
        moduledefs.write(r'{"python_ver":  "@ver"}'.replace('@ver', pyversionstrshort))

def findmodule(dirbname):
  sdir = os.path.join(os.curdir, dirbname) 
  for fname in os.listdir(sdir):
    if 'DelphiFMX' in fname:
      return os.path.basename(fname)
  return None 

def new_import():  
    dirbname_full = os.path.dirname(os.path.abspath(__file__)) 
    modulefullpath = os.path.join(dirbname_full, findmodule(dirbname_full))   
    loader = importlib.machinery.ExtensionFileLoader("DelphiFMX", modulefullpath)
    spec = importlib.util.spec_from_file_location("DelphiFMX", modulefullpath,
        loader=loader, submodule_search_locations=None)
    ld = loader.create_module(spec)
    package = importlib.util.module_from_spec(spec)
    sys.modules["delphifmx"] = package
    spec.loader.exec_module(package)
    return package

init_module_defs()
package = new_import()