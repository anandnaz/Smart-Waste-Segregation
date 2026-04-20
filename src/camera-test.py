import camera

# **1️⃣ Initialize Camera**
cam = camera.init()
if cam:
    print("✅ Camera initialized successfully!")
    
    # **2️⃣ Set Camera Preferences**
    camera.framesize(10)     # Frame size 800x600 (1.33 aspect ratio)
    camera.contrast(2)       # Increase contrast
    camera.speffect(2)       # Apply grayscale effect

    # **3️⃣ Capture a Photo**
    img = camera.capture()
    if img:
        print("📸 Photo captured successfully!")
        with open("photo.jpg", "wb") as f:
            f.write(img)
        print("✅ Photo saved as 'photo.jpg'")
    else:
        print("❌ Failed to capture photo.")
else:
    print("❌ Camera initialization failed.")
