import sqlite3

def create_db():
    conn = sqlite3.connect("todo_list.db")



    # create tables

    conn.execute('PRAGMA foreign_keys = ON')
    conn.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT 
    );
    ''')
    conn.execute('''
    CREATE TABLE IF NOT EXISTS UserDetails(
    user_details_id INTEGER PRIMARY KEY ,
    user_id INTEGER ,
    phone_number TEXT,
    preferences TEXT,
    address TEXT,
    FOREIGN KEY(user_id) REFERENCES Users(user_id)
    );
    ''')
    conn.execute('''
    CREATE TABLE IF NOT EXISTS Tasks(
    task_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    description TEXT, 
    date DATETIME,
    status TEXT,
    FOREIGN KEY(user_id) REFERENCES Users(user_id)
    );
    ''')
    conn.execute('''
    CREATE TABLE IF NOT EXISTS Tags(
    Tag_id INTEGER PRIMARY KEY,
    name TEXT
    );
    ''')
    conn.execute('''
    CREATE TABLE IF NOT EXISTS TasksTags(
    task_id INTEGER,
    tag_id INTEGER,
    PRIMARY KEY(task_id,tag_id) 
    FOREIGN KEY(task_id) REFERENCES Tasks(task_id),
    FOREIGN KEY(tag_id) REFERENCES Tags(tag_id)
    );
    ''')

    conn.commit() #This line saves (commits) any changes made to the database during the current transaction.

                  #In SQLite (and other databases), when you execute SQL commands like CREATE TABLE, INSERT, UPDATE, or DELETE, the changes are not immediately written to the database. Instead, they are held in a temporary state until you explicitly call commit().

                  #If you don’t call commit(), the changes will be lost when the connection is closed.

    conn.close() #This line closes the connection to the database.

                 #It is important to close the connection after you’re done working with the database to free up resources and ensure that all changes are properly saved.




if __name__ == "__main__"  :
    create_db()