Installation
============

DelphiFMX package distribution is available via `PyPi <https://pypi.org/project/delphifmx/>`__ 
or by downloading the source via GitHub. DelphiFMX is compiled and made available for Windows, 
Linux, Mac OSX and Android platforms. All Python versions from 3.6 to 3.11 are supported.

Installing DelphiFMX via PIP
****************************

The easiest way to install DelphiFMX is via PIP:

.. code-block:: bash

   pip install delphifmx


Installing DelphiFMX from source
********************************

You can also install manually by downloading or cloning the repository from GitHub:
`github.com/Embarcadero/DelphiFMX4Python <https://github.com/Embarcadero/DelphiFMX4Python/>`__. 
After cloning or downloading, enter the root DelphiFMX4Python folder/directory and open the 
command prompt or Conda prompt with that path. Now install the package using:

.. code-block:: bash

   python setup.py install


Testing the Installation
************************

On your computer, open up the Python REPL either from the Command prompt or the Conda 
prompt. After installing the package using ``pip``, let's enter the Python REPL to understand
a few essential things. Python has a predefined ``dir()`` function that lists available names 
in the local scope. So, before importing anything, let's check the available names using the 
``dir()`` function.

.. code-block:: bash

   >>> dir()
   ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', 
   '__spec__']

Now let's import the installed ``delphifmx`` module to validate its installation and check for 
the output of the ``dir()`` function:

.. code-block:: bash

   >>> import delphifmx
   >>> dir()
   ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', 
   '__spec__', 'delphifmx']
