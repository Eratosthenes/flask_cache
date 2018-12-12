import os 

class Config:
	pass

class ProdConfig:
	pass

class DevConfig:
	DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
		user=os.environ['POSTGRES_USER'],
		pw=os.environ['POSTGRES_PW'],
		url=os.environ['POSTGRES_URL'],
		db=os.environ['POSTGRES_DB'])

	DEBUG = True
	SQLALCHEMY_DATABASE_URI = DB_URL
	SQLALCHEMY_TRACK_MODIFICATIONS = False


