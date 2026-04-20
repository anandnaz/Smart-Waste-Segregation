import machine
import time

# Define the GPIO pin connected to the IR sensor
IR_SENSOR_PIN = 42

# Initialize the IR sensor pin
ir_sensor = machine.Pin(IR_SENSOR_PIN, machine.Pin.IN)

# Function to read the IR sensor value
def read_ir_sensor():
    return ir_sensor.value()

# Test the IR sensor
print("Testing IR sensor on Pin 41")
for _ in range(10):
    sensor_value = read_ir_sensor()
    print(f"IR sensor value: {sensor_value}")
    time.sleep(1)

print("IR sensor test completed")