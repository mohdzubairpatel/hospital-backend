import os
import psycopg2

def get_connection():
    return psycopg2.connect(
        os.environ.get("postgresql://neondb_owner:npg_sLgMKp6uHbP3@ep-fancy-cake-a107xc6m-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require")
    )