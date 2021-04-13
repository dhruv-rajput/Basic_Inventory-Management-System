from Products import *
from productData import Product
from Input import *

def main():

    print(" SELECT THE NUMBER OF OPERATION YOU WOULD LIKE TO PERFORM")
    print(" 1.Add a product \n 2.Remove a product \n 3.Edit specifics of a product\n 4.List all products\n 5.Inquire about a product\n 6.Quit\n 7.See all commands again\n")
    q = int(input("Enter here - "))
    if (q == 1):
        add_a_product()
        command()
    if (q == 2):
        remove_a_product()
        command()
    if (q == 3):
        update_product()
        command()
    if (q == 4):
        list_all_products()
        command()
    if (q == 5):
        inquire_product()
        command()
    if (q == 6):
        exit()
    if (q == 7):
        main()

def command():
    command = int(input("Enter 7 to see all command again or Enter 6 to quit "))
    if (command == 7):
        main()
    else:
        exit()
print(" Welcome to INVENTORY MANAGEMENT")
main()