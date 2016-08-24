#!/usr/bin/env python
import os
import sys

__all__ = ["setup"]

if "setup.py" not in str(getattr(sys.modules["__main__"],"__file__",None)):
    print("SKIP: not setup.py")
    sys.exit(0)

dirname = os.path.abspath(os.path.dirname(__file__))
if dirname in sys.path:
    sys.path.remove(dirname)
sys.path.insert(0, os.path.join(dirname,"packages"))

del sys.modules["setupfiles"]

import setupfiles # nopep8

def setup(**kwargs):
    setupfiles.setup(name="setupfiles",**kwargs)
