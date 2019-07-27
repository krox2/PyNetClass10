from my_devices import devices
from my_functions import ssh_command2
from netmiko import ConnectHandler
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

start=time.time()

#use concurrent futures threading  to simultanesously gather "show version"
#Wait for all threads to complete.

max_threads = 5
pool = ThreadPoolExecutor(max_threads)

#Create list to append threads to
futures = []

#start each of the threads
for device in devices:
    futures.append(pool.submit(ssh_command2, device, "show version")) 

print("\n\n")
for future in as_completed(futures):
    print("*"*60)
    print(future.result())
    print("*"*60)

end= time.time()
print(f"runned {end-start:.2f} seconds")
