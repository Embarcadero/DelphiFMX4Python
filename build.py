import sys
import os
import sys
import shutil
import time
import platform
import distutils.dir_util
from wheel.bdist_wheel import bdist_wheel


'''
BDistWheel forces python and abi wheel tags for binary distributions
'''


class BDistWheel(bdist_wheel):

    def finalize_options(self):
        bdist_wheel.finalize_options(self)
        self.root_is_pure = ("--universal" in sys.argv)


'''
Sort out the platform library for binary distribution and add to the package directory.
Place all libraries onto the package directory for source distribution.
Place the XML doc file onto the package directory.
'''


class PackageDataBuilder():

    def __init__(self):
        self.pkg_dir = os.path.join(os.curdir, "delphifmx")
        self.plat_name = None
        for arg in sys.argv:
            if arg.startswith("--plat-name=") and (len(arg.split("=")) == 2):
                self.plat_name = arg.split("=")[1]

    '''
    Must run "python setup.py clean --all" between builds.
    '''

    def clean_up(self):
        lib_dirs = [os.path.join(self.pkg_dir, "Win32"),
                    os.path.join(self.pkg_dir, "Win64"),
                    os.path.join(self.pkg_dir, "Linux64"),
                    os.path.join(self.pkg_dir, "OSX64"),
                    os.path.join(self.pkg_dir, "OSXARM64")]

        for lib_dir in lib_dirs:
            if os.path.isdir(lib_dir):
                shutil.rmtree(lib_dir)

        # Wait until the OS remove all dirs
        for lib_dir in lib_dirs:
            for attempts in range(3):
                if not os.path.isdir(lib_dir):
                    break
                else:
                    time.sleep(1)

    '''
    Cross-compiling wheel. 
    This generates a wheel following the cross platform set on --plat-name.
    See: https://docs.python.org/3/distutils/builtdist.html#cross-compiling-on-windows
    '''

    def __check_cross_compiling(self):
        is_cross_compiling = False
        lib_dir = None

        if self.plat_name:
            is_cross_compiling = True
            if self.plat_name == "win32":
                lib_dir = "Win32"
            elif self.plat_name == "win_amd64":
                lib_dir = "Win64"
            elif self.plat_name == "manylinux1_x86_64":
                lib_dir = "Linux64"
            # macosx_10_9_x86_64
            elif self.plat_name.startswith("macosx") and self.plat_name.endswith("x86_64"):
                lib_dir = "OSX64"
            # macosx_11_0_arm64
            elif self.plat_name.startswith("macosx") and self.plat_name.endswith("arm64"):
                lib_dir = "OSXARM64"
            else:
                is_cross_compiling = False

        return (is_cross_compiling, lib_dir)

    '''
    Copy the FMX extension module(s) to the package data folder.
    Source distributions and Universal binary distributions will deliver 
    all library versions. The right one will be loaded by __init__.py.
    Platform distributions will deliver only the library that matches the runner.
    '''

    def __pick_and_copy_libraries(self):
        if ("sdist" in sys.argv) or (("bdist_wheel" in sys.argv) and ("--universal" in sys.argv)):
            # sdist/bdist[--universal] deploy all extension modules
            distutils.dir_util.copy_tree("lib", self.pkg_dir)
        else:
            # Deploys the current platform extension module only
            is_cross_compiling, lib_dir = self.__check_cross_compiling()
            if not is_cross_compiling:
                plat_sys = platform.system()
                plat_mac = platform.machine()
                if plat_sys == "Windows":
                    if (sys.maxsize > 2**32):
                        # Win x64
                        lib_dir = "Win64"
                    else:
                        # Win x86
                        lib_dir = "Win32"
                elif plat_sys == "Linux":
                    if plat_mac == "x86_64":
                        # Linux x86_64
                        lib_dir = "Linux64"
                elif plat_sys == "Darwin":
                    if plat_mac == "x86_64":
                        # macOS x86_64
                        lib_dir = "OSX64"
                    elif plat_mac == "arm64":
                        # macOS arm64
                        lib_dir = "OSXARM64"

            if lib_dir:
                distutils.dir_util.copy_tree(os.path.join(
                    "lib", lib_dir), os.path.join(self.pkg_dir, lib_dir))
            else:
                raise ValueError("Unsupported platform.")

    '''
    Copy the XML doc file to the package data folder.
    The docs.xml file is the result of the compilation of all xml doc files.
    '''

    def __pick_and_copy_docs(self):
        # Copy the doc files to the package folder into the doc subfolder
        docs_file = os.path.join("docs", "xml", "docs.xml")
        if os.path.exists(docs_file):
            pkg_doc_dir = os.path.join(self.pkg_dir, "doc")
            if not os.path.exists(pkg_doc_dir):
                os.mkdir(pkg_doc_dir)
            distutils.file_util.copy_file(
                docs_file, os.path.join(pkg_doc_dir, "docs.xml"))

    def build_package_data(self):
        self.__pick_and_copy_libraries()
        self.__pick_and_copy_docs()


def setup():
    builder = PackageDataBuilder()
    builder.clean_up()
    builder.build_package_data()
