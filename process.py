import subprocess
import os

files = os.listdir("videos")
for file in files:
    file_name = file.split(" ｜ ")[0]
    file_number = file.split(" [")[0].split("#")[1]
    print(f"Converting {file_number}_{file_name}")
    print(file)
    #subprocess.run(["ffmpeg", "-i", f"F:/RAG-SEARCH-ENGINE/videos/{file}", f"{file_number}_{file_name}.mp3"])
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", "-vn", f"{file_number}_{file_name}.mp3"])
