# -*- coding: utf-8 -*-

import os

def run(**args):
    
    print "[*] In dirister module."
    files = os.listdir(".")
    
    return str(files)
