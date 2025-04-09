import os
import polars as pl
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
from models import Base, Ro


load_dotenv()

DATABASE_URL = os.getenv("DEV_DATABASE_URL")

# engine = create_engine(DATABASE_URL)
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATAFRAMES = os.path.join(BASE_DIR, 'data')


class RoAutomationSpreedsheet:
    def __init__(self):
        pass
        
    def extract(self):
        df = pl.read_csv(os.path.join(DATAFRAMES, 'data.csv'), truncate_ragged_lines=True)
        newdf = df[['']]
        print(df.head())
 
if __name__ == "__main__":
    RoAutomationSpreedsheet().extract()