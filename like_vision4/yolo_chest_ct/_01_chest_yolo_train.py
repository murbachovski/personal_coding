# Only Origin Datasets
from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolo11n-cls.pt")

# 2. 모델 훈련 - 의료영상에 맞게 증강기법 최소화 및 모자이크 끔
model.train(
    data="datasets",        # 훈련 데이터셋 경로
    epochs=300,
    batch=32,
    imgsz=512,
    patience=5,
    device="mps",
    hsv_h=0.0,
    hsv_s=0.0,
    hsv_v=0.0,
    translate=0.0,
    scale=0.0,
    fliplr=0.0,
    mosaic=0.0,
    erasing=0.0,
    auto_augment=None
)