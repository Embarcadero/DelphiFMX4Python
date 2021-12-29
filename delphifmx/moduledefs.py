import sys, os, platform, json

def get_defs_path():    
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "moduledefs.json")

def has_defs():
    return os.path.exists(get_defs_path())

def get_prop(prop_name):
    if not os.path.exists(get_defs_path()):
        return ''

    with open(get_defs_path(), 'r+') as openfile:   
        try: 
            moduledefs = json.load(openfile)
            if not (prop_name in moduledefs):
                return ''
            else:
                return moduledefs[prop_name]
        except json.decoder.JSONDecodeError: #empty file
            return ''         

def set_prop(prop_name, value):
    if os.path.exists(get_defs_path()):
        with open(get_defs_path(), 'r+') as openfile:    
            try:
                moduledefs = json.load(openfile)
            except json.decoder.JSONDecodeError:
                moduledefs = {}
    else:
        moduledefs = {}

    moduledefs[prop_name] = value
    with open(get_defs_path(), 'w+') as openfile:              
        openfile.write(json.dumps(moduledefs))

def set_python_home(python_home):    
    set_prop('python_home', python_home)

def get_python_home():
    return get_prop('python_home')

def set_python_bin(python_bin):    
    set_prop('python_bin', python_bin)

def get_python_bin():
    return get_prop('python_bin')

def set_python_lib(python_lib):    
    set_prop('python_lib', python_lib)

def get_python_lib():
    return get_prop('python_lib')    

def set_python_shared_lib(python_shared_lib):    
    set_prop('python_shared_lib', python_shared_lib)

def get_python_shared_lib():
    return get_prop('python_shared_lib') 

def set_python_ver(python_ver):
    set_prop('python_ver', python_ver)

def get_python_ver():
    return get_prop('python_ver')

def try_load_defs(force):
    #def is_conda():
    #    return os.path.exists(os.path.join(sys.prefix, 'conda-meta'))

    def find_python_home():
        return sys.prefix

    def find_python_bin():
        ossys = platform.system()
        if (ossys == 'Windows'):
            return sys.prefix
        else:
            return os.path.dirname(sys.executable)            

    def find_python_lib():
        ossys = platform.system()
        if (ossys == 'Windows'):
            return sys.prefix
        else:
            libpath = os.path.join(os.path.dirname(os.path.dirname(sys.executable)), 'lib')
            return (libpath if os.path.exists(libpath) else '')

    def find_python_shared_lib():
        pylibdir = get_python_lib()
        if (pylibdir == ''):
            return ''

        ossys = platform.system()
        prefix = ''
        ext = ''        
        if (ossys == 'Windows'):
            ext = '.dll'
        elif ossys == "Linux":
            prefix = 'lib'
            ext = '.so'
        elif ossys == "Darwin":
            prefix = 'lib'
            ext = '.dylib'

        pyver = get_python_ver()
        pysharedlib = f"{prefix}python{pyver}{ext}"        
        if os.path.exists(os.path.join(pylibdir, pysharedlib)):
            return pysharedlib
        
        pysharedlib = f"{prefix}python{pyver}m{ext}"    
        if os.path.exists(os.path.join(pylibdir, pysharedlib) ):
            return pysharedlib

        return ''

    def find_python_ver():
        return f"{sys.version_info.major}.{sys.version_info.minor}"

    if (get_python_home() == '') or (force):
        set_python_home(find_python_home())

    if (get_python_bin() == '') or (force):
        set_python_bin(find_python_bin())

    if (get_python_lib() == '') or (force):
        set_python_lib(find_python_lib())    

    if (get_python_ver() == '') or (force):
        set_python_ver(find_python_ver())

    if (get_python_shared_lib() == '') or (force):
        set_python_shared_lib(find_python_shared_lib())

_auto_load_defs = True
def get_auto_load_defs():
    return _auto_load_defs

def set_auto_load_defs(auto_load_defs): 
    global _auto_load_defs           
    _auto_load_defs = auto_load_defs