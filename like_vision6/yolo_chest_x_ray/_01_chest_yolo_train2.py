from ultralytics import YOLO

model = YOLO("yolo_brain_mri/yolo_brain_mri.pt")  # 기존 모델

model.train(
    data="yolo_brain_mri/datasets",
    epochs=300,
    batch=32,
    imgsz=256,
    device="mps",
    pretrained=True,  # 기존 가중치에서 시작
    patience=5,
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
