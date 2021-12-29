import json

def get_prop(prop_name):
    with open('moduledefs.json', 'r+') as openfile:    
        moduledefs = json.load(openfile)
        return moduledefs[prop_name]

def set_prop(prop_name, value):
    with open('moduledefs.json', 'w+') as openfile:    
        moduledefs = json.load(openfile)
        moduledefs[prop_name] = value
        openfile.write(json.dump(moduledefs))

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