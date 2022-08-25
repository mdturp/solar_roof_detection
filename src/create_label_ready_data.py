"""This file creates label ready data. Label ready data means that the
data is ready to being labeled by a human annotator.
"""
import glob
import itertools
import os

import PIL
from PIL import Image
import tqdm

PIL.Image.MAX_IMAGE_PIXELS = 1312500000


def create_label_ready_data(input_file_path, output_dir, new_image_size):
    img = Image.open(input_file_path)
    name = os.path.basename(input_file_path)[:-4]

    w, h = img.size
    grid = itertools.product(range(0, h-h % new_image_size, new_image_size),
                             range(0, w-w % new_image_size, new_image_size))
    output_dir = os.path.join(output_dir, name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, j in grid:
        box = (j, i, j+new_image_size, i+new_image_size)
        output_file_path = os.path.join(output_dir, f"{name}_{i}_{j}.jpg")
        img.crop(box).save(output_file_path)


if __name__ == "__main__":
    file_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data_dir = os.path.join(os.path.dirname(file_dir), "data/raw_data")
    label_ready_data_dir = os.path.join(
        os.path.dirname(file_dir), "data/label_ready_data")
    search_dir = os.path.join(raw_data_dir, "*.tif")

    for raw_data_file_path in tqdm.tqdm(sorted(glob.glob(search_dir))):
        create_label_ready_data(
            input_file_path=raw_data_file_path,
            output_dir=label_ready_data_dir,
            new_image_size=500)
