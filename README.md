## COCO DATASET to Mask_RCNN

coco dataset 인 DeepFashion2 dataset으로 Mask_RCNN학습 진행

    python coco.py train --dataset=/Users/daegukim/PycharmProjects/ts_img/validation --weights=coco
    python coco.py train --dataset=/Users/daegukim/PycharmProjects/ts_img/validation --weights=last


## STEP1. 4만개 validation image를 통한 학습 진행

첫번째는 validation 데이터를 통해서 학습을 진행 하였으며.
40epoch 이후에 4+ layer 로 120epoch까지 진행하는 중

중간에 생성된 모델틍 통해서 image detect 진행... 결과는 이미지 인식율일 현저하게 떨어지며, class구분도 못하는 경우가 빈번하게 발생함

만약 최종까지 만족할만한 결과물이 나오지 않으면. Mask RCNN -> yolo V3로 변경할 예정
