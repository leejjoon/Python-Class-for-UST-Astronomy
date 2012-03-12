Install Python
==============

Adopted from 

http://fperez.org/py4science/starter_kit.html

On Linux
--------

On a reasonably recent Linux distribution, all the tools you need are
available via the package management system. On Ubuntu or other
Debian-based distributions, type at the shell::

  sudo apt-get install ipython python-scipy python-matplotlib \
    cython python-nose python-setuptools python-sphinx build-essential

  sudo apt-get build-dep python python-scipy python-matplotlib cython

These two commands give you all the core packages to get started with
scientific Python work, including development tools like compilers. On
Fedora, the equivalent commands are (tested on Fedora 12)::

  sudo yum install yum-utils

  sudo yum install ipython scipy python-matplotlib Cython \
    python-nose python-setuptools python-sphinx 

  sudo yum-builddep python scipy python-matplotlib Cython

On Mac OSX
----------

You may install required packages using fink or macports, but your
mileage will vary. Alternatively, you can install the Enthought Python
Distribution (EPD). This has all of the above, and much more, in a single
installer. Unless you know fink or macports well, I recommend you to
install the EPD.

You will also want to have:

 - The Apple Xcode development toolkit. Once you register, it’s a free
   (but fairly large) download.

 - The GNU Fortran compiler.


On Windows
----------

Install EPD.

EPD
---

**If you want to install academic version of the Enthought Python
Distribution, check my google group post (or send me an email at
lee.j.joon@gmail.com)**.


Code Editor
-----------

Python is a programming language, so at some point you’ll need to type
code. **Learning how to use a good, powerful text editor is one of the
best investments of time you can make in terms of computing-related
skills**. I(=fperez)’m a life **emacs** user, but **vi** is equally
sophisticated (in a very different style). These editors, however,
aren’t the easiest to get started with (if you’re serious about
computing though, I strongly recommend you do learn how to use them).

If you want something with a slightly easier learning curve to begin
with, the following are all free, good options:

 - Linux: gedit (typically installed by default).

 - OSX: Text Wrangler, TextMate (not free)

 - Windows: Notepad++
