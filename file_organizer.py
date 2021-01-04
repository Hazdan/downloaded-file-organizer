import os
import shutil
import time


DOWNLOAD_PATH = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')


extension = {
    'video': ['.mov', '.mp4', '.MKV', '.avi', '.mpeg', '.webm'],
    'document': ['.doc', '.docx', '.txt', '.pdf', '.pptx', '.csv', '.epub'],
    'photo': ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'],
    'audio': ['.mp3', '.wav', '.ogg', '.MIDI'],
}


def search_extension(file_extension):
    path = 'other'
    for key, value in extension.items():
        if file_extension in value:
            path = key
    return path


def sort_file(file, path):
    shutil.move(os.path.join(DOWNLOAD_PATH, file), path)


def main():
    for file  in os.listdir(DOWNLOAD_PATH):
        file_name, file_extension = os.path.splitext(file)
        if file_extension != '':
            file_type = search_extension(file_extension)
            path = os.path.join(DOWNLOAD_PATH, file_type)
            sort_file(file, path)


if __name__ == '__main__':
    main()