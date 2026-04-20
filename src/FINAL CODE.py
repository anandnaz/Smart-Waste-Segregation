import machine
import time
import network
import camera
import urequests
import ubinascii
import gc
import os
from machine import Pin, SoftI2C
from neopixel_driver import NeoPixel
from motor import HalfStepMotor
from machine_i2c_lcd import I2cLcd

# Pin definitions
SERVO1_PIN_FRONT = 9
SERVO2_PIN_FRONT = 8
IR_SENSOR_PIN = 41
SERVO1_PIN_DROP = 7
SERVO2_PIN_DROP = 44
NEOPIXEL_PIN = 1
NUM_PIXELS = 16
STEPPER_PINS = [2, 3, 4, 43]
I2C_ADDR = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

# Initialize devices
np = NeoPixel(Pin(NEOPIXEL_PIN), NUM_PIXELS)
stepper = HalfStepMotor.frompins(*STEPPER_PINS)
i2c = SoftI2C(sda=Pin(5), scl=Pin(6), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
ir_sensor = Pin(IR_SENSOR_PIN, Pin.IN)

# Wi-Fi credentials
SSID = 'ANAND 7075'
PASSWORD = 'anand1401'
GEMINI_API_KEY = 'AIzaSyDZvN320mIsVDIyjAbjrzwgxQ3qEATAmbg'
GEMINI_API_URL = f'https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}'

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        time.sleep(1)
    print("Connected to Wi-Fi")

connect_to_wifi(SSID, PASSWORD)

camera.init()
camera.framesize(10)
camera.contrast(1)
camera.brightness(1)
camera.speffect(0)
camera.quality(10)

lcd.clear()
lcd.putstr("Ready")

def set_servos_angle(servo1, servo2, angle1, angle2):
    pwm1 = machine.PWM(machine.Pin(servo1), freq=50)
    pwm2 = machine.PWM(machine.Pin(servo2), freq=50)
    duty1 = int(20 + (angle1 / 180) * 100)
    duty2 = int(20 + (angle2 / 180) * 100)
    pwm1.duty(duty1)
    pwm2.duty(duty2)
    time.sleep(1)
    pwm1.deinit()
    pwm2.deinit()

def neopixel_fill(color):
    np.fill(color)
    np.write()

def capture_photo():
    print("Turning on white LED and capturing photo...")
    neopixel_fill((255, 255, 255))  # White light ON
    time.sleep(0.5)
    img = camera.capture()
    neopixel_fill((0, 0, 0))  # White light OFF

    if img:
        filename = f"/photo_{time.ticks_ms()}.jpg"
        with open(filename, "wb") as f:
            f.write(img)
            f.flush()
            os.sync()
        print(f"Photo saved: {filename}")
        return filename
    print("Failed to capture photo.")
    return None

def detect_waste(photo_path):
    print("Analyzing image...")
    try:
        with open(photo_path, 'rb') as f:
            encoded_img = ubinascii.b2a_base64(f.read()).decode('utf-8').replace("\n", "")
        data = {
            "contents": [{
                "parts": [
                    {
                        "text": "Analyze the waste item shown in the image. Identify the object present and categorize it into one of the following three categories: Biodegradable, Non-biodegradable, or Unknown. Provide a one-word answer indicating the category."
                    },
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": encoded_img
                        }
                    }
                ]
            }]
        }
        response = urequests.post(GEMINI_API_URL, headers={'Content-Type': 'application/json'}, json=data)
        print("Response received.")
        if response.status_code == 200:
            category = response.json().get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "Unknown")
            print(f"Category: {category}")
        else:
            print("API error.")
            category = "Unknown"
    except Exception as e:
        print("Detection error:", e)
        category = "Unknown"
    finally:
        try:
            os.remove(photo_path)
            print(f"Deleted photo: {photo_path}")
        except Exception as e:
            print("Delete error:", e)
    return category

try:
    while True:
        neopixel_fill((100, 100, 100))  # Idle gray
        if ir_sensor.value() == 0:
            lcd.clear()
            lcd.putstr("Processing...")
            print("Object detected.")
            set_servos_angle(SERVO1_PIN_FRONT, SERVO2_PIN_FRONT, 135, 49)
            time.sleep(2)
            set_servos_angle(SERVO1_PIN_FRONT, SERVO2_PIN_FRONT, 4, 180)
            time.sleep(3)

            photo = capture_photo()
            if photo:
                category = detect_waste(photo)
                lcd.clear()
                lcd.putstr(f"Category: {category}")
                time.sleep(2)

                if category == "Biodegradable":
                    print("Stepper for Biodegradable.")
                    stepper.step(600)
                elif category == "Non-biodegradable":
                    print("Stepper for Non-biodegradable.")
                    stepper.step(-600)

                time.sleep(2)
                set_servos_angle(SERVO1_PIN_DROP, SERVO2_PIN_DROP, 70, 70)
                time.sleep(3)
                set_servos_angle(SERVO1_PIN_DROP, SERVO2_PIN_DROP, 4, 4)
                time.sleep(3)

                if category == "Biodegradable":
                    stepper.step(-600)
                elif category == "Non-biodegradable":
                    stepper.step(600)

            lcd.clear()
            neopixel_fill((0, 0, 0))  # Off
            lcd.putstr("Ready")
            print("Ready for next.")
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Stopping...")
