"""
Main application for running queries against the wootronics database
"""
# Third-part imports
from dotenv import load_dotenv

# Custom application imports
from init_db import setup_database, connect_db

load_dotenv()


def query_items_in_order(cursor, order_number):
    """
    Query for all items contained within a given order number.

    :param cursor: cursor to run commands against the database
    :param order_number: the order id you want to find all related items
    """

    sql_query = """
        SELECT ordered_products.order_id, orders.date,
            products.name, products.price, customers.first_name, customers.last_name
        FROM ordered_products
            INNER JOIN orders
                ON ordered_products.order_id = orders.order_id
            INNER JOIN products
                ON ordered_products.product_id = products.product_id
            INNER JOIN customers
                ON orders.customer_id = customers.customer_id
        WHERE ordered_products.order_id = %s;
    """

    cursor.execute(sql_query, (order_number,))
    for record in cursor.fetchall():
        print(record)


def query_orders_containing_item(cursor, item_number):
    """
    Query for all orders containing a given product.

    :param cursor: cursor to run commands against the database
    :param item_number: the item id you want to find all orders containing that item
    """

    sql_query = """
        SELECT ordered_products.product_id, products.name, products.price,
            orders.order_id, orders.date, customers.first_name, customers.last_name
        FROM ordered_products
            INNER JOIN orders
                ON orders.order_id = ordered_products.order_id
            INNER JOIN products
                ON products.product_id = ordered_products.product_id
            INNER JOIN customers
                ON customers.customer_id = orders.customer_id
        WHERE ordered_products.product_id = %s;
    """

    cursor.execute(sql_query, (item_number,))
    for record in cursor.fetchall():
        print(record)


def main():
    """
    Main function to run the application
    """
    setup_database('wootronics-data.csv')
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    
    for order_number in range(1,8):
        print(f"Find all items associated with order #{order_number}")
        query_items_in_order(cursor, order_number)
        print()
    
    for product_number in range(1,6):
        print(f"Find all orders that have product #{product_number}")
        query_orders_containing_item(cursor, product_number)
        print()


if __name__ == "__main__":
    main()
