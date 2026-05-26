
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')

# Load environment variables from .env file
load_dotenv(env_path)

class MySQLConfig:
    HOST = os.getenv('host')
    PORT = os.getenv('port')
    USER = os.getenv('mysql_user')
    PASSWORD = os.getenv('mysql_password')
    DATABASE = os.getenv('database')
    @staticmethod
    def get_connection_string():
        
        return f"mysql+pymysql://{MySQLConfig.USER}:{MySQLConfig.PASSWORD}@{MySQLConfig.HOST}:{MySQLConfig.PORT}/{MySQLConfig.DATABASE}"
       
#global base class for mysql connection
base = declarative_base()

engine=create_engine(
            MySQLConfig.get_connection_string(),
            pool_size=10,
            max_overflow=20,
            pool_timeout=30,
            pool_recycle=1800,
            pool_pre_ping=True)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
