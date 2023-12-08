#!/usr/bin/env python3

import cv2
import os
import subprocess
import argparse

SCALE_FACTOR = 5

class ImageProcessor:
    DEFAULT_IMAGE_FORMAT = ".png"
    INTERPOLATION_METHOD = cv2.INTER_AREA

    @staticmethod
    def read_image(image_path):
        """Reads an image from the specified path."""
        image = cv2.imread(image_path)
        if image is None:
            raise IOError(f"Could not open or find the image {image_path}.")
        return image

    @staticmethod
    def resize_image(image, scale_factor):
        """Resizes the given image by a scale factor."""
        new_width = int(image.shape[1] * scale_factor)
        new_height = int(image.shape[0] * scale_factor)
        return cv2.resize(image, (new_width, new_height), interpolation=ImageProcessor.INTERPOLATION_METHOD)

    @staticmethod
    def save_image(image, image_path, format=DEFAULT_IMAGE_FORMAT):
        """Saves the image to the specified path with the given format."""
        base, _ = os.path.splitext(image_path)
        new_path = f"{base}_resized{format}"
        cv2.imwrite(new_path, image)
        return new_path

    @staticmethod
    def convert_to_jpg(image_path):
        """Converts the image at the given path to JPG format."""
        file_name, _ = os.path.splitext(image_path)
        output_file = f"{file_name}.jpg"
        subprocess.run(["convert", image_path, output_file], check=True)
        return output_file

def process_image(file_path, scale_factor=SCALE_FACTOR):
    """Process the image: resize and convert to JPG."""
    try:
        image = ImageProcessor.read_image(file_path)
        resized_image = ImageProcessor.resize_image(image, scale_factor)
        resized_image_path = ImageProcessor.save_image(resized_image, file_path)
        converted_image_path = ImageProcessor.convert_to_jpg(resized_image_path)
        print(f"Processed {file_path}: Resized to {resized_image_path}, Converted to {converted_image_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Resize and convert images.")
    parser.add_argument('images', nargs='+', help='Image files to process')
    args = parser.parse_args()

    for file_path in args.images:
        process_image(file_path)

if __name__ == "__main__":
    main()
