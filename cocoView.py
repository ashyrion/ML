from skimage import io
from skimage.draw import circle
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
import os
import json

anno_dir = "./train/annos/"
anno = "./train/annos/via_region_data.json"
image_dir = "./train/image/"


def imageViewer(anno, image_dir, image_id):
    with open(anno) as json_file:
        json_data = json.load(json_file)

    img_path = str(image_id) + ".jpg"
    poly = json_data[img_path]["regions"]["0"]["shape_attributes"]
    img_abs_path = os.path.join(image_dir, img_path)
    image = io.imread(img_abs_path)
    height, width = image.shape[:2]
    mask = np.zeros([height, width, 2], dtype=np.uint8)
    print(mask)
    rr, cc = Polygon(poly["all_points_x"], poly["all_points_y"])
    mask[rr, cc, 1] = 1
    io.imshow(image)
    plt.show()


def annoViewer(anno_dir, image_dir):
    directory = os.listdir(anno_dir)
    for anno in directory:
        with open(anno_dir + anno) as json_file:
            json_data = json.load(json_file)

        img_path = anno.replace('.json', '.jpg')

        img_abs_path = os.path.join(image_dir, img_path)
        image = io.imread(img_abs_path)
        height, width = image.shape[:2]
        img_size = height * width


