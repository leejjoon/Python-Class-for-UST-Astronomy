.. raw:: html

   <link rel="stylesheet" href="jj.css" type="text/css">

.. raw:: html

   <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
    extensions: ["tex2jax.js"],
    jax: ["input/TeX", "output/HTML-CSS"],
    tex2jax: {
       inlineMath: [ ['$','$'], ["\\(","\\)"] ],
       displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
       processEscapes: true
    },
    "HTML-CSS": { availableFonts: ["TeX"] }
    });
   </script>
   <script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

.. role:: tex(raw)
   :format: latex html

.. role:: strike
    :class: strike

.. role:: red
    :class: red

.. container:: centeredtitle

   Introduction to Python for Astronomers : Lab 01

.. container:: centeredauthor

   Jae-Joon Lee (KASI)

----

Journey to Python.org
=====================

 - Python home page
    - http://python.org


----


Before you try Python
=====================

- Python : a language specification

  .. code-block:: python

     print "Hello world!"


- Python implementation

  - CPython

  - IronPython

  - Jython

  - etc

----

Python 2 vs. Python 3?
======================


Short version: Python 2.x is the status quo, Python 3.x is the present
and future of the language.

Benevolent Dictator for Life (BDFL; Guido van Rossum; the original
creator of the Python language) decided to clean up Python language
and to create Python 3.

 - with :red:`less regard for backwards compatibility` than is the
   case for new releases in the 2.x range.

 - The most drastic improvement is the better unicode support (with
   all text strings being unicode by default) as well as saner
   bytes/unicode separation.

:red:`We will primarily use Python 2.7 in this class`. But some Python 3
features will be introduced.

----

Python packages
===============

- Python : Python + Standard Library

- Python distribution : Re-packaged Python, often with more libraries


----

Python Program vs. Python Packages
==================================

 - Packages, Module, Library, etc.

   - Reusable python modules created by 3rd party.

 - Python package index

    - The Python Package Index is a repository of software for the Python programming language. 

    - http://pypi.python.org/pypi


----

Installing Python
=================

 - Windows

 - Mac OS X

 - Linux


----

Invoking the interpreter
========================

 - interpreter only

  .. code-block:: sh

     python

 - excute a python file

  .. code-block:: sh

     python filename.py

 - interpreter with gui

  .. code-block:: sh

     idle


----

Python as a Calculator I
========================

 - numbers
 - operators
 - expression

.. raw:: html

   <iframe src='http://127.0.0.1:8888/bd7f7c65-6a0f-42d9-b4e3-3e1436c49558' width=800 height=400></iframe>


----

Python as a Calculator II
=========================

 - assignment
 - strings
 - string operations : indexing, slicing (`Python Tutorial`_)

.. _Python Tutorial: http://docs.python.org/tutorial/introduction.html#strings

.. raw:: html

   <iframe src='http://127.0.0.1:8888/e78ef50e-f160-4658-83fd-5985c26fa2f5' width=800 height=400></iframe>


----

String Indexing
===============


 .. image:: string_diagram.png
    :width: 700



----

H/W
===

Read Python tutorial from beginning of section 3 to 3.1.2.


