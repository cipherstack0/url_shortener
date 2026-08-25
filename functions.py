import mysql.connector
import os
# Base62 characters
BASE62 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def get_connection(database=None):
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST","localhost"),         #where your database lives (for now, your own PC)
        user=os.getenv("MYSQL_USER", "root"),              #your MySQL username
        password = os.getenv("MYSQL_PASSWORD"),  # password in env
        database=database
    )
    
def start_db():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS short_url_db")

    cursor.execute("USE short_url_db")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INT AUTO_INCREMENT PRIMARY KEY,
            short_code VARCHAR(20) UNIQUE,
            long_url TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()
    

BASE_URL = "http://localhost:5000/"


# Encode long URL to short URL
def encode(long_url, database="short_url_db"):
    # Store mapping
    if not long_url.startswith(("http://", "https://")):
        long_url = "https://" + long_url
    connection = get_connection(database)
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO urls (long_url) VALUES (%s)",
        (long_url,)
    )
    connection.commit()
    new_id = cursor.lastrowid
    # Generate short key using Base62
    short_key = convert_to_base62(new_id)
    
    cursor.execute(
        "UPDATE urls SET short_code = %s WHERE id = %s",
        (short_key, new_id)
    )

    connection.commit()
    connection.close()

    return BASE_URL + short_key


# Decode short URL to original long URL
def decode(short_url):
    short_key = short_url.replace(BASE_URL, "", 1)
    connection = get_connection("short_url_db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT long_url FROM urls WHERE short_code = %s",
        (short_key,)
    )

    result = cursor.fetchone()
    
    connection.close()
    if result:
        return result[0]
    
    return "URL not found"


# Convert number to Base62
def convert_to_base62(num):
    result = []

    while num > 0:
        remainder = num % 62
        result.append(BASE62[remainder])
        num //= 62

    return "".join(reversed(result))

# redirect to page
def redirect_url(url_encoded):
    connection = get_connection("short_url_db")
    cursor = connection.cursor()
    cursor.execute(
        "select long_url from urls where short_code = %s",
        (url_encoded,)
    )
    result = cursor.fetchone()
    print(result)
    
    if result:
        connection.close()
        return result[0]
    connection.close()
    
    return None
     

