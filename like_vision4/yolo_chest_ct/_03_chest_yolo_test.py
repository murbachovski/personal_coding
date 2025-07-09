import os

def count_files_in_folder(folder_path):
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        print(f"'{folder_path}' 폴더 내 파일 개수: {len(files)}개")
    except Exception as e:
        print(f"오류 발생: {e}")

# 예시 사용
count_files_in_folder("datasets/test/ChestCT_ILD")
count_files_in_folder("runs/classify/ChestCT_ILD")
# 'datasets/test/ChestCT_ILD' 폴더 내 파일 개수: 27개
# 'runs/classify/ChestCT_ILD' 폴더 내 파일 개수: 26개

count_files_in_folder("datasets/test/ChestCT_Lung_Cancer")
count_files_in_folder("runs/classify/ChestCT_Lung_Cancer")
# 'datasets/test/ChestCT_Lung_Cancer' 폴더 내 파일 개수: 27개
# 'runs/classify/ChestCT_Lung_Cancer' 폴더 내 파일 개수: 26개

count_files_in_folder("datasets/test/ChestCT_Normal")
count_files_in_folder("runs/classify/ChestCT_Normal")
# 'datasets/test/ChestCT_Normal' 폴더 내 파일 개수: 22개
# 'runs/classify/ChestCT_Normal' 폴더 내 파일 개수: 21개

count_files_in_folder("datasets/test/ChestCT_Pneumonia")
count_files_in_folder("runs/classify/ChestCT_Pneumonia")
# 'datasets/test/ChestCT_Pneumonia' 폴더 내 파일 개수: 27개
# 'runs/classify/ChestCT_Pneumonia' 폴더 내 파일 개수: 26개

count_files_in_folder("datasets/test/ChestCT_Pneumothorax")
count_files_in_folder("runs/classify/ChestCT_Pneumothorax")
# 'datasets/test/ChestCT_Pneumothorax' 폴더 내 파일 개수: 27개
# 'runs/classify/ChestCT_Pneumothorax' 폴더 내 파일 개수: 26개