from flask import Flask
from decouple import config
from flask_restx import Api
app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
api = Api(
    app,
    version='1.0',
    title='Подборка анекдотов!',
    description='<B>Получаем Анекдоты с сайта Анекдотов!</B>',
    contact='Николаева Кристина',
    contact_url='https://vk.com/twinfield',
    doc='/',
    prefix='/api/v1'
)
from core import routes