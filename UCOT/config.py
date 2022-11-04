class Config:
    SECRET_KEY = 'Develoteca'


class DevelopmentConfig():
    DEBUG = True
    MYSQL_DATABASE_HOST='localhost'
    MYSQL_DATABASE_USER='root'
    MYSQL_DATABASE_PASSWORD=''
    MYSQL_DATABASE_DB='ucot'


config = {
    'development' : DevelopmentConfig
}