import sqlite3
import arrow


timenow = arrow.now()
def createdatabase(namedatabase):
        #Creates a database with the table buttonpush. Give it the name of database.
        conn = sqlite3.connect('{}.db'.format(namedatabase))
        c = conn.cursor()

        c.execute('''CREATE TABLE buttonpush
                     (date text, username text, length real)''')

def pushbutton(namedatabase, username, lentime):
    #Perform a button push based on current time. Give it 
    #database name, username, and amount button is held for. 
    conn = sqlite3.connect('{}.db'.format(namedatabase))
    
    c = conn.cursor()
    timenow = arrow.now()


    c.execute("INSERT INTO buttonpush VALUES ('{}','{}', {})".format(timenow.timestamp,
                                                                        username, lentime))

    conn.commit()
    conn.close()
    
def readata(namedatabase):
    #This reads the database. Give it name of database.
    conn = sqlite3.connect('{}.db'.format(namedatabase))
    c = conn.cursor()

    c.execute('SELECT * FROM buttonpush')
    #conn.close()
    return(c.fetchall())
    conn.close()
    
def createdbtext(namedatabase):
    #creates database table for textmessage. Give it name of database. 
    conn = sqlite3.connect('{}.db'.format(namedatabase))
    c = conn.cursor()

    c.execute('''CREATE TABLE message
                    (date text, friendname text, username text, message text)''')
    
def createtext(namedatabase, friendname, username, message):
    #creates a database entry from friend to username. Input friendname, their 
    #username, and the message. This is then saved in the database for when 
    #username pushes the button. 
    conn = sqlite3.connect('{}.db'.format(namedatabase))
    
    c = conn.cursor()
    timenow = arrow.now()


    c.execute("INSERT INTO message VALUES ('{}','{}', '{}', '{}')".format(timenow.timestamp,
                                                                            friendname, 
                                                                            username, message))

    conn.commit()
    conn.close()
    
def readtext(namedatabase):
    #This reads the database of messages. Give it name of database.
    conn = sqlite3.connect('{}.db'.format(namedatabase))
    c = conn.cursor()

    c.execute('SELECT * FROM message')
    #conn.close()
    return(c.fetchall())
    conn.close()
    