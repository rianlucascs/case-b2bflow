
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd
from logger import get_logger

class Database:
    """Classe para gerenciar a conexão e consultas ao banco de dados."""
    
    def __init__(self):
        
        self.log = get_logger("db")
        
        load_dotenv()
        self.load()
        
        
    def load(self) -> None:
        """Estabelece a conexão com o banco de dados."""
        
        try:
            
            self.engine = create_engine(os.environ["DATABASE_URL"])
            
        except Exception as e:
            
            self.log.error(f"Erro ao conectar ao banco: {e}")
            
            raise
        
        self.log.info("Conexão com o banco estabelecida")

    
    def query(self, query: str) -> pd.DataFrame:
        """Executa uma query SQL e retorna o resultado como DataFrame."""
        
        try:
            
            df = pd.read_sql(query, self.engine)
            
            self.log.debug(f"Query executada com sucesso:{query}")
            
            return df
        
        except Exception as e:
            
            self.log.error(f"Erro ao executar query: {e}")
            
            raise
        
    def select_all(self, limit: int=5) -> pd.DataFrame:
        """Seleciona todos os registros da tabela 'Leads' com um limite."""
        
        try:
            
            query = f'SELECT * FROM "Leads" LIMIT {limit}'
            self.log.debug("Query: %s", query)
            
            df = self.query(query)

            self.log.info(f"Selecionados {len(df)} registros da tabela 'Leads'")
            
            return df
        
        except Exception as e:
            
            self.log.error(f"Erro ao selecionar dados: {e}")
            
            raise    

