import pandas as pd
import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# 1)

script_dir = os.path.dirname(os.path.abspath(__file__))
dataPathCustomer = os.path.join(script_dir,'../dati/customer.csv')
dataPathProduct = os.path.join(script_dir,'../dati/product.csv')
dataPathTransaction = os.path.join(script_dir,'../dati/transaction.csv')

df_customer = pd.read_csv(dataPathCustomer)
df_product = pd.read_csv(dataPathProduct)
df_transaction = pd.read_csv(dataPathTransaction)

df_customer.rename(columns={'Col1':'CustomerID'})
df_customer.rename(columns={'Col2':'Country'})

df_product.rename(columns={'Col1':'StockCode'})
df_product.rename(columns={'Col2':'Description'})

#---------------------------------------------------#
# 2)

df_merge = pd.merge(df_customer, df_transaction, on='CustomerID')

def store_on_database(self, df: pd.DataFrame) -> None:  
    table_name = "Clienti_transazioni"
    engine = create_engine(self.config.db_uri)
    try:
        with engine.begin() as conn:  
            df.to_sql(table_name, con=conn, if_exists='replace', index=False)
    except SQLAlchemyError as e:
        print(f"Error di scrittura in database: {e}")
    finally:
        engine.dispose()

### LEGGI DATI DA PostgreSQL DB ###
SIMPLE_QUERY_1 = """
SELECT *
FROM CustomerID
"""
engine = create_engine('postgresql+psycopg://postgres:postgres@postgresql:5432/Clienti_transazioni')
print(SIMPLE_QUERY_1)

# # Leggi i dati da PostgreSQL ad un DataFrame
df_from_db = pd.read_sql_query(text(SIMPLE_QUERY_1), con=engine.connect())
print(df_from_db)

#----------------------------------------------------#
# 3)
df_merge.replace()
df_merge.replace()
df_merge.dropna()





