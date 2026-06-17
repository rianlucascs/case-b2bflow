
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd


class Database:

    
    def __init__(self):
        load_dotenv()
        self.load()

        
    def load(self):
        self.engine = create_engine(os.environ["DATABASE_URL"])

    
    def query(self, query):
        return pd.read_sql(query, self.engine)

        
    def select_all(self, limit=5):
        query = f'SELECT * FROM "Leads" LIMIT {limit}'
        return self.query(query)
        

