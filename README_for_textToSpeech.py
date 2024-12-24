# Text-to-Speech App with OCR Integration

This application captures an image using your webcam, extracts text from the image using OCR (EasyOCR), and converts the text to speech using a text-to-speech engine (pyttsx3). Additionally, it allows users to pause, resume, and control the speech output.

---

## Features
- Capture an image using your webcam.
- Extract text from the captured image using EasyOCR.
- Convert the extracted text to speech using pyttsx3.
- Control speech output: pause, resume, or quit.

---

## Requirements
- Python 3.8+
- Webcam or built-in camera
- Required Python libraries:
  - `opencv-python`
  - `easyocr`
  - `pyttsx3`
  - `pickle`

---

## Setup Instructions

### 1. Install Dependencies
Run the following command to install the required libraries:
```bash
pip install opencv-python easyocr pyttsx3
```

### 2. Verify Camera Setup
Ensure your webcam is connected and accessible. Test it by running the following code snippet:
```python
import cv2
cap = cv2.VideoCapture(0)
if cap.isOpened():
    print("Camera is working")
else:
    print("Unable to access the camera")
cap.release()
```

### 3. Run the Application
To start the app, execute:
```bash
python app.py
```
Follow the on-screen instructions to:
- Press `c` to capture an image.
- View extracted text and listen to speech output.

---

## Application Workflow
1. **Capture Image**:
   - The app uses OpenCV to capture an image from your webcam.
   - Press `c` to capture the image, or `q` to quit.

2. **Text Extraction**:
   - Extracts text from the captured image using EasyOCR.

3. **Text-to-Speech Conversion**:
   - Converts the extracted text to speech using pyttsx3.

4. **Speech Control**:
   - Use the following keys during the speech output:
     - Press `p` to pause.
     - Press `r` to resume.
     - Press `q` to quit.

---

## Use Cases
- **Accessibility Tools**: Assist visually impaired users by reading out text from images.
- **Document Scanning**: Quickly scan and read out text from physical documents.
- **Language Learning**: Help users practice reading and listening in English.

---

## Documentation Links
- [OpenCV Documentation](https://docs.opencv.org/)
- [EasyOCR Documentation](https://github.com/JaidedAI/EasyOCR)
- [pyttsx3 Documentation](https://pyttsx3.readthedocs.io/en/latest/)
- [Pickle Documentation](https://docs.python.org/3/library/pickle.html)

---

## Troubleshooting
1. **Camera Not Working**:
   - Ensure no other applications are using the camera.
   - Verify your camera drivers are installed and updated.

2. **Text Extraction Issues**:
   - Ensure the captured image has clear text with good lighting.
   - Use high-resolution captures for better OCR performance.

3. **Speech Not Playing**:
   - Check your audio settings.
   - Ensure the pyttsx3 library is installed and configured correctly.

---

## Contribution
Feel free to fork this repository, report issues, or suggest enhancements.

---

