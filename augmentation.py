import os
import cv2 as cv
import numpy as np
import random


def flip_images(img, flipcode):
    flip = cv.flip(img, flipcode)
    return flip


def adjust_brightness(img, value):
    # Convert the image to float32 to avoid overflow/underflow
    img_float = img.astype(np.float32)

    # Adjust brightness by adding the value to all pixel values
    brightened_img = img_float + value

    # Clip values to the range [0, 255] and convert back to uint8
    brightened_img = np.clip(brightened_img, 0, 255).astype(np.uint8)

    return brightened_img


def adjust_opacity(img, opacity):
    # Apply opacity to the image
    img_with_opacity = cv.addWeighted(img, opacity, np.zeros_like(img), 1 - opacity, 0)
    return img_with_opacity


def rotate_image_without_cutoff(img, angle):
    # Get the image dimensions
    (h, w) = img.shape[:2]

    # Calculate the center of the image
    center = (w // 2, h // 2)

    # Calculate the rotation matrix
    M = cv.getRotationMatrix2D(center, angle, 1.0)

    # Calculate the new bounding dimensions of the image
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # Compute the new bounding dimensions of the image
    new_w = int((h * sin) + (w * cos))
    new_h = int((h * cos) + (w * sin))

    # Adjust the rotation matrix to take into account translation
    M[0, 2] += (new_w / 2) - center[0]
    M[1, 2] += (new_h / 2) - center[1]

    # Perform the actual rotation and return the image
    rotated_img = cv.warpAffine(img, M, (new_w, new_h), borderValue=(255, 255, 255))
    return rotated_img


def shear_image(img, shear_factor):
    height, width = img.shape[:2]

    # Calculate the necessary translation to accommodate negative shear
    if shear_factor < 0:
        translation_x = -shear_factor * height
    else:
        translation_x = 0

    # Define the transformation matrix with translation included
    M = np.array([[1, shear_factor, translation_x],
                  [0, 1, 0]], dtype=np.float32)

    # Calculate the new width accounting for the translation
    new_width = int(width + abs(shear_factor) * height)

    # Apply the shear transformation
    sheared_img = cv.warpAffine(img, M, (new_width, height))

    return sheared_img


def main():

    root = os.getcwd()
    os.chdir(root + '/finals/1doc+sign')
    root = os.getcwd()
    images = os.listdir()

    for _ in range(5):
        for i in images:
            imgPath = os.path.join(root, i)
            img = cv.imread(imgPath)
            img = cv.cvtColor(img,cv.COLOR_BGR2RGB)


            img = adjust_brightness(img, random.randrange(-5, 80))
            img = adjust_opacity(img, round(random.uniform(0.5,2), 3))
            img = rotate_image_without_cutoff(img, random.randrange(-10, 10))
            img = shear_image(img, random.uniform(0, 0.5) * -1**random.randrange(0,2))

            cv.imwrite('/Handwritten Texts/finals/doc+sign/' + str(_) + '__'+ i, img )


main()

