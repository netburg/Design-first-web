import os

#dialect+driver://username:password@host:port/database
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '645018@hzzj'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE ='demo'
SQLALCHEMY_DATABASE_URI ='{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = True

DEBUG = True

SECRET_KEY = os.urandom(24)

# DB_CONNECTION = mysql
# DB_HOST = 121.196.202.34
# DB_PORT = 3306
# DB_DATABASE = saturn - dev01
# DB_USERNAME = zhizao
# DB_PASSWORD = zhizao16888