# 🚀 프로젝트 설명
```
학생 데이터셋을 활용한 GPA 예측 신경망 모델로, MinMaxScaler를 적용하여 정규화한 학습
```

# ⚙️ 환경 및 모델 정보
```
- Python 버전: 3.10
- TensorFlow 버전: 2.x
- Scikit-learn 버전: 1.x
- GPU/CPU: CPU 또는 GPU 환경 모두 사용 가능
- 모델: 완전 연결 신경망(Sequential)
```

# 🐍 가상환경 생성
```
conda create -n regression python=3.10
pip install tensorflow scikit-learn pandas matplotlib seaborn
```

# 📁 Kaggle

[](Students performance analysis and GPA prediction)

# 📊 EDA
<p align="center">
  <img src="https://github.com/user-attachments/assets/5c82bece-29af-420c-b804-48b5f941e8df" width="700">
  <img src="https://github.com/user-attachments/assets/de30a392-6a39-4087-bf05-887237db48d6" width="700">
  <img src="https://github.com/user-attachments/assets/de30a392-6a39-4087-bf05-887237db48d6" width="700">
  <img src="https://github.com/user-attachments/assets/cf96fb63-279b-4cc5-9374-751843db6583" width="700">
  <img src="https://github.com/user-attachments/assets/ebfb88b3-968c-4756-bbc9-f8d8456e3fdd" width="700">
  <img src="https://github.com/user-attachments/assets/8a2d24b4-9cd4-4ed2-9c22-b60c9e34cd3a" width="700">
  <img src="https://github.com/user-attachments/assets/38150ab1-682b-42e6-ad5a-e764fdaf1b23" width="700">
  <img src="https://github.com/user-attachments/assets/10e407a0-c63c-4cd6-89f3-de28566369e6" width="700">
  <img src="https://github.com/user-attachments/assets/466167a5-7fc1-4846-9270-73192f29bd1d" width="700">
  <img src="https://github.com/user-attachments/assets/a4eb3a4d-5014-4362-985a-154a4a2dc6b7" width="700">
  <img src="https://github.com/user-attachments/assets/a4db2523-baac-4708-867b-4b9bdf71acd8" width="700">
  <img src="https://github.com/user-attachments/assets/b0570a43-b08e-4e86-935f-40713c72563c" width="700">
</p>

---

## 📊 성능 평가 결과
기존
```
Total deviation: 4.39344392454638
Average deviation: 0.29289626163642535
```

MinMaxScaler 적용
```
Total deviation: 1.9896162748336792
Average deviation: 0.13264109194278717
```

---

## 🎉 결론

MinMaxScaler 적용 및 신경망 모델을 통해 학생 GPA 예측 가능함  
조기 종료와 배치 학습 등 안정적 학습 적용  
향후 변수 추가 및 모델 튜닝을 통한 성능 향상 기대

---
