import os
import shutil
import time


DOWNLOAD_PATH = "C:\\Users\\Hazdan\\Downloads\\"

extension = {
    'video': ['.mov', '.mp4'],
    'document': ['.doc', '.docx', '.txt', '.pdf', '.pptx', '.csv', '.epub'],
    'photo': ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.PNG'],
    'audio': ['.mp3'],
}


def search_extension(file_extension):
    path = 'other'
    for key, value in extension.items():
        if file_extension in value:
            path = key
    return path


def sort_file(file, path):
    shutil.move(DOWNLOAD_PATH + file, path)


def main():
    for file  in os.listdir(DOWNLOAD_PATH):
        file_name, file_extension = os.path.splitext(file)
        if file_extension != '':
            file_type = search_extension(file_extension)
            path = DOWNLOAD_PATH + file_type
            sort_file(file, path)


if __name__ == '__main__':
    main()