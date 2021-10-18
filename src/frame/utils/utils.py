import subprocess
from fastapi import UploadFile
from uuid import uuid4
import shutil
from base64 import b64encode


def check_or_create_directory(name: str = 'data', path: str = '*') -> None:
    if name + '/' not in subprocess.getoutput(f'ls -d {path}/'):
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
