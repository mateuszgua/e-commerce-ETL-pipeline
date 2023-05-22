import os
from dotenv import load_dotenv
from os import path

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:

    def load_env_variables():
        AWS_KEY_ID = os.getenv('AWS_KEY_ID')
        AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
        AWS_REGION_NAME = os.getenv('AWS_REGION_NAME')
        AWS_BUCKET = os.getenv('AWS_BUCKET')