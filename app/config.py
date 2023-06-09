import os
from dotenv import load_dotenv
from os import path

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:

    AWS_KEY_ID = os.getenv('AWS_KEY_ID')
    AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
    AWS_REGION_NAME = os.getenv('AWS_REGION_NAME')
    AWS_BUCKET = os.getenv('AWS_BUCKET')

    FILE_PATH_TEST = 'data/source/test.parquet'
    FILE_PATH_TRAIN = 'data/source/train.parquet'
    FILE_PATH_VAL = 'data/source/val.parquet'

