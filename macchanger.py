#!/usr/bin/env python

import subprocess

interface=input("interface > ")
newmac=input("newmac > ")

subprocess.call(["ifconfig",  interface, "down"])
subprocess.call(["ifconfig",  interface, "hw", "ether",  newmac])
subprocess.call(["ifconfig", interface, "up"])
subprocess.call(["ifconfig"])

