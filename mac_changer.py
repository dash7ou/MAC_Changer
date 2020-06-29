# !/usr/bin/env python
import subprocess
import optparse


# get aregument from shell
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="An interface to change its MAC address.")
    parser.add_option("-m", "--mac", dest="new_mac",
                      help="A new mac address to change old address")

    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error(
            "[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error(
            "[-] Please specify a new mac, use --help for more info.")
    else:
        return options


# change mac function
def change_mac(interface, new_mac):
    print("[+] Change MAC address for " +
          interface + " to " + new_mac)

    # this way is more secure than using string, you can not run commant we did not want to excute
    subprocess.call(['ifconfig', interface, "down"])
    subprocess.call(['ifconfig', interface,
                     'hw', 'ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])


options = get_arguments()
change_mac(options.interface, options.new_mac)
