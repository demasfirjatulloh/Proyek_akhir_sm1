import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("POSTGRES_USER", "postgres")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
HOST = os.getenv("POSTGRES_SERVER", "localhost")
PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = "smart_canteen_db"

try:
    connection = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT,
        database="postgres"
    )
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()

    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'")
    exists = cursor.fetchone()

    if not exists:
        cursor.execute(f"CREATE DATABASE {DB_NAME}")
        print(f"Sukses! Database '{DB_NAME}' berhasil dibuat.")
    else:
        print(f"Database '{DB_NAME}' sudah ada sebelumnya.")

    cursor.close()
    connection.close()

except Exception as error:
    print(f"Gagal terhubung ke PostgreSQL: {error}")
    print("Tips: Pastikan password di file backend/.env sudah sesuai dengan password PostgreSQL-mu.")