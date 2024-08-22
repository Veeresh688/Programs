# CRUDS operation on domain "Bank".

dataFile = "bank.dat"
dataDictionary = {}
givenId = "**"
isAccountFound = 0

def printNoRecordFound():
	print("No account found with the id equal to " + givenId + ".\n")
	
def printSuccessMessage(operationName):
	print("operation " + operationName + " is done successfully.\n")

def search():
	global isAccountFound
	isAccountFound = 0
	for accountId, data in dataDictionary.items():
		if givenId == accountId:
			isAccountFound = 1
			break

def getId(operationName):
	global givenId
	givenId = input("Enter account ID to " + operationName + ": ")

def loadAccounts():
	global dataDictionary
	oDataFile = open(dataFile, "r")
	dataDictionary = eval(oDataFile.read())
	oDataFile.close()
	saveAccounts()

def saveAccounts():
	oDataFile = open(dataFile, "w")
	oDataFile.write(str(dataDictionary))
	oDataFile.close()

def addBankAccount():
	global dataDictionary
	accountId = input("Account ID: ")
	dataDictionary[accountId] = [input("Account holder name: "), input("Balance: ")]
	saveAccounts()

def readBankAccounts():
	for accountId, data in dataDictionary.items():
		print("\nID = " + accountId + "\nAccount holder name = " + data[0] + "\nBalance = " + data[1])

def searchBankAccount():
	getId("search")
	search()
	if isAccountFound == 1:
		print("Account found.\n")
	else: 
		printNoRecordFound()

def updateBankAccount():
	global dataDictionary
	getId("update")
	search()
	if isAccountFound == 1:
		option = int(input("1) Update user name\n2) Update balance\nEnter choice: "))
		if option == 1:
			dataDictionary[givenId][0] = input("Enter new user name: ")
		elif option == 2:
			dataDictionary[givenId][1] = input("Enter new balance: ")
		else:
			print("Invalid choice.\n")
		printSuccessMessage("update")
	else:
		printNoRecordFound()
	saveAccounts()


def deleteBankAccount():
	global dataDictionary
	getId("delete")
	search()
	if isAccountFound == 1:
		dataDictionary.pop(givenId)
		printSuccessMessage("delete")
		saveAccounts()
	else:
		printNoRecordFound()

def exit():
	quit()

def showMenu():
	loadAccounts()
	operationList = [addBankAccount, readBankAccounts, searchBankAccount, updateBankAccount, deleteBankAccount, exit]
	choice = 1
	while choice > 0:
		operationList[int(input("1) Add bank account\n2) Read bank account\n3) Search bank account\n4) Update bank account\n5) Delete bank account\n6)Exit\nEnter your choice: ")) - 1]()

showMenu()