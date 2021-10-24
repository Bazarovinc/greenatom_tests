import shutil
import subprocess
from base64 import b64encode

from fastapi import UploadFile


def check_or_create_directory(name: str = 'data', path: str = '*') -> None:
    if name + '/' not in subprocess.getoutput(f'ls -d {path}/').split('\n'):
        if path == '*':
            subprocess.run(['mkdir', name])
        else:
            subprocess.run(['mkdir', path + '/' + name])


def save_image(filename: str, image: UploadFile) -> None:
    with open(filename, 'wb') as buffer:
        shutil.copyfileobj(image.file, buffer)


def decode_image(filename: str) -> str:
    with open(filename, 'rb') as buffer:
        byte_content = buffer.read()
    base64_bytes = b64encode(byte_content)
    return base64_bytes.decode('utf-8')


def delete_image(filename: str):
    subprocess.run(['rm', filename])
