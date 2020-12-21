import ctypes
from ctypes import *

AMC = ctypes.cdll.LoadLibrary
lib_amc = AMC("./driver/amc4030/AMC4030.dll")
print("load of AMC4030.dll succeed")

lib_amc.COM_API_SetComType(ctypes.c_int(2))