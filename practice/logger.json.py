import json
import logging

with open("logger.json","rt")as file:
    config = json.load(file)

logging.config.dictConfig(config) # dictConfig로 json파일의 setting을 받음
logger = logging.getLogger()