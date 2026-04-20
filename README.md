🌍 EcoSort: AI-Powered IoT Waste Classifier

EcoSort is an intelligent waste management system built on MicroPython. By combining computer vision, the Google Gemini API, and precision robotics, it automatically identifies and segregates refuse into three streams: Recyclable, Non-Recyclable, and Organic.
________________________________________
✨ Core Capabilities

•	Intelligent Sensing: Instant object detection via infrared (IR) sensors
•	Vision-Based AI: Captures high-resolution imagery and leverages Gemini's multimodal capabilities for high-accuracy sorting
•	Automated Logistics: Motorized sorting tray system driven by servos and stepper motors
•	Interactive Feedback: Real-time data visualization on a 20x4 LCD and dynamic status lighting via NeoPixel LEDs
•	Cloud-Enabled: Integrated WiFi for remote telemetry and over-the-air updates
________________________________________
🛠️ Hardware Components

•	ESP32 Microcontroller
•	Camera Module (OV2640)
•	IR Sensor
•	4 Servo Motors
•	Stepper Motor
•	16x NeoPixel LED Ring
•	4x20 LCD Display
•	WiFi Module
________________________________________
🔩 Hardware Architecture

Component	Pin Number	Description
Front Servo 1	GPIO 9	Front sorting mechanism
Front Servo 2	GPIO 8	Front sorting mechanism
Drop Servo 1	GPIO 7	Drop mechanism
Drop Servo 2	GPIO 44	Drop mechanism
IR Sensor	GPIO 41	Object detection
NeoPixel Ring	GPIO 1	16 LEDs for status indication
Stepper Motor	GPIO 2,3,4,43	Half-step motor control
I2C SDA	GPIO 5	I2C data line
I2C SCL	GPIO 6	I2C clock line
Camera	Default pins	OV2640 camera module
Technical Note: Servos operate on a 50Hz PWM frequency. The LCD is pre-configured to I2C address 0x27.
________________________________________
📋 Prerequisites

•	MicroPython firmware
•	Python 3.x
•	ESP32 development board
•	Required hardware components
•	WiFi network access
•	Google Gemini API key
________________________________________

⚙️ Setup & Deployment

1. Firmware Initialization
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 micropython.bin
2. Library Dependencies
import upip
upip.install('urequests')
3. Configuration
Update Garbage-Separator.py with your local network details and API credentials:
•	SSID: Your network name
•	PASSWORD: Your WiFi security key
•	GEMINI_API_KEY: Your unique Google AI Studio key
________________________________________
🛠️ Operational Workflow

1.	Boot-up: Device initializes and establishes WiFi handshake
2.	Detection: IR Sensor triggers when object is placed in hopper
3.	Analysis: Camera captures frame → Gemini API classifies image
4.	Sorting: Stepper + Servos align chutes based on classification
5.	Completion: Item deposited, UI resets for next cycle
________________________________________
📊 Taxonomy of Waste

•	♻️ Recyclable: Metals, glass containers, clean paper, HDPE/PET plastics
•	🗑️ Non-Recyclable: Composite materials, contaminated packaging, residuals
•	🍎 Organic: Food scraps, garden waste, compostable matter
________________________________________
