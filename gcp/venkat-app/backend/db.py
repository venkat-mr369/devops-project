import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",   # Cloud SQL Proxy
    database="vapp_db",
    user="vapp_user",
    password="Venkat@369",
    port=5432
)