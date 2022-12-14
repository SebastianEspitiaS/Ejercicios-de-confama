#find menu in python.
# Source: https://stackoverflow.com/a/59138799 .
mylist = []
def list():

    operation = input('''Select operation:\n [1] Add number to the list \n [2] Remove number from the list \n [3] Display list\n ''')


    if operation == '1':
        print("Type the number you would like to add to the list: ")
        number = int(input())
        mylist.append(number)

    elif operation == '2':
        print("Type position of the element number you like to remove from the list: ")
        number = int(input())
        mylist.pop(number)

    elif operation == '3':
        print(mylist)

    else:
        print('You have not chosen a valid operator, please run the program again.')

    again()

def again():
    list_again = input('''Would you like to see main menu again? (Y/N)''')

    if list_again.upper() == 'Y':
        list()
    elif list_again.upper() == 'N':
        print('OK. Bye bye. :)')
    else:
        again()

list()
