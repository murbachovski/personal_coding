# 검증 코드

from ultralytics import YOLO

# Load a model
model = YOLO("yolo_chest_x_ray/yolo_chest_x_ray_m.pt")  # load an official model

# Validate the model
metrics = model.val(data="yolo_chest_x_ray/data.yaml", imgsz=256, batch=32, save=True)
print(f"Top-1 Accuracy: {metrics.top1 * 100:.2f}%")
print(f"Top-5 Accuracy: {metrics.top5 * 100:.2f}%")

# Top-1 Accuracy: 90.21%
# Top-5 Accuracy: 100.00%

# | 지표             | 의미                    | 까다로움 정도 |
# | -------------- | --------------------- | ------- |
# | Top-1 Accuracy | 가장 높은 점수 예측이 정답일 확률   | 가장 엄격   |
# | Top-5 Accuracy | 상위 5개 예측 중 하나가 정답일 확률 | 좀 더 관대  |
