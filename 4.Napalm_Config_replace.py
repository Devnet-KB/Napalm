from napalm import get_network_driver

driver = get_network_driver('ios')

device = driver(hostname='sandbox-iosxe-recomm-1.cisco.com',username='developer', password='C1sco12345',optional_args={'port':22})

device.open()

device.load_replace_candidate(filename='new-config.txt')

print(device.compare_config())

choice = input("\n Are you happy with the changes? Type Y/N for Yes or No: ")

if str(choice.lower()) == 'y':
    print("Saving config")
    device.commit_config()
else:
    print("Discarding config change")
    device.discard_config()

device.close()

