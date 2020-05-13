import psycopg2

connection = psycopg2.connect(user = "ehguposgnxoqgt",
                            password = "4ae2a7ab4f8c57aef3a1141e4969c89586bf2c34bf4e26eb1b57032299f9da04",
                            host = "ec2-3-222-30-53.compute-1.amazonaws.com",
                            port = "5432",
                            database = "dd6ron4p756nq6")
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