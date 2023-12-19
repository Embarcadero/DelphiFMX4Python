DelphiFMX4Python - PyInstaller Sample[]()
# DelphiFMX4Python - PyInstaller Sample 


This is a sample that shows the use of the [PyInstaller](https://pyinstaller.org/en/stable/) package to create executables.
## Contents

* [1 Creating your app](#creating_your_app)
* [2 Making the PyInstaller spec file](#making_pyinstaller_spec_file)
* [3 Build your executable](#build_your_executable)

## Creating your app 

First thing first, install delphifmx as follows (use terminal):
```
python -m pip install delphifmx
```

Now let's install PyInstaller:
```
python -m pip install pyinstaller
```

Create a new folder and call it "installer". Inside your project folder, create a file called "delphifmxexecutable.py". Edit the "delphifmxexecutable.py" content to look like follows:

```
import delphifmx
input(delphifmx.__spec__)
```

## Making the PyInstaller spec file

Using a spec file will simplify your next buildings. Let's create a new spec file based upon project's main script file. In Terminal, run the following:

```
cd installer
pyi-makespec delphifmxexecutable.py
```

Now we need to setup the spec file to distribute the DelphiFMX package. Open the spec file and include the following code in the data list:

```
(r"<<<<THE DELPHI FMX FOLDER IN YOUR SITE-PACKAGES>>>>", "delphifmx")
```

This is how it looks to me:

```
...
datas=[(r"C:\Users\lmbelo\AppData\Local\Programs\Python\Python311\Lib\site-packages\delphifmx", "delphifmx")],
...
```
Note: you can remove the "docs" folder from delphifmx to make it smaller.

## Build your executable

We're now ready to build the exectable. Use the following command in Terminal to proceed:

```
pyinstaller delphifmxexecutable.spec
```

After that, you will see the dist folder within project's folder. The executable file will be available as "delphifmxexecutable.exe". You can customize the spec file as needed.