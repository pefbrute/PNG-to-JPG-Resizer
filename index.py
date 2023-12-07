#!/usr/bin/env python3

import cv2
import sys
import os
import subprocess

def resize_image(image_path, new_width, new_height):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not open or find the image {image_path}.")
        return None

    resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
    base, _ = os.path.splitext(image_path)
    resized_image_path = f"{base}_resized.png"  # Saving as PNG to avoid loss before conversion to JPG
    cv2.imwrite(resized_image_path, resized_img)
    print(f"Resized image saved as {resized_image_path}")
    return resized_image_path

def convert_to_jpg(file_path):
    file_name, _ = os.path.splitext(file_path)
    output_file = f"{file_name}.jpg"
    try:
        subprocess.run(["convert", file_path, output_file], check=True)
        print(f"Converted {file_path} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting file: {e}")

def main():
    new_width = 6000
    new_height = 6000

    for file_path in sys.argv[1:]:
        resized_image_path = resize_image(file_path, new_width, new_height)
        if resized_image_path:
            convert_to_jpg(resized_image_path)

if __name__ == "__main__":
    main()
