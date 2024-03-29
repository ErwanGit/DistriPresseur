from machine import I2C, Pin
from I2C_LCD import I2CLcd

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
devices = i2c.scan()

def updateScreen(line1, line2):
    if devices != []:
        lcd = I2CLcd(i2c, devices[0], 2, 16)
        lcd.move_to(0, 0)
        lcd.putstr(line1[:16].center(16))
        lcd.move_to(0, 1)
        lcd.putstr(line2[:16].center(16))
        return True
    else:
        print("No address found")
        return False