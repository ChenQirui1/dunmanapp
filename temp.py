import psycopg2

connection = psycopg2.connect(user = "postgres",
                        password = "gby021229",
                        host = "127.0.0.1",
                        port = "5432",
                        database = "dunmanapp")
cursor = connection.cursor()
q = """
    CREATE TABLE users (
        id TEXT PRIMARY KEY,
        classid TEXT NOT NULL,
        name TEXT,
        email TEXT UNIQUE NOT NULL,
        profile_pic TEXT NOT NULL,
        admin INTEGER NOT NULL
    )
    """
cursor.execute(q)
connection.commit()
cursor.close()
connection.close()