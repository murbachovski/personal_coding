from ultralytics import YOLO

# 1. 학습된 모델 로드
model = YOLO("yolo_chest_ct/yolo11n_chest_ct_.pt")  # 학습 결과 best.pt 경로 지정

results = model.predict("yolo_chest_ct/datasets/test/ChestCT_ILD",
                        imgsz=512,
                        device="mps",
                        conf=0.25
                        )
