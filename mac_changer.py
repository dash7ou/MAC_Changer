
'''
    Author: DashZou 
    Site: https://dashzou.web.app/
    GitHub: https://www.github.com/dash7ou
'''


# !/usr/bin/env python
import re
import optparse
import subprocess


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
    elif not options.new_mac or not re.match(r"(?:[0-9a-fA-F]:?){12}", options.new_mac):
        parser.error(
            "[-] Please specify a new MAC or enter right MAC, use --help for more info.")
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


def get_current_mac(interface):
    # make shure there are MAC to change, interface like "lo" has no MAC
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(
        r"(?:[0-9a-fA-F]:?){12}", ifconfig_result)

    if not mac_address_search_result:
        print("[-] Could not read MAC address.")

    print("Current MAC address => " + str(mac_address_search_result.group(0)))
    return mac_address_search_result.group(0)


options = get_arguments()
current_mac = get_current_mac(options.interface)
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print('[+] MAC address was successfully changed to ' + current_mac)
else:
    print('[-] MAC address did not get changed.')
