import psycopg2
def updatevalue(nameofstudent,rollnumber):
    conn = None
    try:
        conn = psycopg2.connect(database='sqliitm',user='postgres',password='ramanujan@1729',host='127.0.0.1',port=5433)
        cur = conn.cursor()
        cur.execute("update student set name = %s where rollno = %s " ,(nameofstudent,rollnumber))
        conn.commit()
        print("total number os rows updated :", cur.rowcount)
        cur.close()
    except (Exception,psycopg2.DatabaseError) as e:
        print(e)

    finally:
        if conn is not None:
            conn.close()
updatevalue('sdf','22f1000003')