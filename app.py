from ultralytics import YOLO
import supervision as sv
import os
import cv2
import argparse
from utils import dominant_color_hsv, classify_color_dominant, save_detected_img


def process_image(image):
    image = cv2.imread(image)
    model = YOLO('weights/best.pt')
    result = model.predict(image)[0]

    detections = sv.Detections.from_ultralytics(result)
    color_counts = {'red': 0, 'yellow': 0, 'green': 0}

    for xyxy in detections.xyxy:
        x_min, y_min, x_max, y_max = xyxy
        x_min, y_min, x_max, y_max = int(x_min), int(y_min), int(x_max), int(y_max)
        cropped_apple = image[y_min:y_max, x_min:x_max]
        if cropped_apple.size == 0 : # handling if the cropped apple is empty
                continue
                
        color = classify_color_dominant(cropped_apple)

        color_counts[color] += 1
        save_detected_img(cropped_apple, color, color_counts[color])

    print("Saved classified apples to 'result' folder.")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load an image of apple")
    parser.add_argument("image", help="Path to the image file")
    args = parser.parse_args()

    process_image(args.image)