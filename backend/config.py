from pathlib import Path

BASE_DIR = Path(__file__).parent.absolute()
print(BASE_DIR)
class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:2001513SamuelWu11@127.0.0.1:3306/ihproject"
    SQLALCHEMY_TRACK_MODIFICATIONS = False