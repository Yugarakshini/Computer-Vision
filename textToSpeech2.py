import cv2
import easyocr
import pyttsx3
import pickle
import os
import threading
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Global variable to control the speech engine
speech_engine = None
speaking_thread = None
is_paused = False


# Function to select and upload an image from the phone (via file selection)
def select_image():
    Tk().withdraw()  # Hide the root Tkinter window
    file_path = askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        print(f"Image selected: {file_path}")
        return file_path
    else:
        print("No file selected.")
        return None


# Function to extract text from image using easyOCR
def extract_text_from_image(image_path):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image_path)

    # Extract text from OCR result
    extracted_text = " ".join([item[1] for item in result])
    return extracted_text


# Function to convert extracted text to speech
def text_to_speech(text):
    global speech_engine
    speech_engine = pyttsx3.init()
    speech_engine.setProperty('rate', 150)  # Speed of speech
    speech_engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    def speak():
        print("Speaking...")
        speech_engine.say(text)
        speech_engine.runAndWait()

    # Run speech in a separate thread so we can pause and resume
    global speaking_thread
    speaking_thread = threading.Thread(target=speak)
    speaking_thread.start()


# Function to pause the speech
def pause_speech():
    global is_paused
    if speech_engine is not None:
        is_paused = True
        speech_engine.stop()  # Stopping the speech engine for pause
        print("Speech paused")


# Function to resume the speech
def resume_speech(text):
    global is_paused
    if is_paused:
        is_paused = False
        print("Resuming speech...")
        text_to_speech(text)


# Function to save the pipeline model using pickle (optional)
def save_pipeline(model, filename="text_to_speech_model.pkl"):
    with open(filename, 'wb') as file:
        pickle.dump(model, file)
    print(f"Model saved as {filename}")


# Function to load the pipeline model (if needed)
def load_pipeline(filename="text_to_speech_model.pkl"):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            model = pickle.load(file)
        print(f"Model loaded from {filename}")
        return model
    else:
        print("Model file does not exist.")
        return None


# Main function to run the pipeline
def main():
    # Select the image (from phone or PC)
    image_path = select_image()

    if image_path is None:
        return

    # Extract text from the image
    extracted_text = extract_text_from_image(image_path)
    print("Extracted Text:", extracted_text)

    # Convert extracted text to speech
    text_to_speech(extracted_text)

    # Give user options to control speech
    while True:
        key = input("Press 'p' to pause, 'r' to resume, or 'q' to quit: ").lower()
        if key == 'p':
            pause_speech()
        elif key == 'r':
            resume_speech(extracted_text)
        elif key == 'q':
            if speaking_thread.is_alive():
                speech_engine.stop()  # Stop speech if running
            break

    # Optional: Save the model (this could be any part of the process you'd like to pickle)
    save_pipeline(None)  # Saving a 'None' object just as an example (no model in this specific case)


if __name__ == "__main__":
    main()