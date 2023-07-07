from m5stack import *
from m5ui import *
from uiflow import *
from libs.m5_espnow import M5ESPNOW


setScreenColor(0x222222)


Version = None
Data = None

now = M5ESPNOW(11, 1)

label0 = M5TextBox(0, 25, "Passthrough on PortA 9600Baud", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label1 = M5TextBox(0, 39, "USB Output at 115200Baud", lcd.FONT_Default, 0xFFFFFF, rotate=0)
title0 = M5Title(title="Serial Sniffer VX.X.X", x=47, fgcolor=0xFFFFFF, bgcolor=0x0000FF)
label2 = M5TextBox(0, 55, "ESPNOW AP Mode on channel 11", lcd.FONT_DefaultSmall, 0xFFFFFF, rotate=0)
ESPNOWMac = M5TextBox(0, 65, "XX:XX:XX:XX:XX:XX", lcd.FONT_DefaultSmall, 0xFFFFFF, rotate=0)
Masterkey = M5TextBox(0, 75, "M5StationVX.X", lcd.FONT_DefaultSmall, 0xFFFFFF, rotate=0)




Version = '1.0'
uart1 = machine.UART(1, tx=33, rx=32)
uart1.init(9600, bits=8, parity=None, stop=1)
uart2 = machine.UART(2, tx=1, rx=3)
uart2.init(115200, bits=8, parity=None, stop=1)
now.espnow_set_ap('SerialSniffer', '')
now.espnow_set_pmk(((str('M5StationSniffer') + str(Version))))
uart2.write('M5Station Serial Sniffer Version 1.0 By wil-sys https://github.com/wil-sys'+"\r\n")
title0.setTitle(str((str('Serial Sniffer ') + str(Version))))
ESPNOWMac.setText(str((str('MAC:') + str((now.espnow_get_mac(1))))))
Masterkey.setText(str((str('MasterKey:') + str(((str('M5StationSniffer') + str(Version)))))))
while True:
  if uart1.any():
    rgb.setColor(1, 0x0000ff)
    rgb.setColor(7, 0x0000ff)
    rgb.setColor(4, 0x00ff00)
    Data = uart1.readline()
    uart2.write(str(Data)+"\r\n")
    now.espnow_broadcast_data(((str('Received:') + str(Data))))
  elif uart2.any():
    rgb.setColor(1, 0x00ff00)
    rgb.setColor(7, 0x00ff00)
    rgb.setColor(4, 0x0000ff)
    Data = uart2.readline()
    uart1.write(str(Data)+"\r\n")
    now.espnow_broadcast_data(((str('Sent:') + str(Data))))
  wait_ms(2)
