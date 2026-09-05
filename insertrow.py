import psycopg2
def insertrow(num, name,dept):
    conn = None
    try:
        conn = psycopg2.connect(database = "sqliitm",user='postgres',password='ramanujan@1729',host='127.0.0.1',port = 5433)
        cur = conn.cursor()
        cur.execute("insert into employee(emp_num,emp_name,department) values(%s,%s,%s)", (num,name,dept))
        conn.commit()
        print("total number or rwo is inserted")

        cur.close()
    except (Exception,psycopg2.DatabaseError) as e:
        print(e)
    finally:
        if conn is not None:
            conn.close()
insertrow(100,'bhaskara','HR')
    