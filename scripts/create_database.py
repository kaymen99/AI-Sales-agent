import sqlite3
from products_list import products

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    model TEXT,
    processor TEXT,
    memory TEXT,
    storage TEXT,
    display TEXT,
    graphics TEXT,
    cooling TEXT,
    dpi TEXT,
    type TEXT,
    capacity TEXT,
    read_speed TEXT,
    write_speed TEXT,
    display_type TEXT,
    resolution TEXT,
    refresh_rate TEXT,
    size TEXT,
    connectivity TEXT,
    stripe_price_id TEXT,
    price REAL
)
''')

# Insert data into the table
for product in products:
    cursor.execute('''
    INSERT INTO products (
        category, model, processor, memory, storage, display, graphics, cooling, dpi, type, capacity, read_speed, write_speed, display_type, resolution, refresh_rate, size, connectivity, stripe_price_id, price
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        product.get('category'),
        product.get('model'),
        product.get('processor'),
        product.get('memory'),
        product.get('storage'),
        product.get('display'),
        product.get('graphics'),
        product.get('cooling'),
        product.get('dpi'),
        product.get('type'),
        product.get('capacity'),
        product.get('read_speed'),
        product.get('write_speed'),
        product.get('display_type'),
        product.get('resolution'),
        product.get('refresh_rate'),
        product.get('size'),
        product.get('connectivity'),
        product.get('stripe_price_id'),
        product.get('price')
    ))

# Commit changes and close the connection
conn.commit()
conn.close()