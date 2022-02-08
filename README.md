# DelphiFMX for Python <a href="https://github.com/Embarcadero/DelphiFMX4Python/"><img align="right" alt="DelphiFMX for Python" src="images/DelphiFMX4Python(256px).png"></a> 
Delphi's FireMonkey framework as a Python module for Windows, MacOS, Linux, and Android GUI development.

FireMonkey is a GUI framework originally from [Embarcadero Delphi](https://www.embarcadero.com/products/delphi) for native cross-platform application development. It uses the GPU via DirectX or OpenGL for hardware accellerated rendering. It includes a rich styling system and is user extensible. 

<b>About:</b>

The `delphifmx` is a natively compiled Python module powered by the [Python4Delphi library](https://github.com/pyscripter/python4delphi). It gives Python developers access to the FireMonkey GUI framework from Python with no need to use Delphi in their development process, and is [freely redistributable](https://github.com/Embarcadero/DelphiFMX4Python/blob/main/LICENSE.md). 

<b>Python installation requirements on Linux:</b>

It uses the Python interpreter, requiring Python to be compiled with the "--enable-shared" flag.
<br>Make sure you've set the "LD_LIBRARY_PATH" and "PATH" environment variables and that Python loads the same libpython.so used by delphifmx.
* Check out the [scripts directory](https://github.com/Embarcadero/DelphiFMX4Python/tree/main/scripts) for further instructions in how to install Python or for an automated installation process. 

<b>Installation:</b>

    pip install delphifmx
   
<b>Supports:</b>
* Win32 x86, Win64 x86, Linux64 x86, Android64, macOS64 and macM1 architectures
* Python cp3.6, cp3.7, cp3.8, cp3.9 and cp3.10 (excluding cp3.6 on Linux and macOS)

<b>Conda support:</b>
* Win x86 and x64 from Python cp3.6 to cp3.10 
* Linux x86_64 from Python cp3.7 to cp3.10
* macOS not supported yet

Also check out [DelphiVCL4Python](https://github.com/Embarcadero/DelphiVCL4Python).

Powered by [Embarcadero Delphi](https://www.embarcadero.com/products/delphi) and the [Python4Delphi library](https://github.com/pyscripter/python4delphi).

Sponsored by [Embarcadero](https://www.embarcadero.com/). 
