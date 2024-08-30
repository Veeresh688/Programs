# Framework program using the database.

import sqlite3

dataBasePath = 'C:\\Users\\hsuao\\Framework.db'
menuTableName = 'fwTable'
connection = sqlite3.connect(dataBasePath)
cursor = connection.cursor()

dataTableName = None
dataTableFields = None
menuData = None
isItemFound = 0
givenId = None

def getDataTableName():
    global dataTableName
    cursor.execute(f"SELECT menuValue FROM {menuTableName} WHERE key = 'Title'")
    record = cursor.fetchone()
    if record:
        dataTableName = record[0]
    else:
        print("No data found for 'Title'")
        dataTableName = None

def getFieldValues():
    global dataTableFields
    if dataTableName:
        cursor.execute(f"PRAGMA table_info('{dataTableName}')")
        headers = cursor.fetchall()
        dataTableFields = [header[1] for header in headers]
    else:
        dataTableFields = []

def getMenuData():
    global menuData
    cursor.execute(f"SELECT menuValue FROM {menuTableName} WHERE key = 'menu'")
    menu_record = cursor.fetchone()
    if menu_record:
        menuData = menu_record[0]
    else:
        menuData = "No menu data found."

def printSuccessMessage(operationName):
    print(operationName + " successfully.")

def printSavedMessage():
    command = f"select menuValue from {menuTableName} where key = 'SavedMessage'"
    cursor.execute(command)
    message = cursor.fetchone()
    savedMessage = message[0]
    print(savedMessage)


def addRecord():
    if dataTableFields:
        recordValues = []
        for dataTableField in dataTableFields:
            recordValues.append(input(f"Enter {dataTableField}: "))
        recordValues = tuple(recordValues)
        command = f"insert into {dataTableName} values {recordValues}"
        cursor.execute(command)
        connection.commit()
        printSavedMessage()
    else:
        print("No table fields found.")

def readRecords():
    if dataTableName:
        cursor.execute(f"SELECT * FROM {dataTableName}")
        records = cursor.fetchall()
        print()
        for record in records:
            for indexCounter in range(len(dataTableFields)):
                print(f"{dataTableFields[indexCounter]}: {record[indexCounter]}")
            print()
    else:
        print("No data table available.")

def getId(operationName):
    global givenId
    givenId = input(f"Enter {dataTableFields[0]} to {operationName}: ")

def printNoRecordFound():
    print(f"No record found with id '{givenId}'.\n")

def search():
    global isItemFound
    isItemFound = 0
    if dataTableName and dataTableFields:
        # key = "dataTableFields[0]" 
        #cursor.execute(f"select * from {dataTableName} where {dataTableFields[0]} = {givenId}")
        # query = "select * from " + dataTableName +  " where \"" +  dataTableFields[0] + "\" = \'" + givenId + "\'"
        #print(query)
        query = f"select * from {dataTableName} where \"{dataTableFields[0]}\" = \'{givenId}\'"
        cursor.execute(query)
        records = cursor.fetchall()
        if records:
            isItemFound = 1    

def searchRecord():
    global isItemFound
    getId("search")

    search()

    if isItemFound:
        print("Record found.\n")
    else:
        printNoRecordFound()

def updateRecord():
    getId("update")
    search()
    if isItemFound == 0:
        printNoRecordFound()
    else:
        for indexCounter in range(1, len(dataTableFields)):
            print(f"{indexCounter}. Update {dataTableFields[indexCounter]}")    
        choice = int(input("Enter choice: "))
        if choice <= len(dataTableFields) - 1:
            newValue = input(f"Enter new {dataTableFields[choice]}: ")
            #command = "update " + dataTableName + " set \"" + dataTableFields[choice] + "\" = \'" + newValue +  "\' where \"" + dataTableFields[0] + "\" = \'" + givenId + "\'"
            command = f"update {dataTableName} set \"{dataTableFields[choice]}\" = \'{newValue}\' where \"{dataTableFields[0]}\" = \'{givenId}\'"
            # print(command)
            cursor.execute(command)
            connection.commit()
            printSuccessMessage("Updated")
        else:
            print("Invalid choice.")

def deleteRecord():
    getId("delete")
    search()
    if isItemFound == 0:
        printNoRecordFound()
    else:
        choice = int(input("Do you really want to delete record\n\t1) Yes\t2) No\nEnter choice: "))
        if choice == 2:
            print("Delete operation cancelled.")
        elif choice > 2:
            print("Invalid choice.")
        else:
            command = f"delete from {dataTableName} where \"{dataTableFields[0]}\" = '{givenId}'"
            cursor.execute(command)
            printSuccessMessage("Deleted")
            connection.commit()

def close():
    connection.close()
    print("Connection closed.")
    exit()

def mainMenu():
    global dataTableName
    getDataTableName()
    getFieldValues()
    getMenuData()
    operationNames = [addRecord, readRecords, searchRecord, updateRecord, deleteRecord, close]
    while True:
        print(menuData)
        operationNames[int(input("Enter choice: ")) - 1]()
            

mainMenu()

