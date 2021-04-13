from Products import *


def add_a_product():
    id = int(input("Enter id of product  "))
    name = input("Enter name of product  ")
    value = int(input("Enter value of product  "))
    packaging_quantity = int(input("Enter packaging quantity od product  "))
    pro = Product(id, name, value,packaging_quantity)
    add_product(pro)

def remove_a_product():
    print("Find product by ID or Name: \n")
    q = int(input("1.Press 1 to find by ID\n2.Press 2 to find by Name  "))
    if(q==1):
        id = int(input("Enter id of the product to delete "))
        remove_product_id(id)
        print("Product deleted successfully")
    if(q==2):
        name = input("Enter name of product to delete  ")
        remove_product_name(name)
        print("Product deleted successfully")

def list_all_products():
    print("Here is the list of all the products")
    print("Products\t\t\t\t\tID")
    product_list = showall()
    for i in product_list:
        print(str(i[0])+"\t\t\t\t\t\t"+str(i[1]))

def update_product():
    print("Find product by ID or Name: \n")
    q = int(input("1.Press 1 to find by ID\n2.Press 2 to find by Name  "))
    if (q == 1):
        id = int(input("Enter id of the product to update  "))
        product_details_id(id)
        print("Enter the field you would like to update  ")
        option = int(input("Type 1 to replace value of product\nType 2 to replace package quantity of product  "))
        if(option == 1):
            value = int(input("Enter new value of product  "  ))
            update_product_id(id,1,value)
        else:
            packaging_quantity = int(input("Enter new package quantity  "  ))
            update_product_id(id,2,packaging_quantity)
        product_details_id(id)
        print("Product updated successfully")
    if (q == 2):
        name = input("Enter name of product to update   ")
        product_details_name(name)
        print("Enter the field you would like to update  ")
        option = input("Type 1 to replace value of product\nType 2 to replace package quantity of product  ")
        if (option == 1):
            value = int(input("Enter new value of product  "))
            update_product_name(name,1, value)
        else:
            packaging_quantity = int(input("Enter new package quantity  " ))
            update_product_name(name,2, packaging_quantity)
        product_details_name(name)
        print("Product updated successfully")


def inquire_product():
    print("Find product by ID or Name: \n")
    q = int(input("1.Press 1 to find by ID\n2.Press 2 to find by Name  "))
    if (q == 1):
        id = int(input("Enter id of the product  "))
        print("\n")
        product_details_id(id)
    if (q == 2):
        name = input("Enter name of product  ")
        print("\n")
        product_details_name(name)


def product_details_id(id):
    print("Here is the details of product")
    product_details = showproduct_id(id)
    for i in product_details:
        print("ID of the product is:\t\t\t\t\t\t" + str(i[0]))
        print("Name of the product is:\t\t\t\t\t\t" + str(i[1]))
        print("Value of the product is:\t\t\t\t\t" + str(i[2]))
        print("Packaging Quantity of the product is:\t\t" + str(i[3]))
        print("\n")

def product_details_name(name):
    print("Here is the details of product")
    product_details = showproduct_name(name)
    for i in product_details:
        print("ID of the product is:\t\t\t\t\t\t" + str(i[0]))
        print("Name of the product is:\t\t\t\t\t\t" + str(i[1]))
        print("Value of the product is:\t\t\t\t\t" + str(i[2]))
        print("Packaging Quantity of the product is:\t\t" + str(i[3]))
        print("\n")
