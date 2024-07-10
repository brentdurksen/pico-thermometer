from machine import I2C, Pin
from time import sleep
from onewire import OneWire
from ds18x20 import DS18X20

# define the pin the thermometer is connected to
PIN = 12

dat = Pin(PIN)

# create the onewire object for the thermometer
ds = DS18X20(OneWire(dat))
# scan for devices on the bus
# we assume there is only one device connected
roms = ds.scan()

def read_temp():
    ds.convert_temp()
    sleep(0.2)
    return ds.read_temp(roms[0])