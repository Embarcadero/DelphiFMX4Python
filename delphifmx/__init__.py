import imp, sys, platform, os, sys
import importlib, importlib.util

dirbname_full = os.path.dirname(__file__)

#print("difull", dirbname_full, "name", __name__)
    
def findmodule():
  sdir = os.path.join(os.curdir, dirbname_full) 
  for fname in os.listdir(sdir):
    if 'DelphiFMX' in fname:
      return os.path.basename(fname)
  return None 
          
def new_import(dirbname):
    modulefullpath = os.path.join(dirbname, findmodule())
    loader = importlib.machinery.ExtensionFileLoader("DelphiFMX", modulefullpath)
    spec = importlib.util.spec_from_file_location("DelphiFMX", modulefullpath,
        loader=loader, submodule_search_locations=None)
    #print("spec", spec, spec.loader, modulefullpath, __file__)
    ld = loader.create_module(spec)
    #print("ld", ld)
    package = importlib.util.module_from_spec(spec)
    sys.modules["delphifmx"] = package
    #print("cmodelq", delphifmx)
    spec.loader.exec_module(package)
    #print("cmodli", delphifmx)
    return package

package = new_import(dirbname_full)
