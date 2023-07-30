import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import urlparse
from dotenv import load_dotenv
load_dotenv()

print("Starting script...")

# Define connection parameters
database_url = os.getenv('DATABASE_URL')

if not database_url:
    raise ValueError("Missing 'DATABASE_URL' environment variable")

# Parse database URL
url = urlparse(database_url)

postgres_db = url.path[1:]  # Remove leading slash
postgres_user = url.username
postgres_password = url.password
postgres_host = url.hostname
postgres_port = url.port

print("Creating database engine...")

# Create engine for PostgreSQL
postgres_engine = create_engine(f'postgresql+psycopg2://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}')

print("Database engine created.")

# Check connection
try:
    connection = postgres_engine.connect()
    print("Successfully connected to the database.")
except Exception as e:
    print(f"Failed to connect to the database: {e}")
    exit()

# Define file path
file_path = os.getenv('CSV_FILE_PATH')

if not file_path:
    raise ValueError("Missing 'CSV_FILE_PATH' environment variable")

print("Reading CSV file...")

# Use pandas to read the CSV file
try:
    df = pd.read_csv(file_path, quotechar='"', on_bad_lines='skip')
    print(f"Read {len(df)} rows from the CSV file.")
except Exception as e:
    print(f"Failed to read CSV file: {e}")
    exit()

print("Writing to database...")

# Use pandas to write the dataframe to the PostgreSQL table
try:
    df.to_sql('aitool', postgres_engine, if_exists='replace', index=False)  # Notice 'replace' instead of 'append'
    print(f"Wrote {len(df)} rows to the database.")
except SQLAlchemyError as e:
    print(f"Failed to write to the database: {e}")
    exit()


print("Script completed.")
