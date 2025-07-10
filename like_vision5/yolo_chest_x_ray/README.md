# 🚀 프로젝트 설명
```
Ultralytics YOLO11m-cls 기반으로 흉부 X-ray에서 Normal / Abnormal 분류하는 의료영상 특화 모델
```

# ⚙️ 환경 및 모델 정보
```
- Ultralytics 버전: 8.3.163
- Python 버전: 3.9.23
- PyTorch 버전: 2.7.1 (CPU, Apple M1)
- 모델: YOLO11n-cls (classification)
- 모델 구조: 47 layers, 1,532,429 parameters, 3.2 GFLOPs
```

# 🐍 가상환경 생성
```
conda create -n chest_x_ray python=3.10
pip install ultralytics
```

# 📁 Kaggle
<p align="center">
  <img src="https://github.com/user-attachments/assets/63e76387-784c-4b22-a0f8-8310af0839ce" width="1000">
  https://www.kaggle.com/datasets/tolgadincer/labeled-chest-xray-images
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/d8b20258-d663-4e5b-a986-ce2b6398a088" width="1000">
  https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia
</p>


# 🫁 Classes
```
0 Abnormal
1 normal
```

# 🧪 Train Params
📌 *의료영상 특성을 고려하여, 데이터 증강을 최소화하고 모자이크를 비활성화했습니다.*
```
model.train(
    data="yolo_chest_x_ray/datasets",
    epochs=300,
    batch=16,
    imgsz=256,
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
```

# 🔢 Batch Size
<p align="center">
  <img src="https://github.com/user-attachments/assets/71daf636-2184-4188-99e8-b6328474276d" width="1000">
</p>

# 📸 Confusion Matrix
<p align="center">
  <img src="https://github.com/user-attachments/assets/a6b3eef5-7211-4f1e-a783-341665eb885f" width="1000">
</p>

# 📈 Result Graphs
<p align="center">
  <img src="https://github.com/user-attachments/assets/804b5e47-53a4-4336-b339-f452f78b923e" width="1000">
</p>

# 🖼️ Result Images
<p align="center">
  <img src="https://github.com/user-attachments/assets/d43004f8-b9cd-4735-aefe-3de029e45e90" width="300">
  <img src="https://github.com/user-attachments/assets/074bc531-7793-4f1a-a883-156d7cb9c254" width="300">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/dec2d639-cf35-4ad1-b899-7d1984b42ec8" width="300">
  <img src="https://github.com/user-attachments/assets/9df6f924-ba80-4a0f-a079-afe7154761d6" width="300">
</p>

---

## 📊 성능 평가 결과

- Top-1 Accuracy: 모델이 가장 높은 확률로 예측한 클래스가 실제 정답과 일치하는 비율  
- Top-5 Accuracy: 모델이 확률 상위 5개 예측 중에 실제 정답이 포함되는 비율

---

## 🎉 결론

---
