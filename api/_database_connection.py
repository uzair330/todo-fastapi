from dotenv import load_dotenv, find_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv(find_dotenv())
DATABASE_URL = os.getenv("DATABASE_URL")


database_url = os.getenv("DATABASE_URL")
if database_url is None:
    print("DATABASE_URL not set")
else:
    engine = create_engine(DATABASE_URL, echo=True)


Session = sessionmaker(bind=engine)
