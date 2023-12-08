#!/usr/bin/env python3

import cv2
import os
import subprocess
import argparse

DEFAULT_WIDTH = 6000
DEFAULT_HEIGHT = 6000

def read_image(image_path):
    """Reads an image from the specified path."""
    image = cv2.imread(image_path)
    if image is None:
        raise IOError(f"Could not open or find the image {image_path}.")
    return image

def resize_image(image, new_width, new_height):
    """Resizes the given image to the specified width and height."""
    return cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)

def save_image(image, image_path, format=".png"):
    """Saves the image to the specified path with the given format."""
    base, _ = os.path.splitext(image_path)
    new_path = f"{base}_resized{format}"
    cv2.imwrite(new_path, image)
    return new_path

def convert_to_jpg(image_path):
    """Converts the image at the given path to JPG format."""
    file_name, _ = os.path.splitext(image_path)
    output_file = f"{file_name}.jpg"
    subprocess.run(["convert", image_path, output_file], check=True)
    return output_file

def process_image(file_path, width, height):
    """Process the image: resize and convert to JPG."""
    try:
        image = read_image(file_path)
        resized_image = resize_image(image, width, height)
        resized_image_path = save_image(resized_image, file_path)
        converted_image_path = convert_to_jpg(resized_image_path)
        print(f"Processed {file_path}: Resized to {resized_image_path}, Converted to {converted_image_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Resize and convert images.")
    parser.add_argument('images', nargs='+', help='Image files to process')
    parser.add_argument('--width', type=int, default=DEFAULT_WIDTH, help='New width of images')
    parser.add_argument('--height', type=int, default=DEFAULT_HEIGHT, help='New height of images')
    args = parser.parse_args()

    for file_path in args.images:
        process_image(file_path, args.width, args.height)

if __name__ == "__main__":
    main()
