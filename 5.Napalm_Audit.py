from napalm import get_network_driver
import pprint
driver = get_network_driver('ios')
device = driver(hostname='10.10.20.48',username='developer', password='C1sco12345',optional_args={'port':22})

device.open()
pprint.pprint(device.compliance_report("audit.yml"))
device.close()