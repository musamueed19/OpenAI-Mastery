def get_all_customers(db_cursor):
    """ Get All Customers """
    print("\nAll Customers:\n")
    for row in db_cursor.execute("SELECT * FROM customers"):
        print(row)