import psycopg2


def init():
    # if __name__ == "__main__":
    conn = None
    try:

        conn = psycopg2.connect(
            host="localhost",
            database="airflow",
            user="airflow",
            password="airflow"
        )

        with conn:
            with conn.cursor() as curs:
                curs.execute(
                    open("/usr/local/airflow/dags/init.sql", "r").read())
                curs.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
