import psycopg

def connect_database():
    try:
        db_connection = psycopg.connect("dbname=tapu_db user=postgres host=localhost password=15246868")
        cur = db_connection.cursor()
        cur.execute("""SELECT * FROM sales""")
        query_result = cur.fetchone()
        print(query_result)
        # print(type(query_result))
        cur.close()
    except:
        print("Cannot execute query!")
    finally:
        if db_connection is not None:
            db_connection.close()
            print("Connection closed!")


if __name__ == "__main__":
    try:
        connect_database()
    except:
        pass