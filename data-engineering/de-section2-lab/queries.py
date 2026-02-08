class DBQueryClass:
    def __init__(self, db_cursor):
        self.db_cursor = db_cursor

    def execute_query(self, query):
        """Execute a query using the connection's cursor and return all rows."""
        self.db_cursor.execute(query)
        return self.db_cursor.fetchall()

    def get_all_customers(self):
        """Get all customers using the central execute_query helper."""
        query = "SELECT * FROM customers"
        print("\nAll Customers:")
        rows = self.execute_query(query)
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
        rows = self.execute_query(query)
        for row in rows:
            print(row)
