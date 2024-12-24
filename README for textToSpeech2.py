# Text-to-Speech from Image with GUI File Selection

This project extracts text from an image and converts it into speech. It allows users to select images from their device (PC or phone) using a GUI file picker.

## Features
- **Upload Image:** Use a file dialog to upload images.
- **Text Extraction:** Utilize EasyOCR to extract text from the uploaded image.
- **Text-to-Speech:** Convert the extracted text to speech using pyttsx3.
- **Speech Control:** Pause and resume speech at any point.

## Requirements

Ensure you have the following dependencies installed:

- Python 3.6+
- OpenCV (`cv2`)
- EasyOCR (`easyocr`)
- pyttsx3 (`pyttsx3`)
- Pickle (standard library)
- Tkinter (standard library)

Install EasyOCR and pyttsx3 using pip:
```bash
pip install easyocr pyttsx3
```

## How to Set Up

### 1. Install Dependencies
Follow the steps in the Requirements section to install the necessary libraries.

### 2. Run the Program
Save the code to a file, e.g., `text_to_speech_app.py`, and execute it in your terminal:
```bash
python text_to_speech_app.py
```

### 3. Select an Image
- A file dialog will open when prompted.
- Choose a `.jpg`, `.jpeg`, or `.png` image file.

### 4. Extract Text and Hear Speech
- Once the image is selected, the text will be extracted and read aloud.
- Control speech using the following commands:
  - **`p`**: Pause speech.
  - **`r`**: Resume speech.
  - **`q`**: Quit the program.

## Use Cases
- Accessibility: Helping visually impaired individuals hear text from images.
- Language Learning: Extract and listen to text in images for practice.
- Quick Notes: Extract text from snapshots for later reference.

## How to Customize

### Changing Speech Settings
Modify the `text_to_speech` function to adjust:
- **Rate:** Change `speech_engine.setProperty('rate', 150)`.
- **Volume:** Change `speech_engine.setProperty('volume', 1)`.

### Adding More Languages
Update the `extract_text_from_image` function with additional language support:
```python
reader = easyocr.Reader(['en', 'es'])  # Example: English and Spanish
```

### Extending File Formats
Update the `filetypes` parameter in `select_image` to support more formats:
```python
file_path = askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
```

## Documentation Links
- [OpenCV Documentation](https://docs.opencv.org/)
- [EasyOCR GitHub](https://github.com/JaidedAI/EasyOCR)
- [pyttsx3 Documentation](https://pyttsx3.readthedocs.io/en/latest/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)

## Contributing
Feel free to submit issues or fork the repository for further improvements.


