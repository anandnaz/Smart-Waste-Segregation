import machine
import time

# Define the GPIO pins connected to the servos and IR sensor
SERVO1_PIN = 9  # Change this to your actual GPIO pin
SERVO2_PIN = 8  # Change this to another GPIO pin
IR_SENSOR_PIN = 42  # IR sensor pin

# Initialize the servos using PWM
servo1 = machine.PWM(machine.Pin(SERVO1_PIN), freq=50)  # 50Hz PWM for servos
servo2 = machine.PWM(machine.Pin(SERVO2_PIN), freq=50)  # 50Hz PWM for servos

# Initialize the IR sensor pin
ir_sensor = machine.Pin(IR_SENSOR_PIN, machine.Pin.IN)

# Function to move each servo to a specific angle (0 to 180 degrees)
def set_servos_angle(angle1, angle2):
    if 0 <= angle1 <= 180 and 0 <= angle2 <= 180:
        duty1 = int(20 + (angle1 / 180) * 100)  # Convert angle to duty cycle (20-120)
        duty2 = int(20 + (angle2 / 180) * 100)  # Convert angle to duty cycle (20-120)
        servo1.duty(duty1)
        servo2.duty(duty2)
        print(f"Servo1 moved to {angle1}°, Servo2 moved to {angle2}°")
    else:
        print("Invalid angle! Use 0 to 180 for both angles.")

# Function to read the IR sensor value
def read_ir_sensor():
    return ir_sensor.value()

# Control servos based on IR sensor value
try:
    while True:
        sensor_value = read_ir_sensor()
        if sensor_value == 0:  # IR sensor is low
            print("IR sensor is low, moving servos.")
            set_servos_angle(135, 49)  # Move servos to angles 135° and 49°
            time.sleep(3)  # Wait for 3 seconds
            set_servos_angle(4, 180)  # Move servos back to 4° and 180°
        else:  # IR sensor is high, do nothing
            print("IR sensor is high, doing nothing.")
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping the script.")
    # Cleanup in case of interruption
    servo1.deinit()
    servo2.deinit()
    print("Stopped power to the servos")