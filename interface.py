import ctypes
from ctypes import *
from pyfirmata import Arduino, util
from time import sleep
import copy

board = Arduino('COM6')  # Change to your port
print("Start blinking D13")

currentcycle = 0;
x = 0;
y = 0;
z = 0;

def getcurrentcycle():
    return currentcycle

def updatecurrentcycle(x):
    global currentcycle
    currentcycle = x


def getX():
    return x

def updateX(X):
    global x
    x = X

def getY():
    return y

def updateY(Y):
    global y
    y = Y

def getZ():
    return z

def updateZ(Z):
    global z
    z = Z


def set_communication(API, comNumber):
    response = API.COM_API_SetComType(ctypes.c_int(comNumber))
    return response


def open_link(API):
    response = API.COM_API_OpenLink(ctypes.c_int(24), ctypes.c_int(115200))
    return response

#Move desired axis by a certain distance and speed
def jog(API, axis, distance, speed):
    response = set_communication(API, 2)
    response = open_link(API)
    response = API.COM_API_Jog(ctypes.c_int(axis), ctypes.c_float(distance), ctypes.c_float(speed))
    return response

#Go to home, if 0 or 1 depending if you want each axis to go to home or not
def home(API, X, Y, Z):
    set_communication(API, 2)
    open_link(API)
    response = API.COM_API_Home(ctypes.c_int(X), ctypes.c_int(Y), ctypes.c_int(Z))
    return response

#Get coordinates of planes X Y and Z
def get_coordinates(API, buffer):
    API.COM_API_GetMachineStatus(ctypes.byref(buffer))
    smb_request = SMB_REQUEST()
    smb_request.receiveSome(buffer.raw)
    return smb_request.nPos

#load DLL and go home in all axis, returns DLL object
def start():
    AMC = ctypes.WinDLL
    lib_amc = AMC("C:/Users/Developer/PycharmProjects/SILAR/SILARRAZER/driver/amc4030/AMC4030.dll")
    print("load of AMC4030.dll succeed")
    home(lib_amc,1,1,1)
    sleep(15)
    return lib_amc


def arm_up(API):
    response = home(API,0,0,1)
    return response


def calculate_offset(start, goal):
    return goal - start


def go_to_point(points, cycles, ceiling, speed):
    API = start()
    buffer = ctypes.create_string_buffer(1000)
    current_position = get_coordinates(API, buffer)
    z_home = copy.deepcopy(current_position[2])
    for x in range(0,cycles):
        updatecurrentcycle(x)
        for point in points:
            jog(API,0,calculate_offset(current_position[0]/100000,point[0]), speed)
            jog(API, 1, calculate_offset(current_position[1]/100000, point[1]), speed)


            while ((current_position[0] != (point[0] * 100000)) or (current_position[1] != (point[1] * 100000))):
                current_position = get_coordinates(API, buffer)
                updateX(current_position[0]/100000)
                updateY(current_position[1]/100000)
                updateZ(current_position[2]/100000)
                sleep(0.5)

            current_position = get_coordinates(API, buffer)
            updateX(current_position[0] / 100000)
            updateY(current_position[1] / 100000)
            updateZ(current_position[2] / 100000)

            jog(API, 2, calculate_offset(current_position[2] / 100000, point[2]), speed)


            while current_position[2] != (point[2] * 100000):
                current_position = get_coordinates(API, buffer)
                updateX(current_position[0] / 100000)
                updateY(current_position[1] / 100000)
                updateZ(current_position[2] / 100000)
                sleep(0.5)


            sleep(point[3])


            jog(API,2, calculate_offset(current_position[2] / 100000, ceiling), speed)
            while current_position[2] != z_home:
                current_position = get_coordinates(API, ceiling)
                updateX(current_position[0] / 100000)
                updateY(current_position[1] / 100000)
                updateZ(current_position[2] / 100000)
                sleep(0.5)
            current_position = get_coordinates(API, buffer)
    home(API,1,1,1)

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



