# !/usr/bin/env python

import subprocess

interface = input("Enter your interface you need to change its MAC > ")
new_mac = input("Enter new MAC > ")
print("[+] Change MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig "+ interface +" down", shell=True)
subprocess.call("ifconfig " + interface +" hw ether " + new_mac, shell=True)
subprocess.call("ifconfig "+ interface +" up", shell=True)