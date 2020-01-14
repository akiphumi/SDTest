# www.tctec.net
#
# Example of controlling the Top16 USB IO Module
# Version:   1.0
# Modified:  10-May-2016
#
# Uses pylibftdi
#
# Remember to run the python script as SUPER USER (sudo python top16)
# or run python and desktop as SUPER USER (sudo startx)
#
# Discover the name of your board with
#    sudo python -m pylibftdi.examples.list_devices
#
#

import time
import threading
import pylibftdi
from pylibftdi import Device
import subprocess
from subprocess import PIPE


# change this to the name of your device
# boardName = "FT3LK4CL"
proc = subprocess.run("python -m pylibftdi.examples.list_devices", shell=True, stdout=PIPE, stderr=PIPE, universal_newlines=True)
print(proc.stdout)
boardName = proc.stdout[21:29]
RESPONSE_DELAY = 0.04

top16 = Device(boardName)

# ---- Top16 Functions ----

Top16InputSetting = 0
Top16OutputSetting = 0


def setup():
    # Turn off the USB character buffer, allowing quicker communication and responses
    top16.ftdi_fn.ftdi_set_latency_timer(0)

    top16.baudrate = 115200


def queryVersion():
    top16.write("?\r")
    time.sleep(RESPONSE_DELAY)
    print("response: ")
    print(top16.read(6))
    print("\r\n")


# bits = the setting of the 8 digital outputs
# mask = which outputs are allowed to change

def setOutputs(bits, mask):
    top16.write("#%02X%02X\r" % (bits, mask));
    time.sleep(RESPONSE_DELAY)
    response = top16.read(6)
    # print("response: ")
    # print(response)
    # print("\r\n")
    try:
        Top16InputSetting = int(response[2:4], 16)
        Top16OutputSetting = int(response[4:6], 16)
    except ValueError:
        Top16InputSetting = -1
        Top16OutputSetting = -1


def getAnalog(gain, inputToRead):
    top16.write("#%01s%01d\r" % (gain, inputToRead))
    time.sleep(RESPONSE_DELAY)
    response = top16.read(6)
    # print("response: ")
    print(response)
    # print("\r\n")

    try:
        analogReading = int(response[2:6], 16)

    except ValueError:
        analogReading = -1

    return (analogReading)


def setPWM(output, setting):
    top16.write("#P%01d%02X\r" % (output, setting))
    time.sleep(RESPONSE_DELAY)
    response = top16.read(6)
    # print("response: ")
    # print(response)
    # print("\r\n")

    return (response)


def getInputs():
    top16.write("#0000\r");
    time.sleep(RESPONSE_DELAY)
    response = top16.read(6)
    # print("response: ")
    # print(response)
    # print("\r\n")
    try:
        Top16InputSetting = int(response[2:4], 16)
        Top16OutputSetting = int(response[4:6], 16)

    except ValueError:
        Top16InputSetting = -1
        Top16OutputSetting = -1

    return (Top16InputSetting)

    # ---- End Top16 Functions ----