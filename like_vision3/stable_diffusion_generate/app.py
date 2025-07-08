# 가상환경 생성
    # conda create -n hugg python=3.10
# pip install huggingface-hub
# Pip install pillow
import os
from huggingface_hub import InferenceClient
import time

# ⏱️ 시작 시간 기록
start_time = time.time()

print("코드 시작")

# 🔑 Hugging Face API 토큰 환경변수에서 불러오기
# os.environ["HF_TOKEN"]에 사전에 토큰을 설정해야 합니다.

# 🌐 InferenceClient 객체 생성 (Hugging Face Hub)
client = InferenceClient(
    provider="auto",
    api_key=os.environ["HF_TOKEN"],  # 환경변수 HF_TOKEN에 API 키 저장 필요
)

# 💬 사용자로부터 이미지 생성에 사용할 텍스트 입력받기
prompt = input("생성할 이미지를 설명해주세요. : ")

print(f"🖼️ 이미지 생성 중... (프롬프트: {prompt})")

# 🤖 입력 텍스트를 바탕으로 이미지 생성 요청
image = client.text_to_image(
    prompt,               # 생성할 이미지에 대한 설명 텍스트
    model="black-forest-labs/FLUX.1-dev",  # 사용할 모델 지정
)

# 💾 생성된 이미지를 파일로 저장
save_path = "result_image.png"
image.save(save_path)

print(f"📁 이미지 저장 완료: {save_path}")

# 🖼️ iTerm2 터미널에서 이미지 출력 (imgcat 명령어 실행)
os.system(f"imgcat {save_path}")

# ⏳ 총 실행 시간 출력
elapsed_time = time.time() - start_time
print(f"⏰ 전체 실행 시간: {elapsed_time:.2f}초")

print("✅ 전체 코드가 잘 실행되었음!")
