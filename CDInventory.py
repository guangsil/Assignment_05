#------------------------------------------#
# Title: CDInventory.py
# Desc: CDInventory to store CD Inventory data in dictionaries format
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# GuangSin_Lu, 2022-Feb-23, Modify TODO part
# GuangSin_Lu, 2022-Feb-27, Add Print function to info user
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
# replace list of lists with list of dicts
dicRow = {}  # dict of data row 
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    print('IMPORTANT!!! Before add new inventory, load data to check is there existed CD-Inventory')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    if strChoice == 'l': 
        # Add the functionality of loading existing data
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(",")
            dicRow = {"ID": lstRow[0], "Title": lstRow[1], "Artist": lstRow[2]}
            lstTbl.append(dicRow)
        print("====== Existed CD Inventory Loaded======\n")
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep=", ")
        print('\n=========================================\n')
        objFile.close()
        pass
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {"ID": intID, "Title": strTitle, "Artist": strArtist} # Modify it and replace the inner data structure by dictionaries 
        lstTbl.append(dicRow) 
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('=========================================\n')
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep=", ")
        print('\n=========================================\n')
    elif strChoice == 'd':
        # Add functionality of deleting an entry
        lstTbl.clear()
        print("===== Temporary Data Deleted =====\n")
        pass
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        print("===== CD Inventory Saved =====\n")
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ","
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

