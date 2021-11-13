import importlib, os, sys, platform
import importlib.machinery, importlib.util
import logging
logger = logging.getLogger(__name__)


def new_import(internal_name="DelphiFMX", module_full_path=None,
               pyd_file_basename="DelphiFMX.pyd", external_name="delphifmx"):
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


def find_module(internal_name="DelphiFMX"):
    platmac = platform.machine()
    if platmac.endswith('64'):
      # Win x64
      platmacshort = "Win64"
    else:
      # Win x86
      platmacshort = "Win32"

    dir_last_level = f"{internal_name}_{platmacshort}_{sys.version_info.major}{sys.version_info.minor}"
    my_folder = os.path.dirname(os.path.abspath(os.path.join(os.getcwd(), __file__)))
    dirbname_full = os.path.normpath(os.path.join(my_folder, "..", "lib", dir_last_level))
    internal_name_lower = internal_name.lower()

    for fname in os.listdir(dirbname_full):
        #Do a case-insensitive search for the .pyd file
        if internal_name_lower in fname.lower():
            return os.path.join(dirbname_full, fname)
    return None
