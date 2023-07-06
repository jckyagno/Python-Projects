import os

fPath = 'C:\\Users\saeri\\OneDrive\\Documents\\GitHub\\Python-Projects\\Projects\\Script_Assignment'

def sortFunction():

    for x in os.listdir(fPath):
        if '.txt' in x:
            print(x)
            abPath = os.path.join(fPath, x)
            print(os.path.getmtime(abPath))

sortFunction()
