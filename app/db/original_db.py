# coding=utf-8


from OnlineClassroom.app.ext.plugins import original_db




def task(arg):
    conn = original_db.raw_connection()      #拿到的是一个原生的pymysql连接对象
    cursor = conn.cursor()
    cursor.execute(
        "select * from t1"
    )
    result = cursor.fetchall()
    cursor.close()
    conn.close()