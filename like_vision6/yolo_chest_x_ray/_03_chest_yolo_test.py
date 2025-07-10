import os

def count_files_in_folder(folder_path):
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        print(f"'{folder_path}' 폴더 내 파일 개수: {len(files)}개")
    except Exception as e:
        print(f"오류 발생: {e}")

# 학습 데이터 개수 확인
count_files_in_folder("yolo_brain_mri/datasets/train/abnormal")
count_files_in_folder("yolo_brain_mri/datasets/train/normal")
# 'yolo_brain_mri/datasets/train/abnormal' 폴더 내 파일 개수: 4000개
# 'yolo_brain_mri/datasets/train/normal' 폴더 내 파일 개수: 4000개

# 검증 데이터 개수 확인
count_files_in_folder("yolo_brain_mri/datasets/val/abnormal")
count_files_in_folder("yolo_brain_mri/datasets/val/normal")
# 'yolo_brain_mri/datasets/val/abnormal' 폴더 내 파일 개수: 500개
# 'yolo_brain_mri/datasets/val/normal' 폴더 내 파일 개수: 500개