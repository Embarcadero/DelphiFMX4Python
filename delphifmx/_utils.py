import importlib, os, sys, platform
import importlib.machinery, importlib.util
import logging
logger = logging.getLogger(__name__)


def new_import(internal_name="DelphiFMX", module_full_path=None,
               pyd_file_basename=None, external_name="delphifmx"):
    platmac = platform.machine()
    platsys = platform.system()
    if platsys == "Windows":
        pyd_file_basename = "DelphiFMX.pyd"
    elif platsys == "Linux":
        pyd_file_basename = "libDelphiFMX.so"
    elif platsys == "Darwin":
        pyd_file_basename = "libDelphiFMX.dylib"

    if module_full_path is None:
        dirbname_full = os.path.dirname(os.path.abspath(__file__))
        module_full_path = os.path.join(dirbname_full, pyd_file_basename)
    loader = importlib.machinery.ExtensionFileLoader(internal_name, module_full_path)
    spec = importlib.util.spec_from_file_location(internal_name, module_full_path,
        loader=loader, submodule_search_locations=None)
    try:
        package = importlib.util.module_from_spec(spec)
    except Exception:
        raise Exception(f"Error when loading the extension file: {module_full_path}")
    sys.modules[external_name] = package
    spec.loader.exec_module(package)
    return package
