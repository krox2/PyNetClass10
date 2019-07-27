from my_devices import devices
from netmiko import ConnectHandler
import time

def ssh(device, command):
    d=ConnectHandler(**device)
    return d.send_command(command)

start=time.time()

for device in devices:
    print()
    print(ssh(device, "show version"))
    print("\n\n")
    print("-"*45)
    print("\n\n")

end= time.time()
print(f"runned {end-start:.2f} seconds")
