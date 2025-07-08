# 가상환경: conda create -n diff python=3.9
# 설치: pip install diffusers transformers accelerate imgcat

from diffusers import StableDiffusionPipeline
import os
import time

# ⏱️ 시작 시간 기록
start_time = time.time()

print("✅ 코드 시작")

# 🔄 Stable Diffusion 모델 로드
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

# 🧠 CPU 사용 (macOS에서는 기본)
pipe = pipe.to("cpu")

# 🎨 이미지 생성할 프롬프트 입력
prompt = input("생성할 이미지를 입력해주세요 : ")
print(f"🖼️ 이미지 생성 중... (프롬프트: {prompt})")

# 🧾 이미지 생성
image = pipe(prompt).images[0]

# 💾 이미지 저장 경로 지정
save_path = os.path.abspath("tti2_image.png")
image.save(save_path)

print(f"📁 이미지 저장 완료: {save_path}")

# 🖼️ iTerm2에서 이미지 출력 (imgcat 명령어 실행)
os.system(f"imgcat {save_path}")

# ⏱️ 실행 시간 출력
elapsed_time = time.time() - start_time
print(f"⏳ 전체 실행 시간: {elapsed_time:.2f}초")

print("🏁 실행 완료")
