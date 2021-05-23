import psycopg2

with psycopg2.connect(host='localhost', port=54320, dbname='database_a', user='postgres', password='postgres') as conn, conn.cursor() as cursor:
    query = """
    SELECT DISTINCT table_name FROM information_schema."columns" c WHERE table_schema = 'public'
    """
    cursor.execute(query)
    for row in cursor:
        print(row[0])