# Only Origin Datasets
from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolo_chest_ct/yolo11n_chest_ct_.pt")

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

# all      0.997          1

# 영어 클래스 이름	한국어 번역
# ChestCT_ILD	흉부 CT_간질성 폐질환
# ChestCT_Lung_Cancer	흉부 CT_폐암
# ChestCT_Normal	흉부 CT_정상
# ChestCT_Pneumonia	흉부 CT_폐렴
# ChestCT_Pneumothorax	흉부 CT_기흉