# Picosat Sensor Module 2

The second sensing module is a fun little package of environmental sensing which includes temperature, humidity and photodiode(Lux) sensing.
From our previous three lessons, we have worked to combine these three sensors into a neat little board that provides easy plug and play into the carrier board.

See the [online tutorial](https://spaceops.com.au/education/sensor-module-2-tutorial) for detailed instructions.
![sensor_module_2](https://github.com/spaceopsaus/SpaceOpsEducation/blob/master/picosat_sensor_module2/images/SM2_04.jpg "Sensor Module 2")

This tutorial is designed for use with either one or multiple picosat sensing modules. The relevant examples are included in each directory and include:
* Single Device
  * Compass
  * G Forces
* Multiple Devices
  * Remote Sensing

## Instructions:
Projects can either be directly copied to microbits by copying the relevant .hex file to the device after plugging it into a computer via the microUSB cable, or code can be flashed to devices via the [browser based application](https://makecode.microbit.org/), as below:


1. Create a new project at [https://makecode.microbit.org/](https://makecode.microbit.org/)
2. Select Python as the coding environment in the top bar.
3. Copy the text from the relevant .py file in this repsotiry to the editor in the browser.
4. Ensure that microbit device is connected in the application. Click the three dots beside the Download button and follow instructions to connect.
5. Flash the device via the Download button: `Download to micro:bit`. The LED on the device will blink repeatedly during this process if successful.

To see results in real time, connect the device (master device if using the radio example) via USB to computer. Logs and plots can be seen in the micro:bit application's console. Select `Show console` above the Download button. If this is not displayed, then nothing is currently being written to the device's serial port. Ensure that all devices have been flashed correctly

## Notes: 
-   When flashing a microbit, ensure that the yellow light is blinking, otherwise it is likely the connection has been lost but not acknowledged.
-   If after flashing the console option is not shown, try unplugging and replugging the microbit then reflash. Alternatively it may be that you are not properly writing to the serial port, try a working example frm this repo.
-   A microbit device powered by battery will not show the yellow LED even when turned on.
