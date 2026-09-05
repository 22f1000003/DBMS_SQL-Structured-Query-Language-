import psycopg2
def selectall():
    conn = None
    try:
        conn = psycopg2.connect(database = "sqliitm",user='postgres',password='ramanujan@1729',host='127.0.0.1',port = 5433)
        cur = conn.cursor()
        cur.execute("select rollno , name ,dob from student ")
        rows = cur.fetchall() 
        for row in rows:
            print(print("rollnumber = " , row[0],",NAME = " , row[1] , " dateofbirth = ", row[2]))
            cur.close()
    except (Exception,psycopg2.DatabaseError) as e:
        print(e)

    finally:
        if conn is not None:
            conn.close()
selectall()