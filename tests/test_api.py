from fastapi.testclient import TestClient
from main import app
from src.core.database import SessionLocal
from src.frame.models.inbox import Inbox
from src.frame.utils.utils import decode_image
from datetime import datetime
import subprocess

from dateutil import parser

client = TestClient(app)
session = SessionLocal()


def test_put_images_view():
    # Case #1: image saved, 201
    response = client.put(
        'api/frame',
        files={'images': ('filename', open('tests/files/180px-Python-logo.jpg', 'rb'), 'image/jpg')}
    )
    assert response.status_code == 201
    response_data = response.json()[0]
    inbox = session.query(Inbox).get(response_data['id'])
    now = inbox.created_at.strftime('%Y%m%d')
    assert response_data['code'] == inbox.code
    assert response_data['filename'] == inbox.filename
    assert parser.parse(response_data['created_at']) == inbox.created_at
    assert response_data['filename'] in subprocess.getoutput(f'ls data/{now}').split('\n')
    # Case #2: without file, 422
    response = client.put('api/frame')
    assert response.status_code == 422
    # Case #3: files more than 15
    # Can't understand how to send list of files
    """response = client.post(
        'api/frame',
        headers={'Content-Type': 'multipart/form-data'},
        files={'iamge_1': ('filename', open('../files/180px-Python-logo.jpg', 'rb'), 'image/jpg'),
               'iamge_2': ('filename', open('../files/180px-Python-logo.jpg', 'rb'), 'image/jpg')}
    )
    assert response.status_code == 400"""


def test_get_images_by_code_view():
    # Case #1: found object, 200
    obj = session.query(Inbox).all()[-1]
    response = client.get(f'api/frame/{obj.code}')
    response_data = response.json()[0]
    now = obj.created_at.strftime('%Y%m%d')
    assert response.status_code == 200
    assert response_data['id'] == obj.id
    assert response_data['code'] == obj.code
    assert response_data['filename'] == obj.filename
    assert parser.parse(response_data['created_at']) == obj.created_at
    assert response_data['file'] == decode_image(f'data/{now}/{obj.filename}')
    # Case #2: not found, 404
    response = client.get(f'api/frame/frfrhfie93e9d8furf3f934f')
    assert response.status_code == 404


def test_delete_images_by_code_view():
    # Case #1: delete objects, 204
    obj = session.query(Inbox).all()[-1]
    now = obj.created_at.strftime('%Y%m%d')
    response = client.delete(f'api/frame/{obj.code}')
    assert response.status_code == 204
    assert response.text == f'All images with code {obj.code} had been successefully deleted.'
    assert obj.filename not in subprocess.getoutput(f'ls data/{now}').split('\n')
    # Case #2: not found, 404
    response = client.delete(f'api/frame/frfrhfie93e9d8furf3f934f')
    assert response.status_code == 404



