from netmiko import ConnectHandler

def ssh_command(device, command):
    d=ConnectHandler(**device)
    output = d.send_command(command)
    d.disconnect()
    print()
    print(output)
    print("\n\n")    
    print("-"*45)
    print("\n\n")
    return 


def ssh_command2(device, command):
    d=ConnectHandler(**device)
    output = d.send_command(command)
    d.disconnect()
    return output 
