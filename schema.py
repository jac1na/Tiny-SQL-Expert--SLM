SCHEMA = """
Users (
    user_id INT PRIMARY KEY,
    name TEXT,
    email TEXT
)

Orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    amount DECIMAL,
    FOREIGN KEY(user_id) REFERENCES Users(user_id)
)

Products (
    product_id INT PRIMARY KEY,
    name TEXT,
    price DECIMAL
)

OrderItems (
    item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY(order_id) REFERENCES Orders(order_id),
    FOREIGN KEY(product_id) REFERENCES Products(product_id)
)
"""
BASE_PROMPT = f"""
Convert the user question into a SQL query.

Use ONLY the following schema:
{SCHEMA}

RULES:
- Output ONLY SQL.
- No explanation.
- No markdown.
- Use JOINs when needed.
- Do NOT invent columns or tables.
"""
ALLOWED_TABLES = {
    "users": ["user_id", "name", "email"],
    "orders": ["order_id", "user_id", "order_date", "amount"],
    "products": ["product_id", "name", "price"],
    "orderitems": ["item_id", "order_id", "product_id", "quantity"]
}
