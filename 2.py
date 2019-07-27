from my_devices import devices
from my_functions import ssh_command
from netmiko import ConnectHandler
import time
import threading

start=time.time()

#use legacy threading

threads = []

#start each of the threads
for device in devices:
    t = threading.Thread(target=ssh_command, args=(device, "show version"))
    threads.append(t)
    t.start()

#iterate through threads and wait for all to complete

for t in threads:
    t.join()

end= time.time()
print(f"runned {end-start:.2f} seconds")
