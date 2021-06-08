'''
Measure total G Forces experienced by the microbit using ther on board accelerometer.
RMS (root mean square) is used to get the overall acceleration magnitude across all axes.

Try shaking the microbit and watching the plot of RMS_acc in the console
'''
from microbit import *

x_acc = 0
y_acc = 0
z_acc = 0
sample_rate = 20 #Hz

def on_forever():
    global x_acc, y_acc, z_acc, sample_rate
    basic.pause(1000/sample_rate) #set sample rate by delaying reading of sensor
    x_acc = input.acceleration(Dimension.X)
    y_acc = input.acceleration(Dimension.Y)
    z_acc = input.acceleration(Dimension.Z)
    rms_acc = Math.sqrt(x_acc**2 + y_acc**2 +z_acc**2 )*0.001 #in G's
    serial.write_value("RMS acc", rms_acc)

basic.forever(on_forever)
