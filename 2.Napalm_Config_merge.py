#Merge config. Use context manager to handle opening and closing of the connection.

from napalm import get_network_driver
import getpass

# Prompt user for username and password
print("Please enter Username and Password in next prompt")
uname = input('Username: ')
pwd = getpass.getpass(prompt='Password:')

driver = get_network_driver('ios')

#Using context manager to automatically open and close the connection to the device
with driver(hostname='10.10.20.48',username=uname, password=pwd,optional_args={'port':22}) as device:

    device.load_merge_candidate(filename="merge-config.txt")
    print(device.compare_config())
    choice = input("\n Are you happy with the changes? Type Yes or No: ")
    if str(choice.lower()) == 'yes':
        print("Saving config")
        device.commit_config()
    else:
        print("Discarding config change")
        device.discard_config()
