import ctypes
from ctypes import *
from pyfirmata import Arduino, util
from time import sleep

board = Arduino('COM6')  # Change to your port
print("Start blinking D13")

AMC = ctypes.WinDLL
lib_amc = AMC("C:/Users/Developer/PycharmProjects/SILAR/SILARRAZER/driver/amc4030/AMC4030.dll")
print("load of AMC4030.dll succeed")


def set_communication(API, comNumber):
    response = API.COM_API_SetComType(ctypes.c_int(comNumber))
    return response


def open_link(API):
    response = API.COM_API_OpenLink(ctypes.c_int(24), ctypes.c_int(115200))
    return response


def jog(API, axis, distance, speed):
    response = API.COM_API_Jog(ctypes.c_int(axis), ctypes.c_float(distance), ctypes.c_float(speed))
    return response


def home(API, X, Y, Z):
    response = API.COM_API_Home(ctypes.c_int(X), ctypes.c_int(Y), ctypes.c_int(Z))
    return response


def getMachineStatus(API, buffer):
    response = API.COM_API_GetMachineStatus(ctypes.byref(buffer))
    return response


response2 = set_communication(lib_amc, 2)
response3 = open_link(lib_amc)
home(lib_amc, 0, 0, 1)
sleep(10)
counter = 0

nposarr = c_uint32 * 3
nspeedarr = c_uint32 * 3
rsvarr = c_uint32 * 4


class SMB_REQUEST(Structure):
    _fields_ = [
        ("dwWorkStatus", c_uint32),
        ("dwHomeDone", c_uint8),
        ("nID", c_uint8),
        ("FirmVer", c_uint16),
        ("nPos", nposarr),
        ("RealSpeed", nspeedarr),
        ("nAlmCode", c_uint32),
        ("dwInputStatus", c_uint16),
        ("dwOutputStatus", c_uint16),
        ("Rsv", rsvarr)]

    def receiveSome(self, bytes):
        fit = min(len(bytes), ctypes.sizeof(self))
        ctypes.memmove(ctypes.addressof(self), bytes, fit)


smb_request = SMB_REQUEST()

bigbuffer = ctypes.create_string_buffer(1000)

while counter < 6:
    board.digital[13].write(1)
    response2 = set_communication(lib_amc, 2)
    response3 = open_link(lib_amc)
    response5 = jog(lib_amc, 2, -25, 10)
    print(response5)
    sleep(4)
    getMachineStatus(lib_amc, bigbuffer)
    smb_request.receiveSome(bigbuffer.raw)
    print("X: " + str(smb_request.nPos[0]))
    print("Y: " + str(smb_request.nPos[1]))
    print("Z: " + str(smb_request.nPos[2]))
    board.digital[13].write(0)
    response2 = set_communication(lib_amc, 2)
    response3 = open_link(lib_amc)
    response7 = jog(lib_amc, 2, 25, 10)
    print(response7)
    sleep(2)
    counter = counter + 1
    sleep(3)
    print(counter)
    getMachineStatus(lib_amc, bigbuffer)
    smb_request.receiveSome(bigbuffer.raw)
    print("X: " + str(smb_request.nPos[0]))
    print("Y: " + str(smb_request.nPos[1]))
    print("Z: " + str(smb_request.nPos[2]))

print(response2)
print(response3)
# print(response4)
print(response5)
print(counter)
