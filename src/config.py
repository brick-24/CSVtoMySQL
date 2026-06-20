import os

from dotenv import load_dotenv

load_dotenv()

# MySQL connection settings loaded from environment variables
# Copy .env.example to .env and fill in your values
host = os.environ.get("MYSQL_HOST", "localhost")
user = os.environ.get("MYSQL_USER", "root")
password = os.environ.get("MYSQL_PASSWORD", "")
