# Import OS and sqlite3
import os                   
import sqlite3             



# Utilized the list of file names for assignment.
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \                   
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')              



# Established connection to test.db.
conn = sqlite3.connect('C:\\Users\saeri\\OneDrive\\Documents\\GitHub\\Python-Projects\\test.db')                    



# Commented out following section. Utilized to delete tbl_files to set up proper execution of assignment.
"""
def deleteTbl():
    
    with conn:
        cur = conn.cursor()
        cur.execute("DROP TABLE tbl_files;")
        conn.commit()
"""



#Creates database if not already created.
def createDB():                                                                 
    
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename TEXT \
            )")
        conn.commit()



# Uses a for loop to go through fileList, and if the selected index string value contains '.txt', inserts index string value to col_filename.
def appendList():                                                                                           

    with conn:
        for x in fileList:
            if '.txt' in x:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_files(col_filename) VALUES ('" + x + "')")



# Prints file name of ever entry in col_filename.
def printList():

    with conn:
        cur = conn.cursor()
        cur.execute("SELECT col_filename FROM tbl_files")
        varFile = cur.fetchall()
        for item in varFile:
            msg = "File Name: {}".format(item[0])
            print(msg)
        


# Commented out function. Reinstate function if need to reset conditions for assignment.
# deleteTbl()
createDB()
appendList()
printList()



# Close connection after all tasks are completed.
conn.close()

