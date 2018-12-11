import os 

class Config:
	pass

class ProdConfig:
	pass

class DevConfig:
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

