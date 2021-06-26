import pymysql
from pymysql import connections

rows = tuple()

def Connect_to_table():
    connection = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="1234",
        database="students"  
    )
    return connection

def select_all(table): #select and return all tuples of rows from exemplar
    try:
        connection = Connect_to_table()
        try:
        #   Take all data from table exemplar
            with connection.cursor() as cursor:
                query = "SELECT * FROM " + table
                cursor.execute(query)
                global rows
                rows = cursor.fetchall()
        finally:
            connection.close()
            return rows
    except Exception as ex:
        print ('Connection is refused')
        print (ex)

# insert a row of datas for exemplar
def insert(bname, author, verlag, year):
    try:
        connection = Connect_to_table()
        try:
            with connection.cursor() as cursor:
                query = "INSERT INTO "
                query += "exemplar (book_name, author, verlag, year) VALUES"
                query += '(\'' + bname + '\', \'' + author + '\', \'' + verlag + '\', ' + str(year) + ')'
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()
    except Exception as ex:
        print ('Connection is refused')
        print (ex)

def insert_vorschau(bname, author, verlag, year, count, id_s):
    try:
        connection = Connect_to_table()
        try:
            with connection.cursor() as cursor:
                query = "INSERT INTO "
                query += "vorschau (book_name, author, verlag, year, count, id_s) VALUES"
                query += '(\'' + bname + '\', \'' + author + '\', \'' + verlag + '\', ' + str(year) + ', ' + str(count) + ', \'' + id_s + '\' )'
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()
    except Exception as ex:
        print ('Connection is refused')
        print (ex)

def insert_student(bname, get, back):
    try:
        connection = Connect_to_table()
        try:
            with connection.cursor() as cursor:
                query = "INSERT INTO "
                query += "vorschau (book_name, author, verlag, year, count, id_s) VALUES"
                query += '(\'' + bname + '\', ' + get + ', ' + back + ' )'
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()
    except Exception as ex:
        print ('Connection is refused')
        print (ex)

def Delete_vorschau():
    try:
        connection = Connect_to_table()
        try:
            with connection.cursor() as cursor:
                query = "DROP TABLE `vorschau`;" 
                cursor.execute(query)
                print ('tabe is successfully deleted')
        finally:
            connection.close()
    except Exception as ex:
        print ("Connection is Refused")
        print (ex)

def Delete_all():
    pass

if __name__ == "__main__":
    pass