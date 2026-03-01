import os
import psycopg2

def get_connection():
    return psycopg2.connect(
        host=os.environ.get("ep-fancy-cake-a107xc6m-pooler.ap-southeast-1.aws.neon.tech"),
        database=os.environ.get("neondb"),
        user=os.environ.get("neondb_owner"),
        password=os.environ.get("npg_sLgMKp6uHbP3"),
        port=os.environ.get("5432")
    )