"""
Track the motion (acceleration and orientation) of a remote sensing node
Transmit and receive the information via the inbuilt BLE (Bluetooth Low-Energy) antenna
This replicates the radio communication used by real world sattelites

This example requries 2 microbits: a master and a remote node

This code is for the master microbit
Ensure that a second microbit has been programmed with the remote code

"""
radio_group = 7
radio.set_group(radio_group)
timeout = 2000
# how long we wait until asking where our remote node is
last_ping = input.running_time()

def on_received_value(name, value):
    serial.write_value(str(name), value)

def on_forever():  
    radio.on_received_value(on_received_value)
    time_now = input.running_time()
    if time_now - last_ping > timeout:
        serial.write_string("No connection to remote device(s))   
        last_ping = time_now

basic.forever(on_forever)
