def seed_data(db_cursor):
    """ Seed Data in the Tables """
    
    db_cursor.executemany(
        """
        INSERT OR IGNORE INTO customers (customer_id, name, email) VALUES (?,?,?)
        """,
        [
            (1, "Ahsan Nawab", "ahsannawab6@gmail.com"),
            (2, "Afzal Hussain", "afzalhussainj@gmail.com"),
        ]
    )
    
    db_cursor.executemany(
        """
        INSERT OR IGNORE INTO products (product_id, name, price) VALUES (?,?,?)
        """,
        [
            (1, "Chilli Sauce", 5.99),
            (2, "Ramen Noodles", 160),
        ]
    )
    
    db_cursor.executemany(
        """
        INSERT OR IGNORE INTO orders (order_id, customer_id, product_id, quantity, order_date) VALUES (?,?,?,?,?)
        """,
        [
            (1, 1, 1, 5, "2026-02-07"),
            (2, 1, 2, 1, "2026-02-07"),
            (3, 2, 1, 2, "2026-02-06"),
        ]
    )