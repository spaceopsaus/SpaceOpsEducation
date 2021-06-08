# SpaceOps Educational Tools

The code in this repository is designed for use with the tutorials described at the [SpaceOps website](https://spaceops.com.au/education).
These tutorials currently include:
- [Picosat Sensor Module 2](https://spaceops.com.au/education/sensor-module-2-tutorial)

Instructions for each tutorial are located within the project's directory


## Instructions:
Projects can either be directly copied to microbits by copying the relevant .hex file to the device after plugging it into a computer via the microUSB cable, or code can be flashed to devices via the browser based application, as below:


1. Create a new project at https://makecode.microbit.org/
2. Select Python as the coding environment in the top bar.
3. Copy the relevant .py file to the editor.
4. Ensure that microbit device is connected in the application. Click the three dots beside the Download button and follow instructions to connect.
5. Flash the device via the Download button: `Download to micro:bit`. The LED on the device will blink repeatedly during this process if successful.

To see results in real time, connect the device (master device if using the radio example) via USB to computer. Logs and plots can be seen in the micro:bit application's console. Select `Show console` above the Download button. If this is not displayed, then nothing is currently being written to the device's serial port. Ensure that all devices have been flashed correctly

## Notes: 
-   When flashing a microbit, ensure that the yellow light is blinking, otherwise it is likely the connection has been lost but not acknowledged.
-   If after flashing the console option is not shown, try unplugging and replugging the microbit then reflash. Alternatively it may be that you are not properly writing to the serial port, try a working example frm this repo.
-   A microbit device powered by battery will not show the yellow LED even when turned on.
