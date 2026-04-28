import os
import shutil

folder = r"D:\대학교 과제\인공지능 기초\인공지능(main)"


def organize_files(folder):
    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if not os.path.isfile(path):
            continue

        ext = file.split('.')[-1].lower()

        if ext in ['jpg', 'png']:
            target_folder = "images"
        elif ext in ['docx', 'xlsx']:
            target_folder = "docs"
        elif ext in ['mp4']:
            target_folder = "videos"
        elif ext in ['mp3']:
            target_folder = "music"
        elif ext == "py":
            target_folder = "python"
        else:
            target_folder = "others"

        target_path = os.path.join(folder, target_folder)
        os.makedirs(target_path, exist_ok=True)

        shutil.move(path, os.path.join(target_path, file))

def change_extension(folder, old_ext, new_ext):
    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if file.endswith(old_ext) and os.path.isfile(path):
            new_name = file.replace(old_ext, new_ext)
            os.rename(path, os.path.join(folder, new_name))

def explain_files(folder):
    seen = set() 
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file in seen:
                continue

            seen.add(file)

            ext = file.split('.')[-1].lower()

            if ext in ['jpg', 'png']:
                print(f"{file} → 이미지 파일")
            elif ext in ['docx', 'xlsx']:
                print(f"{file} → 문서 파일")
            elif ext in ['mp4']:
                print(f"{file} → 영상 파일")
            elif ext in ['mp3']:
                print(f"{file} → 음악 파일")
            elif ext == 'py':
                print(f"{file} → 파이썬 파일")
            else:
                print(f"{file} → 기타 파일")

print("파일 정리 시작")
organize_files(folder)

print("확장자 변경 시작")
change_extension(folder, ".txt", ".md")

print("파일 설명 출력")
explain_files(folder)

print("작업 완료! 프로그램을 종료하겠습니다")