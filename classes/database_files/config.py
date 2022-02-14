'''Configuration file for database connection. All Environment variables are assigned a ternary operator dependent upon the state of the DEBUG environment variable. Deployment requires that .env variables be assigned as lists where item(0) is default and item(1) is the value to be used in the deployed implementation.
'''

# Imports
import os
import environ
from dotenv import load_dotenv
load_dotenv()


DB_HOST = os.environ.get('DB_HOST')[0] if os.environ.get('DEBUG') == True else os.environ.get('DB_HOST')[1]

DB_NAME = os.environ.get('DB_NAME') if os.environ.get('DEBUG') == True else os.environ.get('DB_NAME')[1]
DB_USER = os.environ.get('DB_USER') if os.environ.get('DEBUG') == True else os.environ.get('DB_USER')[1]
DB_PASS = os.environ.get('DB_PASSWORD') if os.environ.get('DEBUG') == True else os.environ.get('DB_PASSWORD')[1]
DB_PORT = os.environ.get('DB_PORT') if os.environ.get('DEBUG') == True else os.environ.get('DB_PORT')[1]