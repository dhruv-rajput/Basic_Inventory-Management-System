
import sqlite3
from productData import Product

conn = sqlite3.connect('database.db')

c = conn.cursor()

c.execute("""CREATE TABLE Product (
            pid integer not null primary key,
            name text,
            value integer,
            packaging_quantity integer
            )""")


def add_product(pro):
    try:
        with conn:
            c.execute("INSERT INTO Product VALUES (:pid, :name, :value,:packaging_quantity)", {'pid': pro.pid, 'name': pro.name, 'value' :pro.value,'packaging_quantity':pro.packaging_quantity})
            print("Product added successfully!")
    except:
        print("Product with this id already exists\n")


def showall():
    c.execute("SELECT name,pid FROM Product")
    return c.fetchall()

def showproduct_id(id):
    c.execute("SELECT * FROM Product where pid = :id",{'id':id})
    return c.fetchall()

def showproduct_name(name):
    c.execute("SELECT * FROM Product where name = :name",{'name':name})
    return c.fetchall()

def remove_product_id(id):
    with conn:
        c.execute("DELETE from Product where pid = :id ", {'id': id})

def remove_product_name(name):
    with conn:
        c.execute("DELETE from Product where name = :name ", {'name': name})


def update_product_id( id, n ,new_value ):
    if(n==1):
        with conn:
            c.execute("UPDATE Product SET value = :new_value where pid = :id" , {'new_value':new_value ,'id':id})
    if (n == 2):
        with conn:
            c.execute("UPDATE Product SET packaging_quantity = :new_value where pid = :id", {'new_value':new_value, 'id':id})



def update_product_name(name,n,new_value):
    if (n == 1):
        with conn:
            c.execute("UPDATE Product SET value = :new_value where name = :name", {'new_value': new_value, 'id': name})
    if (n == 2):
        with conn:
            c.execute("UPDATE Product SET packaging_quantity = :new_value where name = :name",
                      {'new_value': new_value, 'name': name})
