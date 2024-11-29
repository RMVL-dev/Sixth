import os
import time

directory = "."

for root, dirs, files in os.walk(directory):
    for file in files:
        if not file.isalpha():
            try:
                filePath = f"./{os.path.join(file)}"
                fileTime = os.path.getmtime(file)
                formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(fileTime))
                fileSize = f"{os.path.getsize(file)} байт"
                parentDir = os.path.dirname(file)
                print()
                print(f"Обнаружен файл: {file}, Путь: {filePath}, Размер: {fileSize}, Время изменения: {formatted_time}, Родительская директория: {parentDir}")
            except FileNotFoundError:
                pass
