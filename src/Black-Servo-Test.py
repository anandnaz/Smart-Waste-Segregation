import machine
import time

# Define the GPIO pins connected to the servos
SERVO1_PIN = 9 # Change this to your actual GPIO pin
SERVO2_PIN = 44  # Change this to another GPIO pin

# Initialize the servos using PWM
servo1 = machine.PWM(machine.Pin(SERVO1_PIN), freq=50)  # 50Hz PWM for servos
servo2 = machine.PWM(machine.Pin(SERVO2_PIN), freq=50)  # 50Hz PWM for servos

# Function to move both servos to the same angle (0 to 180 degrees)
def set_servos_angle(angle):
    if 0 <= angle <= 180:
        duty = int(20 + (angle / 180) * 100)  # Convert angle to duty cycle (20-120)
        servo1.duty(duty)
        servo2.duty(duty)
        print(f"Both servos moved to {angle}°")
    else:
        print("Invalid angle! Use 0 to 180.")

# Test servo movements
print("Moving both servos to 180°")
set_servos_angle(70)
time.sleep(3)

print("Moving both servos to 20°")
set_servos_angle(4)
time.sleep(3)

# Cleanup: Stop the servo PWM
servo1.deinit()
servo2.deinit()

