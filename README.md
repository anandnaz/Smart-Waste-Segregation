![Typing SVG](https://readme-typing-svg.herokuapp.com?color=00FF00&size=22&center=true&vCenter=true&width=600&lines=AI+Powered+Waste+Sorting;ESP32+%2B+Computer+Vision;Patent+Pending+System)
#  EcoSort: AI-Powered IoT Waste Classifier

![Status](https://img.shields.io/badge/Status-Active-green)
![Build](https://img.shields.io/badge/Build-Stable-success)
![Platform](https://img.shields.io/badge/Platform-Thonny-blue)
![Language](https://img.shields.io/badge/MicroPython-Embedded-yellow)
![AI](https://img.shields.io/badge/AI-Gemini-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

 A patent-pending intelligent waste segregation system that uses AI + robotics to classify and sort waste in real-time automatically.

Automates the waste segregation process by detecting objects, capturing images, classifying them using AI, and physically sorting them using motors. This system reduces manual effort and improves efficiency in waste management.

EcoSort combines **computer vision**, **Google Gemini API**, and **embedded systems** to build a fully automated pipeline:

**Detection → AI Classification → Mechanical Sorting**

---

##  Problem Statement

Manual waste segregation leads to:
- Poor recycling efficiency  
- Contamination of recyclable materials  
- Increased environmental damage  

There is no widely adopted **low-cost, intelligent automation system** for real-time waste sorting.

---

##  Solution

EcoSort solves this by integrating:
- AI-based image classification  
- Real-time object detection  
- Automated motor-driven sorting  

This enables **hands-free, accurate, and scalable waste segregation**.

---

##  System Architecture

System Diagram
  
  <img width="300" height="400" alt="diagram" src="https://github.com/user-attachments/assets/81266cc4-343e-4e0d-bba5-ca862a0d02de" />

---

##  Core Capabilities

-  **Intelligent Sensing** – IR sensor detects object placement  
-  **Vision-Based AI** – Uses Gemini API for accurate classification  
-  **Automated Sorting** – Servo and stepper motor mechanism  
-  **Interactive Feedback** – 20x4 LCD display and NeoPixel LEDs  
-  **Cloud Connectivity** – WiFi-enabled telemetry and updates  

---

##  Intellectual Property

A patent application has been filed for this system.

- **Application Number:** 202541113884  
- **Status:** Patent Pending  

Details will be updated upon grant.

---

##  Innovation & Novelty

- Integration of real-time AI classification with mechanical sorting
- Use of cloud-based multimodal AI (Gemini) in embedded systems
- Fully automated pipeline from detection → classification → actuation
- Scalable design for smart city waste management systems

---

##  Hardware Components

- ESP32 Microcontroller  
- OV2640 Camera Module  
- IR Sensor  
- 4x Servo Motors  
- Stepper Motor  
- 16x NeoPixel LED Ring  
- 20x4 LCD Display (I2C)  
- WiFi Connectivity  

---

##  Hardware Architecture

| Component        | GPIO Pins       | Description                     |
|----------------|----------------|---------------------------------|
| Front Servo 1  | GPIO 9         | Front sorting mechanism         |
| Front Servo 2  | GPIO 8         | Front sorting mechanism         |
| Drop Servo 1   | GPIO 7         | Drop mechanism                  |
| Drop Servo 2   | GPIO 44        | Drop mechanism                  |
| IR Sensor      | GPIO 41        | Object detection                |
| NeoPixel Ring  | GPIO 1         | Status LEDs                     |
| Stepper Motor  | GPIO 2,3,4,43  | Half-step control               |
| I2C SDA        | GPIO 5         | LCD data line                   |
| I2C SCL        | GPIO 6         | LCD clock line                  |
| Camera         | Default pins   | OV2640 module                   |

**Technical Notes:**
- Servo PWM frequency: **50Hz**  
- LCD I2C Address: **0x27**

---

##  Tech Stack

- MicroPython firmware  
- Python 3.x  
- ESP32 development board  
- Required hardware components  
- WiFi network access  
- Google Gemini API key  

---

##  Installation & Setup

### 1. Flash MicroPython Firmware

```bash
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 micropython.bin
```
### 2. Install Dependencies

```md
```python
import upip
upip.install('urequests')
```

### 3. Configure Credentials

Edit Garbage-Separator.py:

```bash
SSID = 'your_wifi_ssid'
PASSWORD = 'your_wifi_password'
GEMINI_API_KEY = 'your_gemini_api_key'
```
---

##  How It Works (Detailed Flow)

1. **Object Detection**
   - IR sensor detects incoming waste
   - Triggers image capture

2. **Image Processing**
   - ESP32 camera captures a frame
   - Image sent to Gemini API

3. **AI Classification**
   - Gemini analyses object type
   - Returns category (Recyclable / Organic / Non-Recyclable)

4. **Decision Logic**
   - ESP32 maps category → motor action

5. **Mechanical Execution**
   - Stepper aligns chute
   - Servos open the correct bin

6. **Feedback System**
   - LCDs result
   - NeoPixel shows status

7. **Reset Cycle**
   - System prepares for the next object

---

##  Results & Performance

-  Average classification time: ~2–4 seconds  
-  Accuracy (tested on sample items): ~85–92%  
-  Continuous operation: Stable for multiple cycles  
-  WiFi latency impact: Medium (depends on network)

**Note: Accuracy varies with lighting and object clarity.**

---

##  Waste Classification

-  Recyclable – Metals, glass, clean paper, plastics
-  Non-Recyclable – Contaminated or composite waste
-  Organic – Food scraps, biodegradable waste

---

##  Hardware Prototype

Prototype

<img width="300" height="150" alt="WhatsApp Image 2026-04-19 at 11 59 37 AM" src="https://github.com/user-attachments/assets/b07d9ef7-e251-4756-8002-3c34277365bf" />
<br>
<img width="300" height="400" alt="WhatsApp Image 2026-04-19 at 11 58 37 AM (2)" src="https://github.com/user-attachments/assets/8aee622e-2cb9-410b-bf83-6e7eadfad86e" />

---

##  Design

images

<img width="300" height="300" alt="WhatsApp Image 2026-04-19 at 12 01 49 PM (1)" src="https://github.com/user-attachments/assets/9d4f4fd4-c806-492b-b4e8-8f33027f58be" />
<br>
<img width="300" height="300" alt="WhatsApp Image 2026-04-19 at 12 01 48 PM (1)" src="https://github.com/user-attachments/assets/10f80998-69a6-4e5f-aa25-4037c926faf1" />
<br>
<img width="300" height="400" alt="WhatsApp Image 2026-04-19 at 12 01 47 PM" src="https://github.com/user-attachments/assets/87bcb620-0f63-4c43-a897-b674040bb896" />

---

##  Use Cases

- Smart dustbins for cities  
- Waste segregation in apartments  
- Public places (railways, malls)  
- Educational & research prototypes  

---

##  Demo Summary

- Object placed → detected instantly  
- Classified via AI  
- Sorted automatically into the correct bin  

 No human intervention required

---

##  Future Scope

- Edge AI model for offline classification  
- Mobile/web dashboard for monitoring  
- Integration with smart city infrastructure  
- Waste analytics and reporting system  
- Solar-powered autonomous deployment  

---

##  Limitations

- Requires stable WiFi for cloud-based AI classification  
- Latency depends on API response time  
- Accuracy may vary with lighting conditions  
- Hardware cost may limit large-scale deployment  

---

##  Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

##  Acknowledgments

- Google Gemini API for waste classification
- MicroPython community
- Open-source hardware community

---

##  Support

For support, please open an issue in the repository or contact the maintainers.

---
