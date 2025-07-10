# 🚀 프로젝트 설명
```
Hugging Face Transformers 기반 감정 분석 모델 영어 문장을 입력받아 'POSITIVE' 또는 'NEGATIVE'로 분류
```

# ⚙️ 환경 및 모델 정보
```
- Python 버전: 3.10.18
- Transformers 버전: 최신
- PyTorch 버전: 최신 (CPU, Apple M1)
- 모델: distilbert-base-uncased-finetuned-sst-2-english (기본값)
```

# 🐍 가상환경 생성
```
conda create -n trans_senti python=3.10
pip install ultralytics
pip install transformers
pip install torch
```

# 🧠 작동 원리
```
pipeline("sentiment-analysis")는 Hugging Face의 사전 학습 모델을 불러와 사용합니다.
문장을 토큰화하고, BERT 기반 모델에 입력하여 감정(긍/부정)을 분류합니다.
결과는 label (감정)과 score (신뢰도 확률)로 구성된 리스트 형태로 반환됩니다.
```

# 🖼️ Result Images
<p align="center">
  <img src="https://github.com/user-attachments/assets/7a528db9-da57-42a8-9183-6d1389dc2181" width="1000">
</p>
