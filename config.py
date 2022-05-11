import os
import contentful

DATABASE_URL = os.getenv('DATABASE_URL')

client = contentful.Client('cfexampleapi', 'b4c0n73n7fu1', api_url='preview.contentful.com')

class Config:
  SQLALCHEMY_ECHO = False
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_DATABASE_URI = DATABASE_URL
  if 'ON_HEROKU' in os.environ:
    SQLALCHEMY_DATABASE_URI = DATABASE_URL.replace("://", "ql://", 1)