# Apple Object Detection and Color Classification

This repository contains a command-line interface (CLI) application for detecting apples and classifying their color using YOLOv11. The app processes an image provided by the user and outputs the detection and classification results.

## Features

- **Apple Detection:** Identifies apples in an input image using YOLOv11.
- **Color Classification:** Classifies the detected apples based on their color using dominant Hue value in HSV channel

## Installation

### Prerequisites

- Python 3.10 or later
- Pip (Python package manager)

### Steps

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/apple-detection-color-classification.git
   cd apple-detection-color-classification
   ```
2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage
Run the app with the following command:

```bash
python app.py path/to/image.jpg
```
Replace path/to/image.jpg with the path to your input image.

### Arguments
`image`: The path to the input image that you want to process.

### Example
```bash
python app.py ./images/apple.jpg
```
This command processes the image apple.jpg located in the ./images/ directory.

## Structure
`app.py`: Contains the main function process_image(image) that handles the input image and calls methods from utils.py.
`utils.py`: Includes helper functions used by app.py for detection and classification.

## Notes
Ensure the YOLOv11 model and its weights are correctly set up in the repository.
The app will output the detection and classification results to the console or save them as needed.

## Source
- [YOLOv11 pretrained model](https://docs.ultralytics.com/models/yolo11/#what-are-the-key-improvements-in-ultralytics-yolo11-compared-to-previous-versions)
- [Apple Object detection dataset for YOLOv11](https://universe.roboflow.com/robocup2022-jyu1j/apple-twvdf/dataset/3)
- [Supervision](https://supervision.roboflow.com/latest/)
- [OpenCV](https://github.com/opencv/opencv)
