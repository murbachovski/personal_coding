# 테스트 데이터셋 검증 중 오답 클래스는 폴더 생성하여 저장

import os
from ultralytics import YOLO
from pathlib import Path
from PIL import Image
from tqdm import tqdm

# 모델 로드
model = YOLO("yolo_chest_x_ray/yolo_chest_x_ray_m.pt")
# print(model.names)
# {0: 'abnormal', 1: 'normal'}

# 이미지 루트
image_dir = Path("yolo_chest_x_ray/datasets/test/normal")

# 잘못 예측된 이미지 저장할 디렉토리
# wrong_dir = Path("yolo_chest_x_ray/abnormal_misclassified")
wrong_dir = Path("yolo_chest_x_ray/normal_misclassified")
wrong_dir.mkdir(exist_ok=True)

# 전체 이미지 수집
image_paths = [p for ext in ('*.jpg', '*.jpeg', '*.png') for p in image_dir.rglob(ext)]

# 오답 이미지 기록
misclassified = []

for img_path in tqdm(image_paths):
    # 실제 클래스: 상위 폴더 이름
    gt_class = img_path.parent.name

    # 예측
    result = model.predict(str(img_path), imgsz=256, device="mps", conf=0.5, verbose=False)[0]
    pred_class = model.names[int(result.probs.top1)]

    if pred_class != gt_class:
        # 오답인 경우 저장
        misclassified.append((img_path, gt_class, pred_class))

        # 원본 이미지 복사
        dst_path = wrong_dir / f"{img_path.stem}_pred-{pred_class}_gt-{gt_class}.png"
        Image.open(img_path).save(dst_path)

# 오답 목록 출력
for img_path, gt, pred in misclassified:
    print(f"❌ {img_path.name} | GT: {gt} | Pred: {pred}")
print(f"\n총 잘못 예측한 이미지 수: {len(misclassified)}개")

# wrong_dir = Path("yolo_chest_x_ray/abnormal_misclassified")
# 총 잘못 예측한 이미지 수: 164개

# wrong_dir = Path("yolo_chest_x_ray/normal_misclassified")
# 총 잘못 예측한 이미지 수: 51개