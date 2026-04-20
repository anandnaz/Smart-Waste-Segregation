import network
import time
import camera
import urequests
import ubinascii
import gc

# Replace with your Wi-Fi credentials
SSID = 'Capstone'
PASSWORD = 'kya karna hai'
GEMINI_API_KEY = 'AIzaSyCCIdhwgkYknFfMmeuReNSqh3Eta7jwslA'
prompt = "Categorise the waste material in this image into Recyclable, Non-recyclable, Organic. Answer only in these 3 categories and Single Word."

GEMINI_API_URL = f'https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key=AIzaSyCCIdhwgkYknFfMmeuReNSqh3Eta7jwslA'

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    print('Connecting to Wi-Fi...', end='')
    while not wlan.isconnected():
        print('.', end='')
        time.sleep(1)
    print('Connected!')
    print('Network config:', wlan.ifconfig())

# Connect to Wi-Fi
connect_to_wifi(SSID, PASSWORD)

# Initialize Camera
cam = camera.init()
if cam:
    print("✅ Camera initialized successfully!")
    
    # Set Camera Preferences
    camera.framesize(8)     # Frame size 800x600 (1.33 aspect ratio)
    camera.contrast(2)      # Increase contrast
    camera.speffect(0)      # Apply grayscale effect
    camera.brightness(1)    # Increase Brightness
    camera.quality(10)      # Quality to Max (lower is better) 10 - 63

    # Capture a Photo
    img = camera.capture()
    if img:
        print("📸 Photo captured successfully!")
        with open("photo.jpg", "wb") as f:
            f.write(img)
        print("✅ Photo saved as 'photo.jpg'")
        gc.collect()  # Garbage collection after saving the image
    else:
        print("❌ Failed to capture photo.")
else:
    print("❌ Camera initialization failed.")

def detect_waste_with_gemini(photo_path, prompt):
    headers = {
        'Content-Type': 'application/json'
    }
    with open(photo_path, 'rb') as f:
        img_data = f.read()
        encoded_img = ubinascii.b2a_base64(img_data).decode('utf-8').replace("\n", "")  # Encode image data in base64
        data = {
            "contents": [{
                "parts": [
                    {"text": prompt},
                    {"inline_data": {
                        "mime_type": "image/jpeg",
                        "data": encoded_img
                    }}
                ]
            }]
        }
        response = urequests.post(GEMINI_API_URL, headers=headers, json=data)
        gc.collect()  # Garbage collection after sending the request
        if response.status_code == 200:
            detection_results = response.json()
            print(f'✅ Waste detection results: {detection_results}')
            return detection_results
        else:
            print(f'❌ Failed to detect waste. Status code: {response.status_code}')
            print(f'Response: {response.text}')
            return None

# Detect waste using the Gemini API with a prompt
detection_results = detect_waste_with_gemini("photo.jpg", prompt)
gc.collect()  # Garbage collection at the end of the script