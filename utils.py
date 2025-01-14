import os
import cv2
import numpy as np

def dominant_color_hsv(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h = hsv[:, :, 0]
    hist = cv2.calcHist([h], [0], None, [180], [0, 180]) # Calculate hue histogram
    peak = np.argmax(hist) # Find the peak (most frequent hue)
    return peak

def classify_color_dominant(image):
    if image.size == 0:
        return "unknown"
    dominant_hue = dominant_color_hsv(image)
    if dominant_hue < 10 or dominant_hue > 170:
        return "red"
    elif dominant_hue < 33:
        return "yellow"
    elif dominant_hue < 78:
        return "green"
    else:
        return "unknown"

def save_detected_img(image, color, count):
    result_dir = "result"
    os.makedirs(result_dir, exist_ok=True)
    filepath = os.path.join(result_dir, f"{color}_{count}.jpg")
    cv2.imwrite(filepath, image)