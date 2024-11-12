import sys
import os
import platform
import importlib
import importlib.machinery
import importlib.util


def find_extension_module():
    py_ver = f"{sys.version_info.major}.{sys.version_info.minor}"
    plat_sys = platform.system()
    plat_mac = platform.machine()
    lib_dir = None
    lib_ext = None

    if not (py_ver in ["3.8", "3.9", "3.10", "3.11", "3.12", "3.13"]):
        raise ValueError(f"DelphiFMX doesn't support Python{py_ver}.")

    if plat_sys == "Windows":
        if (sys.maxsize > 2**32):
            # Win x64
            lib_dir = "Win64"
        else:
            # Win x86
            lib_dir = "Win32"

        lib_ext = ".pyd"
    elif plat_sys == "Linux":
        # Check if the current platform is Android
        if "ANDROID_BOOTLOGO" in os.environ:
            if (sys.maxsize > 2**32):
                # Android x64
                lib_dir = "Android64"
            else:
                # Android x32
                lib_dir = "Android"
        else:
            if plat_mac == "x86_64":
                # Linux x86_64
                lib_dir = "Linux64"

        lib_ext = ".so"
    elif plat_sys == "Darwin":
        if plat_mac == "x86_64":
            # macOS x86_64
            lib_dir = "OSX64"
        elif plat_mac == "arm64":
           # macOS arm64
            lib_dir = "OSXARM64"

        lib_ext = ".dylib"

    if not lib_dir:
        raise ValueError("Unsupported platform.")

    lib_dir = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), lib_dir)
    if not os.path.exists(lib_dir):
        raise ValueError(
            "DelphiFMX module not found. \
            Try to reinstall the delphifmx package or check for support compatibility.")

    for fname in os.listdir(lib_dir):
        if ('DelphiFMX' in fname) and (fname.endswith(lib_ext)):
            return os.path.join(lib_dir, os.path.basename(fname))

    raise ValueError(
        "DelphiFMX module not found. Try to reinstall the delphifmx package.")


def init_plat():
    if (platform.system() == "Darwin") and (platform.machine() == "arm64"):
        try:
            from . import darwin_arm
        except Exception as e:
            print("Darwin util has failed with message \'%s\'." % (str(e),))


def new_import():
    init_plat()
    lib_path = find_extension_module()
    loader = importlib.machinery.ExtensionFileLoader(
        "DelphiFMX", lib_path)
    spec = importlib.util.spec_from_file_location("DelphiFMX",
                                                  lib_path,
                                                  loader=loader,
                                                  submodule_search_locations=None)
    loader.create_module(spec)
    package = importlib.util.module_from_spec(spec)
    sys.modules["delphifmx"] = package
    spec.loader.exec_module(package)
    return package


# Import the shared lib
package = new_import()
