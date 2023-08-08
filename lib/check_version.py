import sys
from .objects import TempPrint
from .text import *

def check_python_version():
    version = sys.version_info

    TempPrint("-> Check a Python version...", 2).Tprint()
    if (version < (3, 10)):
        print("[-] Eyes only works with Python 3.10+.")
        exit("-> Go install the most recent version of python -> https://www.python.org/downloads/")

    else: 
        TempPrint(f"{GREEN}[+] 🐍 Your Python version is OK.{WHITE}\n", 2).Tprint()