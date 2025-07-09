# 🚀 프로젝트 설명
```
Ultralytics YOLO11n-cls 기반으로 흉부 CT에서 5가지 질환을 분류하는 의료영상 특화 모델
```

# 환경 및 모델 정보
```
- Ultralytics 버전: 8.3.163
- Python 버전: 3.9.23
- PyTorch 버전: 2.7.1 (CPU, Apple M1)
- 모델: YOLO11n-cls (classification)
- 모델 구조: 47 layers, 1,532,429 parameters, 3.2 GFLOPs
```

# 🐍 가상환경 생성
```
conda create -n chestct python=3.10
pip install ultralytics
```

# AIHub
<p align="center">
  <img src="https://github.com/user-attachments/assets/f9330667-f430-4126-b90d-ea9acdda600b" width="1000">
</p>

# Classes
```
ChestCT_ILD           : 흉부 CT_간질성 폐질환
ChestCT_Lung_Cancer   : 흉부 CT_폐암
ChestCT_Normal        : 흉부 CT_정상
ChestCT_Pneumonia     : 흉부 CT_폐렴
ChestCT_Pneumothorax  : 흉부 CT_기흉
```

# Train Params
```
# 모델 훈련 - 의료영상에 맞게 증강기법 최소화 및 모자이크 끔
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

# 📸 Batch Size
<p align="center">
  <img src="https://github.com/user-attachments/assets/64892439-03e3-4c9c-af34-a6f77f905cac" width="1000">
</p>

# 📸 Confusion Matrix
<p align="center">
  <img src="https://github.com/user-attachments/assets/72c004d0-01e5-47bf-aa2c-58b4de1c5411" width="1000">
</p>

# 📸 Result Graphs
<p align="center">
  <img src="https://github.com/user-attachments/assets/c09f2a73-fdfc-41dc-afbd-de4c06c12b4d" width="1000">
</p>

# 📸 Result Images
<p align="center">
  <img src="https://github.com/user-attachments/assets/b98abc11-f5ee-423b-a74c-2f14c009e1cd" width="190">
  <img src="https://github.com/user-attachments/assets/fc389aa8-d61d-498c-be83-1d046e714aab" width="190">
  <img src="https://github.com/user-attachments/assets/c8b3bb14-4ece-469a-9d05-c8c6895e2bf3" width="190">
  <img src="https://github.com/user-attachments/assets/265a9a1f-605d-4b9c-8f0e-f215eeb0e5b6" width="190">
  <img src="https://github.com/user-attachments/assets/3728e4b8-8392-43ee-9308-fa1ef0506136" width="190">
</p>

# YOLO11n Chest CT Classification 모델 검증 결과
---

## 성능 평가 결과

| 클래스 | Top-1 Accuracy | Top-5 Accuracy |
|--------|----------------|----------------|
| 전체   | 99.67%         | 100.00%        |

- Top-1 Accuracy: 모델이 가장 높은 확률로 예측한 클래스가 실제 정답과 일치하는 비율  
- Top-5 Accuracy: 모델이 확률 상위 5개 예측 중에 실제 정답이 포함되는 비율

---

## 결론

YOLO11n classification 모델은 해당 검증 데이터셋에서 매우 높은 정확도를 보였습니다.  
Top-1 정확도 99.67%, Top-5 정확도 100%로 우수한 성능을 확인할 수 있습니다.

---






# 🧠 Chest CT Disease Classification with YOLO11n-cls

Ultralytics YOLO11n-cls 기반으로 흉부 CT에서 5가지 질환을 분류하는 **의료영상 특화 분류 모델**입니다.

---

## ⚙️ 환경 및 모델 정보

- 🐍 Python 버전: `3.9.23`
- 🔧 PyTorch 버전: `2.7.1` (CPU, Apple M1)
- 🤖 Ultralytics 버전: `8.3.163`
- 📦 모델: `YOLO11n-cls`
- 🏗️ 구조: `47 layers`, `1,532,429 parameters`, `3.2 GFLOPs`

---

## 🐍 가상환경 설치 및 패키지

```bash
conda create -n chestct python=3.10
conda activate chestct
pip install ultralytics
```

---

## 🗂️ 클래스 목록 (5 classes)

| 클래스명               | 설명               |
|------------------------|--------------------|
| 🫁 ChestCT_ILD          | 간질성 폐질환       |
| 🧬 ChestCT_Lung_Cancer  | 폐암               |
| ✅ ChestCT_Normal       | 정상               |
| 🌫️ ChestCT_Pneumonia    | 폐렴               |
| 💨 ChestCT_Pneumothorax | 기흉               |

---

## 🧪 모델 훈련 설정

```python
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

> 📌 *의료영상 특성을 고려하여, 데이터 증강을 최소화하고 모자이크를 비활성화했습니다.*

---

## 📸 주요 결과 이미지

### 🔢 Batch Size
<p align="center">
  <img src="https://github.com/user-attachments/assets/64892439-03e3-4c9c-af34-a6f77f905cac" width="800">
</p>

### 📊 Confusion Matrix
<p align="center">
  <img src="https://github.com/user-attachments/assets/72c004d0-01e5-47bf-aa2c-58b4de1c5411" width="800">
</p>

### 📈 학습 결과 그래프
<p align="center">
  <img src="https://github.com/user-attachments/assets/c09f2a73-fdfc-41dc-afbd-de4c06c12b4d" width="800">
</p>

### 🖼️ 테스트 결과 이미지
<p align="center">
  <img src="https://github.com/user-attachments/assets/b98abc11-f5ee-423b-a74c-2f14c009e1cd" width="400">
  <img src="https://github.com/user-attachments/assets/fc389aa8-d61d-498c-be83-1d046e714aab" width="400">
  <img src="https://github.com/user-attachments/assets/c8b3bb14-4ece-469a-9d05-c8c6895e2bf3" width="400">
  <img src="https://github.com/user-attachments/assets/265a9a1f-605d-4b9c-8f0e-f215eeb0e5b6" width="400">
  <img src="https://github.com/user-attachments/assets/3728e4b8-8392-43ee-9308-fa1ef0506136" width="400">
</p>

---

## 📊 성능 평가 결과

| 클래스  | 🎯 Top-1 Accuracy | 🎯 Top-5 Accuracy |
|---------|------------------|------------------|
| 전체     | ✅ **99.67%**      | ✅ **100.00%**     |

- ✅ **Top-1 Accuracy**: 모델이 가장 높은 확률로 예측한 클래스가 실제 정답과 일치하는 비율  
- ✅ **Top-5 Accuracy**: 모델의 예측 상위 5개 중 정답이 포함되는 비율

---

## 🏁 결론

YOLO11n-cls 기반 Chest CT 질환 분류 모델은 검증 데이터셋에서 **우수한 정확도**를 보였습니다.  
실제 의료영상에서의 적용 가능성을 고려할 때, 경량화된 구조와 높은 성능은 실시간 분석에도 적합합니다.

> 💡 **Top-1: 99.67%, Top-5: 100%**

---

## 🖼️ 데이터셋 출처

- 📁 **AIHub - 흉부 CT 영상 기반 폐 질환 진단 이미지**
<p align="center">
  <img src="https://github.com/user-attachments/assets/f9330667-f430-4126-b90d-ea9acdda600b" width="800">
</p>

---
