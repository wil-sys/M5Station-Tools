from m5stack import *
from m5ui import *
from uiflow import *
from easyIO import *
import time


setScreenColor(0x222222)


USB = None



label0 = M5TextBox(77, 120, "Toggle USB", lcd.FONT_Default, 0xFFFFFF, rotate=0)
Status = M5TextBox(77, 104, "USB: ", lcd.FONT_Default, 0xFFFFFF, rotate=0)
title0 = M5Title(title="M5PSU", x=93, fgcolor=0x000000, bgcolor=0xff0000)
Battery = M5TextBox(0, 21, "label1", lcd.FONT_Default, 0xFFFFFF, rotate=0)
CHG = M5TextBox(0, 36, "Charging: ", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label1 = M5TextBox(11, 124, "Screen On", lcd.FONT_DefaultSmall, 0xFFFFFF, rotate=0)
label2 = M5TextBox(173, 124, "Screen Off", lcd.FONT_DefaultSmall, 0xFFFFFF, rotate=0)



def buttonB_wasPressed():
  global USB, uart1, uart2
  if USB == True:
    USB = False
    digitalWrite(12, 0)
  elif USB == False:
    USB = True
    digitalWrite(12, 1)
  Status.setText(str((str('USB: ') + str(USB))))
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonA_wasPressed():
  global USB, uart1, uart2
  axp.setLcdBrightness(50)
  pass
btnA.wasPressed(buttonA_wasPressed)

def buttonC_wasPressed():
  global USB, uart1, uart2
  axp.setLcdBrightness(0)
  pass
btnC.wasPressed(buttonC_wasPressed)


digitalWrite(12, 1)
USB = True
Status.setText(str((str('USB: ') + str(USB))))
axp.setChargeCurrent(axp.CURRENT_700MA)
while True:
  Battery.setText(str((str((map_value((axp.getBatVoltage()), 3.05, 4.15, 0, 100))) + str('%'))))
  CHG.setText(str((str('Charging: ') + str((axp.getChargeState())))))
  if axp.btnState(0x02):
    if (map_value((axp.getBatVoltage()), 3.05, 4.15, 0, 100)) > 75:
      rgb.setColorFrom(1, 3, 0x0000ff)
      rgb.setColorFrom(5, 7, 0x0000ff)
      wait(1)
      rgb.setColorAll(0x000000)
    elif (map_value((axp.getBatVoltage()), 3.05, 4.15, 0, 100)) > 50:
      rgb.setColor(2, 0x00ff00)
      rgb.setColor(3, 0x00ff00)
      rgb.setColor(5, 0x00ff00)
      rgb.setColor(6, 0x00ff00)
      wait(1)
      rgb.setColorAll(0x000000)
    elif (map_value((axp.getBatVoltage()), 3.05, 4.15, 0, 100)) > 25:
      rgb.setColor(3, 0xff0000)
      rgb.setColor(5, 0xff0000)
      wait(1)
      rgb.setColorAll(0x000000)
    elif (map_value((axp.getBatVoltage()), 3.05, 4.15, 0, 100)) < 25:
      rgb.setColor(3, 0xff0000)
      rgb.setColor(5, 0xff0000)
      wait(0.25)
      rgb.setColor(5, 0x000000)
      rgb.setColor(3, 0x000000)
      wait(0.25)
      rgb.setColor(5, 0xff0000)
      rgb.setColor(3, 0xff0000)
      wait(0.25)
      rgb.setColor(5, 0x000000)
      rgb.setColor(3, 0x000000)
      wait(0.25)
      rgb.setColorAll(0x000000)
  wait(1)
  wait_ms(2)