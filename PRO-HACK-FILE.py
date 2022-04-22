import os, sys
try:
    __import__("naim2").bnsbuy()
except Exception as e:
    exit(str(e))