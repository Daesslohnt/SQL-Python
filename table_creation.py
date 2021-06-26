import pymysql


def create_tables():
    try:
        connection = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            passwd="1234",
            database="students"
        )
        # print ('Connection is successful')
        # print ('#' * 20)
        try:
            with connection.cursor() as cursor:
                create_tabel_query = """
                CREATE TABLE IF NOT EXISTS exemplar (
                id INT NOT NULL AUTO_INCREMENT,
                book_name VARCHAR(60),
                author VARCHAR(300),
                verlag VARCHAR(100),
                year INT,
                PRIMARY KEY(id)
                )
                """
                cursor.execute(create_tabel_query)
            with connection.cursor() as cursor:
                create_table_query = """
                    CREATE TABLE IF NOT EXISTS student(
                    id INT NOT NULL AUTO_INCREMENT,
                    std_name VARCHAR(60),
                    book_name VARCHAR(60),
                    get DATE NOT NULL,
                    back DATE,
                    PRIMARY KEY (id),
                    FOREGING KEY (id) REFERENCE exemplar(id),
                    FOREGING KEY (id) REFERENCE exemplar(book_name)
                    )
                """
                cursor.execute(create_tabel_query)
                #print ('table student was successfully created')
            with connection.cursor() as cursor:
                create_database_vorschau = """
                    CREATE TABLE IF NOT EXISTS vorschau(
                        book_name VARCHAR(60),
                        author VARCHAR (300),
                        verlag VARCHAR (100),
                        year INT,
                        count INT,
                        id_s VARCHAR(100)
                        )
                    """
                cursor.execute(create_database_vorschau)
                # print ('Table vorschau created successfully')
        finally:
            connection.close()
    except Exception as ex:
        print ('Connection is redused')
        print (ex)

if __name__ == '__main__':
    create_tables()