
import queries
import table_creation
import pandas as pd



def Count_books(name, author):
    rows = queries.select_all('exemplar')
    counter = 0
    for row in rows:
        if (name in row) and (author in row):
            counter += 1
    return counter

def Find_all_id(name, author):
    rows = queries.select_all('exemplar')
    id_s = list()
    for row in rows:
        if (name in row) and (author in row):
            id_s.append(str(row[0]))
    return ', '.join(id_s)

def Get_all_data():
    rows = queries.select_all('exemplar')
    for item in rows:
        print (item)

def Get_vorschau():
    rows = queries.select_all('vorschau')
    columns = ['book name', 'author', 'verlag', 'year', 'count', 'id-s']
    df = pd.DataFrame(rows, columns=columns)
    print (df)

def Get_student():
    rows = queries.select_all('student')
    columns = ['id', 'book name', 'get', 'back']
    df = pd.DataFrame(rows, columns=columns)
    print (df)

def Insert_data_exemplar():
    bname = input('Enter the name of the book: ')
    author = input('Enter the author: ')
    verlag = input('Enter the verlag: ')
    year = int(input('Enter the year: '))
    queries.insert(bname, author, verlag, year)

def Insert_data_student():
    pass

def Search_for_name():
    try:
        table = input('Enter the tabel: ')
        name = input("Enter name of the book: ")
        datas = queries.select_all(table)
        result = list()
        for sample in datas:
            if sample[1] == name:
                result.append(sample)
        return tuple(result)
    except Exception as ex:
        print ("Error:" )
        print (ex)

def Search_for_id():
    try:
        table = input('Enter the tabel: ')
        id = int(input("Enter name of the id: "))
        datas = queries.select_all(table)
        result = list()
        for sample in datas:
            if sample[0] == id:
                result.append(sample)
        return tuple(result)
    except Exception as ex:
        print ("Error:" )
        print (ex)

def Search_for_author():
    try:
        table = input('Enter the tabel: ')
        author = input("Enter name of the author: ")
        datas = queries.select_all(table)
        result = list()
        for sample in datas:
            if sample[2] == author:
                result.append(sample)
        return tuple(result)
    except Exception as ex:
        print ("Error:" )
        print (ex)

def Reset_vorschau():
    queries.Delete_vorschau()
    table_creation.create_tables()
    data_for_vorschau = queries.select_all('exemplar')
    dataset = set()
    for sample in data_for_vorschau:
        if (sample[1] not in dataset):
            dataset.add(sample[1])
            queries.insert_vorschau(
            sample[1], 
            sample[2],  
            sample[3],  
            sample[4],  
            Count_books(sample[1], sample[2]),
            Find_all_id(sample[1], sample[2])
            )


Reset_vorschau()
####################################################################################################
print ('Commansd: get all data, insert data, search for name, search for id, search for author')
while True:

    command = input("Enter your command: ")
    if command == 'exit':
        break
    elif command == 'get all data':
        Get_all_data()
    elif command == 'get vorschau':
        Get_vorschau()
    elif command == 'insert data':
        Insert_data_exemplar()
        Reset_vorschau()
    elif command == 'search for name':
        datas = Search_for_name()
        for item in datas:
            print (item)
    elif command == 'search for id':
        datas = Search_for_id()
        for item in datas:
            print (item)
    elif command == 'search for author':
        datas = Search_for_author()
        for item in datas:
            print (item)