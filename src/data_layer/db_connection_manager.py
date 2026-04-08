import os 
import mysql.connector

from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv(override=True)


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        user=os.getenv("USER"),
        password=os.getenv("PASS"),
        database=os.getenv("DB"),
        autocommit=True
    )

def select_messages() -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT * FROM demo_table"
        cursor.execute(sql)
        for row in cursor:
            print(row)

def get_message_by_id(id: int) -> str:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM demo_table WHERE id = %s", [id])
        return cursor.fetchone()

def create_message(message: str) -> None:
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO demo_table (message) VALUES (%(message)s)", {"message": message})
        conn.commit()