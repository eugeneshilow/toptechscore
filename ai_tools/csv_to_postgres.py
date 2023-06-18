import pandas as pd
from sqlalchemy import create_engine

# Define connection parameters
postgres_db = 'postgres1'
postgres_user = 'user1'
postgres_password = 'k%<]5N?7,h`JEC;I'
postgres_host = 'localhost'  # This connects to your local Postgres instance
postgres_port = '5432'

# Create engine for PostgreSQL
engine = create_engine(f'postgresql+psycopg2://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}')

# Define CSV file path
csv_file_path = '/Users/eugeneshilov/Dropbox/1. Business/TopTechScore/toptechscore-root/ai_tools/csv_files/AI Tools Database - Database - csv export.csv'

# Use pandas to read the CSV file
df = pd.read_csv(csv_file_path)

# Use pandas to write the dataframe to the PostgreSQL table
df.to_sql('aitool', engine, if_exists='append', index=False)

