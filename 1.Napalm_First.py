# Appreicate ability of Napalm to output the data in Structured format

from napalm import get_network_driver
import json
import pandas as pd


driver = get_network_driver('ios')

device = driver(hostname='sandbox-iosxe-recomm-1.cisco.com',username='developer', password='C1sco12345',optional_args={'port':22})

device.open()

data = device.get_interfaces()


#1 Print data as-is

print(data)
print("*"*200)

#2 JSONify the data

print(json.dumps(device.get_interfaces(), sort_keys=True, indent=4))
print("*"*200)

#3 Pick just one element

print(data["GigabitEthernet1"])
print(data["GigabitEthernet1"]["is_up"])

#4 Get output in CSV format

table_format = pd.DataFrame.from_dict(data)

table_format.to_csv("table.csv")

device.close()
