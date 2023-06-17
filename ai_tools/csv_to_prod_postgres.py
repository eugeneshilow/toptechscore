import os
import pandas as pd
from sqlalchemy import create_engine

# Define connection parameters
postgres_db = os.getenv('DB_NAME', 'postgres1')
postgres_user = os.getenv('DB_USER', 'user1')
postgres_password = os.getenv('DB_PASSWORD', 'mqy%Z9~7-Y<fsJVn')
postgres_host = '/cloudsql/toptechscore:us-central1:toptechscore-database'
postgres_port = '5432'

# Create engine for PostgreSQL
postgres_engine = create_engine(f'postgresql+psycopg2://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}')

# Define CSV file path
csv_file_path = '/Users/eugeneshilov/Dropbox/1. Business/TopTechScore/toptechscore-root/ai_tools/csv_files/AI Tools Database - Database - csv export.csv'

# Use pandas to read the CSV file
df = pd.read_csv(csv_file_path)

# Use pandas to write the dataframe to the PostgreSQL table
df.to_sql('aitool', postgres_engine, if_exists='append', index=False)
