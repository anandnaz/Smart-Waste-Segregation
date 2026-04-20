from machine import Pin
import time

# Import the NeoPixel driver
from neopixel_driver import NeoPixel  # Save your driver as 'neopixel_driver.py'

# Define the NeoPixel Ring
PIN = 1  # Use GPIO6 or change to your preferred pin
NUM_PIXELS = 16  # 16 LED ring
np = NeoPixel(Pin(PIN), NUM_PIXELS)

# Function to test colors
def test_neopixel():
    colors = [(255, 255, 255)]  # Red, Green, Blue
    for color in colors:
        np.fill(color)  # Set all LEDs to the current color
        np.write()  # Send data to NeoPixel
        time.sleep(1)  # Wait for a second

# Run the test function
test_neopixel()
