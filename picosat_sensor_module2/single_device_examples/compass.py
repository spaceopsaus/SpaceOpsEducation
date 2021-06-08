
'''
Uses the on board magnetometer (compass) to determine the bearing of the device.
Try laying the microbit flat on a table and rotating it slowly whilst watching the plot of in the console.

The first time this is run, microbit may ask you to calibrate it by rotating the deive until all LEDs are lit.
'''

def on_forever():
    degrees = input.compass_heading()
    if degrees < 45:
        basic.show_string("N")
    elif degrees < 135:
        basic.show_string("E")
    elif degrees < 225:
        basic.show_string("S")
    elif degrees < 315:
        basic.show_string("W")
    else:
        basic.show_string("N")
    serial.write_value("Bearing:", degrees)
basic.forever(on_forever)
