#------------------------------------------#
# Title: Assignment07.py
# Desc: Working with classes and functions.
# Updated: Error Handling and Pickling, with write to and read data from .dat binary file 
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# LSmileski, 2022-Nov-17, Created File
# LSmileski, 2022-Nov-18, Edited File
# LSmileski, 2022-Nov-19, Edited File
# LSmileski, 2022-Nov-21, Edited File
# LSmileski, 2022-Nov-25, Edited File
#------------------------------------------#

import pickle
# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
binaryFileName = 'CDInventory.dat' # data storage file
objFile = None  # file object

# -- PROCESSING -- #
class DataProcessor:
    """Adding and deleting data to and from inventory"""
    # TOdone add functions for processing here
    @staticmethod
    def add_cd_data(newID, newTitle, newArtist):
        """Function that saves user input into a dictionary row
        
        Args:
            newID, newTitle, newArtist: saving to dictinary row
             
        Returns:
            None
        """   
        dicRow = {'ID': int(newID), 'Title': newTitle, 'Artist': newArtist}
        lstTbl.append(dicRow)       
    
    @staticmethod
    def delete_cd():
        """Function is searching thru table and deleting cd from inventory
        
        Args:
            None
             
        Returns:
            None
        """
        intRowNr = -1
        blnCDRemoved = False
        try:
            for row in lstTbl:
                intRowNr += 1
                if row['ID'] == intIDDel:
                    del lstTbl[intRowNr]
                    blnCDRemoved = True
                    break
            if blnCDRemoved:
                print('The CD was removed')
            else:
                print('Could not find this CD!')
        except NameError:
            print('Please enter ID number that is on the curent inventory list!')

class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Reads table data from file file_name
        
        Args:
            file_name (String): The file name used to read the data from.
             
        Returns:
            table (Object): from the file file_name
        """
        with open(file_name, 'rb') as objFile:
            table = pickle.load(objFile) #load one line of table
        return table
    

    @staticmethod
    def write_file(file_name, table):
        """Saves table data to file file_name
        
        Args:
            table (Object): The table to be saved to file.
            file_name (String): The file name used to save the data to.
             
        Returns:
            None
        """
        # TOdone Add code here
        with open(file_name, 'wb') as objFile:
            pickle.dump(table, objFile)

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    # TOdone add I/O functions as needed
    @staticmethod
    def add_cd():
        """Function asks user to input ID, CD title and artist name

        Args:
            None.

        Returns:
            user inputs newID, newTitle and newArtist.
         """     
        while True:
            try:
                newID = int(input('Enter ID: ').strip())
                break
            except ValueError:
                print('You entered wrong value!Please enter number for ID!')
        newTitle = input('What is the CD\'s title? ').strip()
        newArtist = input('What is the Artist\'s name? ').strip()  
        return newID, newTitle, newArtist   
# 1. When program starts, read in the currently saved Inventory
        FileProcessor.read_file(binaryFileName, lstTbl)
    
# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(binaryFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        
        # TOdone move IO code into function
        ID = 0
        Title = 'None'
        Artist = 'None'
        try: 
            ID, Title, Artist = IO.add_cd()
        except TypeError:
            print('Value is not of the expected type')
        
        # 3.3.2 Add item to the table
        # TOdone move processing code into function
        DataProcessor.add_cd_data(ID, Title, Artist) 
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.5 process delete a CD
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        try:
            intIDDel = int(input('Which ID would you like to delete? ').strip())
        except:
            print("The ID that you entered does not exist!")
        # 3.5.2 search thru table and delete CD
        # TOdone move processing code into function
        DataProcessor.delete_cd()
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    # 3.6 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # TOdone move processing code into function
            FileProcessor.write_file(binaryFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




