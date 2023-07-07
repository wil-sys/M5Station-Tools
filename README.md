# M5Station-Tools
A small set of python programs that show the M5Station's full potential.

# How to run theese programs on your device
Theese are meant to run on an M5Station Device, under a UIFlow 1.12.0 or higher enviroment.
To load theese on to your M5Station you must 1: put the device in UIFlow USB Mode
2: Download the latest version of Visual Studio Code, which can be found here https://code.visualstudio.com/Download
3: Install the M5Stack device addon in Visual Studio, and connect your M5Station to your computer
4: Use a program like device manager (Only on windows) or M5Burner to find your M5Station's serial port (It will look like COMxx) (Note: The serial port will have "FTDI" next to them in VSCode)
5: Connect to that serial port using the M5Stack addon in Visual Studio Code
6: Upload the .py files to the "apps" folder on the M5Station
7: Reboot the M5Sation into App mode, and select the app you want to run using the buttons

# How to use each program
## M5PSU
This is a piece of code that lets youre device act like a USB powerbank using the top USB-A Port.
The screen will show the state of charing (True or False) and the percentage
Button A Shows the screen if it has been turned off with Button C
Button B Enables or disables the USB-A power output
Button C Turns off the display

## SerialSniffer
This is used to "snoop" on UART serial lines
(Note: The default baud rate for the passthough is 9600, however this can be changed by modifing line 27 in the program: "uart1.init(YOUR_BAUD, bits=8, parity=None, stop=1) "YOUR_BAUD" should be your passthrough baud rate.)
The display shows the baud rate of both the passthrough and USB-C interface
The device should be connected through PortA1 and PortA2
This program also supports ESPNow AP mode with the following characteristics: 
AP Name: SerialSniffer
Channel: 11
Master Key: M5StationSniffer[Version Number] 

Theese programs are not developed by or associated with M5Stack
