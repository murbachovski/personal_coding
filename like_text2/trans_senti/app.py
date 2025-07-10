# 가상환경 생성 (터미널에서 실행)
    # conda create -n trans_senti python=3.10
    # pip install transformers    # Hugging Face의 Transformers 라이브러리 설치
    # pip install torch           # PyTorch 설치 (Transformers 백엔드)

from transformers import pipeline  # 고수준 감정 분석 파이프라인 사용
from termcolor import colored      # 터미널 출력에 색상 입히기

# 1. 감정 분석 파이프라인 생성
classifier = pipeline("sentiment-analysis")
# => 사전 학습된 감정 분석 모델 로드됨 (기본적으로 영어 문장만 지원)
# => 문장을 'POSITIVE' 또는 'NEGATIVE'로 분류함

# 2. 분석할 문장 리스트 작성
texts = ["I love you", "I kill you"]
# => 긍정과 부정을 나타내는 예제 문장

# 3. 여러 문장에 대한 감정 분석 실행
results = classifier(texts)
# => 입력한 각 문장에 대해 감정 분석 결과를 리스트 형태로 반환
# => 각 결과는 {'label': 'POSITIVE' or 'NEGATIVE', 'score': 확률값} 형태의 딕셔너리

# 4. 각 문장에 대해 결과 출력 (색상 포함)
for text, result in zip(texts, results):
    colored_text = colored(text, "black")  # 입력 문장은 검정색으로
    colored_label = colored(result['label'], "blue" if result['label'] == "POSITIVE" else "red")  # 긍정: 파랑, 부정: 빨강
    colored_score = colored(str(round(result['score'], 3)), "yellow")  # 신뢰도 점수는 노랑으로

    # 감정 분석 결과 출력
    print(f"Input : {colored_text} => label: {colored_label}, with score: {colored_score}\n")


# Input : I love you => label: POSITIVE, with score: 1.0

# Input : I kill you => label: NEGATIVE, with score: 0.998