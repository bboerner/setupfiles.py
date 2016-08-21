#!/usr/bin/env python
import os
import sys

__all__ = ["setup"]

if "setup.py" not in str(getattr(sys.modules["__main__"],"__file__",None)):
    print("SKIP: not setup.py")
    sys.exit(0)

#if os.getcwd() in sys.path:
    #sys.path.remove(os.getcwd())
if os.path.dirname(__file__) in sys.path:
    sys.path.remove(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__),"packages"))

del sys.modules["setupfiles"]

import setupfiles # nopep8

def setup(**kwargs):
    setupfiles.setup(name="setupfiles",**kwargs)
