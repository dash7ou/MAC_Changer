# !/usr/bin/env python
import subprocess

# if you want to work with pyton2 insted of input using raw_input
interface = input("Enter your interface you need to change its MAC > ")
new_mac = input("Enter new MAC > ")

print("[+] Change MAC address for " + interface + " to " + new_mac)

# this way is more secure than using string, you can not run commant we did not want to excute
subprocess.call(['ifconfig', interface, "down"])
subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
subprocess.call(['ifconfig', interface, 'up'])
