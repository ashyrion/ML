import os
import shutil
import json
from skimage import io

anno_dir = "./val/annos/"
image_dir = "./val/image/"

directory = os.listdir(anno_dir)

VIA_dict = {}


def seg_to_points(segmentation):
    """
    segmentation을 all_points_x, all_points_y로 변환
    """
    hl = len(segmentation) // 2
    x = [segmentation[x * 2] for x in range(hl)]
    y = [segmentation[x * 2 + 1] for x in range(hl)]
    return x, y


def lm_to_points(landmarks):
    """
    landmarks를 all_points_x, all_points_y로 변환
    """
    hl = len(landmarks) // 3
    x = [landmarks[x * 3] for x in range(hl)]
    y = [landmarks[1 + x * 3] for x in range(hl)]
    return x, y


for anno in directory:
    with open(anno_dir + anno) as json_file:
        json_data = json.load(json_file)

    img_path = anno.replace('.json', '.jpg')

    img_abs_path = os.path.join(image_dir, img_path)
    image = io.imread(img_abs_path)
    height, width = image.shape[:2]
    img_size = height * width

    all_points_x, all_points_y = seg_to_points(json_data['item1']['segmentation'][0])

    # all_points_x, all_points_y = lm_to_points(json_data['item1']['landmarks'])
    print(all_points_x)
    print(all_points_y)
    VIA_dict[img_path] = {"fileref": "",
                          "size": img_size,
                          "filename": img_path,
                          "base64_img_data": "",
                          "file_attributes": {},
                          "regions": {"0":
                                          {"shape_attributes": {"name": "polygon",
                                                                "all_points_x": all_points_x,
                                                                "all_points_y": all_points_y
                                                                },
                                           "region_attributes": {
                                               "id": json_data['item1']['category_id'],
                                               "name": json_data['item1']['category_name']
                                           }
                                           }
                                      }
                          }

    try:
        all_points_x, all_points_y = seg_to_points(json_data['item2']['segmentation'][0])
        print(all_points_x)
        print(all_points_y)
        item2_region = {"1":
                            {"shape_attributes": {"name": "polygon",
                                                  "all_points_x": all_points_x,
                                                  "all_points_y": all_points_y
                                                  },
                             "region_attributes": {
                                 "id": json_data['item2']['category_id'],
                                 "name": json_data['item2']['category_name']
                             }
                             }
                        }
        VIA_dict[img_path]["regions"] = item2_region
    except:
        print('item2 is not json', anno)

with open(image_dir + 'via_region_data.json', 'w') as f:
    json.dump(VIA_dict, f)
