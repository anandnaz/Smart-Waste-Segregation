import time
from motor import HalfStepMotor  # Import the HalfStepMotor class from motor.py

# Define stepper motor pins (adjust based on your wiring)
PIN1 = 44   # IN1 of stepper driver
PIN2 = 43   # IN2 of stepper driver
PIN3 = 7   # IN3 of stepper driver
PIN4 = 8   # IN4 of stepper driver

# Initialize stepper motor
stepper = HalfStepMotor.frompins(PIN1, PIN2, PIN3, PIN4)

# Test the stepper motor
print("Moving stepper forward 100 steps")
stepper.step(100)  # Move forward 100 steps
time.sleep(2)

print("Moving stepper backward 100 steps")
stepper.step(-100)  # Move backward 100 steps
time.sleep(2)

print("Moving stepper to 180 degrees")
stepper.step_until_angle(180)  # Move to 180 degrees
time.sleep(2)

print("Moving stepper to 0 degrees")
stepper.step_until_angle(0)  # Move back to 0 degrees
