# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/micropython-i2c-lcd-esp32-esp8266/

from machine import Pin, SoftI2C
from machine_i2c_lcd import I2cLcd
from time import sleep

# Define the LCD I2C address and dimensions
I2C_ADDR = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = SoftI2C(sda=Pin(5), scl=Pin(6), freq=400000)

lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

lcd.putstr("It's working :)")
sleep(4)

try:
    while True:
        lcd.clear()
        lcd.putstr("Hello World!")  # Line 1
        sleep(2)

        lcd.clear()
        lcd.move_to(0, 1)  # Line 2
        lcd.putstr("ESP32S3 Sense")
        sleep(2)

        lcd.clear()
        lcd.move_to(0, 2)  # Line 3
        lcd.putstr("MicroPython LCD")
        sleep(2)

        lcd.clear()
        lcd.move_to(0, 3)  # Line 4
        lcd.putstr("20x4 I2C Display")
        sleep(2)

except KeyboardInterrupt:
    print("Keyboard interrupt")
    lcd.backlight_off()
    lcd.display_off()
