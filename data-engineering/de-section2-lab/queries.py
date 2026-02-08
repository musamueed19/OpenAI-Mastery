class DBQueryClass:
    def __init__(self, db_cursor):
        self.db_cursor = db_cursor

    def execute_query(self, query):
        """Execute a query using the provided cursor and return all rows."""
        # db_cursor is a sqlite3 cursor in this project; reuse it directly
        self.db_cursor.execute(query)
        return self.db_cursor.fetchall()

    def execute_query_with_columns(self, query):
        """Execute a query and return (column_names, rows).

        column_names is a list of strings (from cursor.description) and rows
        is the result of fetchall(). This works with a sqlite3 cursor.
        """
        self.db_cursor.execute(query)
        cols = [col[0] for col in (self.db_cursor.description or [])]
        rows = self.db_cursor.fetchall()
        return cols, rows

    def get_all_customers(self):
        """Get all customers using the central execute_query helper."""
        query = "SELECT * FROM customers"
        print("\nAll Customers:")
        cols, rows = self.execute_query_with_columns(query)
        if cols:
            # print header
            print(" | ".join(cols))
            print("-" * (len(" | ".join(cols))))
        for row in rows:
            print(row)

    def get_order_details(self):
        """Get order details including customer and product info using execute_query."""
        query = (
            """
            SELECT o.order_id, c.name AS customer_name, p.name AS product_name,
                   p.price AS unit_price, o.quantity,
                   (o.quantity * p.price) AS total_price, o.order_date
            FROM orders o
            JOIN customers c ON c.customer_id = o.customer_id
            JOIN products p ON p.product_id = o.product_id
            """
        )
        print("\nOrder Details:")
        cols, rows = self.execute_query_with_columns(query)
        if cols:
            print(" | ".join(cols))
            print("-" * (len(" | ".join(cols))))
        for row in rows:
            print(row)
