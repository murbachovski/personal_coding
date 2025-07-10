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

# 📁 AIHub
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
ChestCT_ILD           : 흉부 CT_간질성 폐질환
ChestCT_Lung_Cancer   : 흉부 CT_폐암
ChestCT_Normal        : 흉부 CT_정상
ChestCT_Pneumonia     : 흉부 CT_폐렴
ChestCT_Pneumothorax  : 흉부 CT_기흉
```

# 🧪 Train Params
📌 *의료영상 특성을 고려하여, 데이터 증강을 최소화하고 모자이크를 비활성화했습니다.*
```
model.train(
    data="datasets",
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
```

# 🔢 Batch Size
<p align="center">
  <img src="https://github.com/user-attachments/assets/64892439-03e3-4c9c-af34-a6f77f905cac" width="1000">
</p>

# 📸 Confusion Matrix
<p align="center">
  <img src="https://github.com/user-attachments/assets/72c004d0-01e5-47bf-aa2c-58b4de1c5411" width="1000">
</p>

# 📈 Result Graphs
<p align="center">
  <img src="https://github.com/user-attachments/assets/c09f2a73-fdfc-41dc-afbd-de4c06c12b4d" width="1000">
</p>

# 🖼️ Result Images
<p align="center">
  <img src="https://github.com/user-attachments/assets/b98abc11-f5ee-423b-a74c-2f14c009e1cd" width="190">
  <img src="https://github.com/user-attachments/assets/fc389aa8-d61d-498c-be83-1d046e714aab" width="190">
  <img src="https://github.com/user-attachments/assets/c8b3bb14-4ece-469a-9d05-c8c6895e2bf3" width="190">
  <img src="https://github.com/user-attachments/assets/265a9a1f-605d-4b9c-8f0e-f215eeb0e5b6" width="190">
  <img src="https://github.com/user-attachments/assets/3728e4b8-8392-43ee-9308-fa1ef0506136" width="190">
</p>

---

## 📊 성능 평가 결과

| 클래스 | Top-1 Accuracy | Top-5 Accuracy |
|--------|----------------|----------------|
| 전체   | 99.67%         | 100.00%        |

- Top-1 Accuracy: 모델이 가장 높은 확률로 예측한 클래스가 실제 정답과 일치하는 비율  
- Top-5 Accuracy: 모델이 확률 상위 5개 예측 중에 실제 정답이 포함되는 비율

---

## 🎉 결론

YOLO11n classification 모델은 해당 검증 데이터셋에서 매우 높은 정확도를 보였습니다.  
Top-1 정확도 99.67%, Top-5 정확도 100%로 우수한 성능을 확인할 수 있습니다.

---
