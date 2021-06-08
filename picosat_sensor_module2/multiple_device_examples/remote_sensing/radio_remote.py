"""
Track the motion (acceleration and orientation) of a remote sensing node
Transmit and receive the information via the inbuilt BLE (Bluetooth Low-Energy) antenna
This replicates the radio communication used by real world sattelites

This example requries 2 microbits: a master and a remote node

This code is for the remote microbit
Ensure that a second microbit has been programmed with the master code

"""
radio_group = 7
device_id = 0 #increment this if using more than 1 device
radio.set_group(radio_group)
sample_rate = 20 #Hz

def getAcc():
    x_acc = input.acceleration(Dimension.X)
    y_acc = input.acceleration(Dimension.Y)
    z_acc = input.acceleration(Dimension.Z)
    rms_acc = Math.sqrt(x_acc**2 + y_acc**2 +z_acc**2 )*0.001 #in G's
    return rms_acc

def getBearing():
    degrees = input.compass_heading() #North is at 0 and 360 degrees.
    return degrees


def on_forever():
    global device_id, sample_rate
    basic.pause(1000 / sample_rate)  
    bearing = getBearing()
    rms_acc = getAcc()
    radio.send_value(str(device_id)+'_acc', rms_acc)
    radio.send_value(str(device_id)+'_bearing', bearing)

basic.forever(on_forever)
