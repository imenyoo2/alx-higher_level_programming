#!/usr/bin/python3
import os
import sys

data = "and that piece of art is useful - Dora Korpar, 2015-10-19\n"
os.write(2, bytes(data, encoding='utf-8'))
sys.exit(1)
