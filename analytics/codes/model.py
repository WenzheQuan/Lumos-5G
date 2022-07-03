import time
import psycopg2
from psycopg2 import Error

for i in range(1):
    print('Welcome to Python')

    # Connect to an existing database
    #note, embedding credentials is bad practice but for the purpo
    connection = psycopg2.connect(user="druid",
                                password="FoolishPassword",
                                host="postgres",
                                port="5432",
                                database="druid")
    connection.autocommit = True

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")
    command = """
            CREATE TABLE STUDENT IF NOT EXISTS 
      (ADMISSION INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      COURSE        CHAR(50),
      DEPARTMENT        CHAR(50));
            """
    # cursor.execute(command)
    # connection.commit()

    command = "SELECT datname FROM pg_database;"
    cursor.execute(command)
    # connection.commit()
    list_tables = cursor.fetchall()
    print(list_tables)

    command = "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')"

    # cursor.execute(command)
    # connection.commit()
    command = "SELECT * FROM STUDENT;"
    cursor.execute(command)

    list_tables = cursor.fetchall()
    print(list_tables)

    # except (Exception, Error) as error:
    #     print("Error while connecting to PostgreSQL", error)
    # finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")



    time.sleep(2)
