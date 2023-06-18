import os
import pandas as pd
from sqlalchemy import create_engine
import gcsfs

print("Starting script...")

# Define connection parameters
postgres_db = os.getenv('DB_NAME', 'postgres1')
postgres_user = os.getenv('DB_USER', 'user1')
postgres_password = os.getenv('DB_PASSWORD', 'mqy%Z9~7-Y<fsJVn')
postgres_host = '35.184.196.3'  # Public IP address of your Cloud SQL instance
postgres_port = '5432'

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

# Define GCS file path
gcs_file_path = 'gs://bucket-toptechscore/AI Tools Database - Database - csv export.csv'

print("Creating GCS file system...")

# Create a gcsfs object
fs = gcsfs.GCSFileSystem(project='toptechscore')

print("GCS file system created.")
print("Reading CSV file...")

# Use pandas to read the CSV file from GCS
with fs.open(gcs_file_path) as f:
    df = pd.read_csv(f)

print("Writing to database...")

# Use pandas to write the dataframe to the PostgreSQL table
df.to_sql('aitool', postgres_engine, if_exists='append', index=False)

print("Script completed.")