import psycopg2
import pandas as pd
import numpy as np


def insert():
    conn = None
    df = pd.read_csv('/usr/local/airflow/dags/new_csv.csv', encoding='utf8')
    try:

        conn = psycopg2.connect(
            host="host.docker.internal",
            database="airflow",
            user="airflow",
            password="airflow"
        )
        tuples = [tuple(x) for x in df.to_numpy()]

        with conn:
            with conn.cursor() as curs:
                for row in tuples:
                    curs.execute(
                        "INSERT INTO benoit_test.table_med (id_spe, name_spe, rem_mean, rem_taux) VALUES(%s, %s, %s,%s) ON CONFLICT DO NOTHING",
                        (row[1], row[0], row[2], row[3]))
                curs.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
