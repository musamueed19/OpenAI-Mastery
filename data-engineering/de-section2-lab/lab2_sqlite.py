import sqlite3

from data_seed import seed_data
from queries import DBQueryClass

# connect to database (file-based)
db = sqlite3.connect("ecommerce_store.db")
db_cursor = db.cursor()

# create tables (schema)
db_cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT UNIQUE
    )
    """
)

db_cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS products(
        product_id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL
    )
    """
)


db_cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        order_date TEXT,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
    """
)

# insert sample data
seed_data(db_cursor=db_cursor)


# commit changes and close connection
db.commit()

# queries data
query_client = DBQueryClass(db_cursor=db_cursor)

query_client.get_all_customers()
query_client.get_order_details()
# query_client.update_order_quantity(order_id=2, new_quantity=3)



# close connection
db.close()