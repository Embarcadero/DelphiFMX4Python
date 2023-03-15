# THIS SCRIPT ONLY WORKS ON DARWIN

# We are using this script to initialize GUI before loading the DelphiFMX library.
# This approach prevents the dead-lock that happens when we start GUI with the dynamic-linker initializer.

try:
	import ctypes
except ImportError:
	raise NotImplementedError("DelphiFMX requires ctypes, which doesn't seem to be available.")

from ctypes import cdll, c_void_p, c_char_p

framework_name = '/System/Library/Frameworks/AppKit.framework/AppKit'
class_name = 'NSScreen'
method_name = 'mainScreen'

try:
    c = cdll.LoadLibrary(framework_name)
except OSError:
	raise ValueError('No framework named \'%s\' found.' %(framework_name,))

objc_getClass = c.objc_getClass
objc_getClass.argtypes = [c_char_p]
objc_getClass.restype = c_void_p

class_getClassMethod = c.class_getClassMethod
class_getClassMethod.restype = c_void_p
class_getClassMethod.argtypes = [c_void_p, c_void_p]

sel_registerName = c.sel_registerName
sel_registerName.restype = c_void_p
sel_registerName.argtypes = [c_char_p]

ptr = objc_getClass(class_name.encode('ascii'))
if ptr is None:
	raise ValueError('No Objective-C class named \'%s\' found.' % (class_name,))

method = class_getClassMethod(ptr, sel_registerName(method_name.encode('ascii')))
if not method:
    raise AttributeError('No class method found for selector "%s".' % (sel_registerName(method_name.encode('ascii'))))

objc_msgSend = c['objc_msgSend']
objc_msgSend.argtypes = [c_void_p, c_void_p]
objc_msgSend.restype = c_void_p
objc_msgSend(ptr, sel_registerName(method_name.encode('ascii')), None)