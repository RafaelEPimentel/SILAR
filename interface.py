import ctypes
from ctypes import *

AMC = ctypes.cdll.LoadLibrary
lib_amc = AMC("./driver/amc4030/AMC4030.dll")
print("load of AMC4030.dll succeed")


def set_communication(API, comNumber):
    response = API.COM_API_SetComType(ctypes.c_int(comNumber))
    return response


def open_link(API):
    response = API.COM_API_OpenLink(ctypes.c_int(24),ctypes.c_int(115200))
    return response


def jog(API,axis,distance,speed):
    response = API.COM_API_Jog(ctypes.c_int(axis),ctypes.c_float(distance),ctypes.c_float(speed))
    return response


response2 = set_communication(lib_amc, 2)
response3 = open_link(lib_amc)
response4 = jog(lib_amc,0,24,4)


