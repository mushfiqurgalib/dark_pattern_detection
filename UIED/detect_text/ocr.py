import cv2
import os
import json
from base64 import b64encode
import time
import pytesseract
from PIL import Image



def ocr_detection_tesseract(imgpath):
    # Start the timer
    start = time.time()
    
    # Load the image using PIL
    try:
        img = Image.open(imgpath)
    except FileNotFoundError:
        print("File not found: {}".format(imgpath))
        return None
    except Exception as e:
        print("An error occurred while opening the image: {}".format(e))
        return None
    
    # Perform OCR using Tesseract
    try:
        text = pytesseract.image_to_string(img)
    except Exception as e:
        print("An error occurred during OCR processing: {}".format(e))
        return None
    
    # Print the time taken
    print("*** Text Detection Time Taken: {:.3f}s ***".format(time.time() - start))
    
    # Split the text into lines (or words) for individual text annotations
    lines = text.split('\n')
    
    # Create a JSON response similar to Google OCR
    text_annotations = [{'description': line} for line in lines if line.strip()]
    response = {
        'responses': [{
            'textAnnotations': text_annotations
        }]
    }
    
    # Return the relevant part of the response
    return response['responses'][0]['textAnnotations']

# Example usage
annotations = ocr_detection_tesseract(imgpath)
if annotations:
    for annotation in annotations:
        print(annotation['description'])
