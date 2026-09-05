import psycopg2

def createTable():
    conn = None
    try:
        conn = psycopg2.connect(database="sqliitm", user="postgres", password='ramanujan@1729', host="127.0.0.1", port=5433)
        cur = conn.cursor()  # create a new cursor
        cur.execute('''create table employee 
                  (emp_num int primary key not null,
                  emp_name varchar(20) not null,
                  department varchar(30) not null)''')
        conn.commit()  # commit the changes to the database
        print("Table created successfully")
        cur.close()  # close the cursor
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

createTable()  # call function — at module level, not inside the function