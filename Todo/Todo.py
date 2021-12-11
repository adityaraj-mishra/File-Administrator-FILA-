# ToDo Manager
import os
from datetime import date

def createToDo():
    ToDoFile = open(f"{path}/ToDoList.txt",'w')
    CompFile = open(f"{path}/CompList.txt",'w')
    print("\n Enter the number ToDos you want to enter : ",end="")
    num = int(input())
    
    for i in range(0,num):
        print(f" Enter the ToDo-{i+1} : ", end="")
        todo = input()
        todoList.append(todo)

    updtFile(ToDoFile,todoList)
    displayToDo(todoList)
    ToDoFile.close()
    CompFile.close()


def updtToDo():
    ToDoFile = open(f"{path}/ToDoList.txt",'w')
    print(" Enter the ToDo : ", end="")
    todo = input()
    todoList.append(todo)
    updtFile(ToDoFile,todoList)
    displayToDo(todoList)
    ToDoFile.close()


def cmpltToDo():

    displayToDo(todoList)
    print(" Enter the ToDo Number that you have completed : ",end="")
    tnum = int(input())
    item = todoList[tnum-1]
    todoComp.append(item)
    todoList.pop(tnum-1)
    CompFile = open(f"{path}/CompList.txt",'w')
    ToDoFile = open(f"{path}/ToDoList.txt",'w')
    updtFile(CompFile,todoComp)
    updtFile(ToDoFile,todoList)
    displayToDo(todoList)
    CompFile.close()
    ToDoFile.close()


def displayToDo(list):
    size = len(list)
    for item in range(size):
        print(f" {item+1}. {list[item]}")


def updtList(file,list):
    list = []
    for item in file:
        list.append(item.strip())
    return list


def updtFile(file,list):
    for i in list:
        file.write(i)
        file.write("\n")


def createDir():
    curDate = date.today()
    fname = curDate.strftime("%d%m%Y")
    path = os.path.join(os.getcwd(),fname)
    
    checkPath = os.path.exists(path)
    if(checkPath == False):
        os.mkdir(path)
    
    return path,curDate


def checkDirFile():
    global todoList
    global todoComp
    checkFile = os.path.exists(f"{path}/ToDoList.txt")
    checkComp = os.path.exists(f"{path}/CompList.txt")
    if(checkFile and checkComp):
        ToDoFile = open(f"{path}/ToDoList.txt",'r')
        CompFile = open(f"{path}/CompList.txt",'r')

        todoList = updtList(ToDoFile,todoList)
        todoComp = updtList(CompFile,todoComp)        

        ToDoFile.close()
        CompFile.close()
        
    

def checkDate():
    newDate = date.today()

    if(newDate != curDate):
        
        newFname = newDate.strftime("%d%m%Y")
        newpath = os.path.join(os.getcwd(),newFname)
        createDir()
        newtodoList = []
        newtodoComp = []
        return newDate,newpath,newtodoList,newtodoComp

    return newDate,path,todoList,todoComp


print("\n Hello User! Welcome to ToDo Manager")
print("\n Choose the operations you want to use : ")

todoList = []
todoComp = []


path,curDate = createDir()
checkDirFile()

choice=0
while(choice != 5):

    print(" 1. Create ToDo List")
    print(" 2. Add More in ToDo List")
    print(" 3. Move a ToDo to Completed List")
    print(" 4. Display ToDo List")
    print(" 5. Exit")
    print(" Choice? ",end="")
    choice = int(input())
    curDate,path,todoList,todoComp = checkDate()

    if(choice == 1):
        createToDo()
        print()
    elif(choice == 2):
        updtToDo()
        print()
    elif(choice == 3):
        cmpltToDo()
        print()
    elif(choice == 4):
        displayToDo(todoList)
        print()
    elif(choice == 5):
        exit(0)
    else:
        print(" !! WRONG CHOICE, TRY AGAIN !!\n")
        print()
