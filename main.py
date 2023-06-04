#!/usr/bin/env python3
import psutil
from playsound import playsound
import osascript

def main():

    battery = psutil.sensors_battery() #get battery status
    plugged = battery.power_plugged #check whether the charger is plugged or not
    osascript.osascript("set volume output volume 100") #send command to Mac to set device volume to max

    if not plugged: #if the charger gets unplugged
        playsound('audio.wav')

main()
