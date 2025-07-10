from ultralytics import YOLO

# 1. 학습된 모델 로드
model = YOLO("yolo_chest_x_ray/yolo_chest_x_ray_m.pt")  # 학습 결과 best.pt 경로 지정

results = model.predict("yolo_chest_x_ray/datasets/test/normal",
                        imgsz=256,
                        device="mps",
                        conf=0.25,
                        batch=32,
                        save=True
                        )