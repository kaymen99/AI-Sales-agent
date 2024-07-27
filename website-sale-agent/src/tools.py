import os, requests, json
import sqlite3
import stripe
from litellm import completion
from embedchain import App

rag_config = {
    "llm": {
        "provider": "groq",
        "config": {
            "model": "mixtral-8x7b-32768",
            "api_key": os.getenv("GROQ_API_KEY"),
            "stream": True
        }
    },
    "embedder": {
        "provider": "huggingface",
        "config": {
            "model": "BAAI/bge-base-en-v1.5",
        },
    }
}

class FileSearchTool:
    def __init__(self):
        print("------------------- Initiate FIle Search Tool -------------------")
        self.app = App.from_config(config=rag_config)
        # Add your data source here
        self.app.add("./files", data_type="directory")
    
    def get_store_info(self, query: str) -> str:
        """Retrieve information about TechNerds' business, services, and products based on the provided query."""
        response = self.app.query(query)
        return str(response) 

def get_product_recommendation(product_category, user_query):
    """
    Retrieves products from the database based on a user query by leveraging an AI agent to generate search queries.

    Args:
        product_category (str): The query from the user to search for products.
        user_query (str): The user requiremenets query.

    Returns:
        list: A list of JSON objects representing the products that match the query.
    """
    # Connect to SQLite database
    conn = sqlite3.connect("./database.db")
    cursor = conn.cursor()

    products = [
        ("model", "processor", "memory", "storage", "display", "graphics", "cooling", "dpi", "type", "capacity", "read_speed", "write_speed", "display_type", "resolution", "refresh_rate", "size", "connectivity", "stripe_price_id", "price")
    ]
    query = f"SELECT * FROM products WHERE category = '{product_category}'"
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            products.append(row)
    except Exception as e:
        print(f"An error occurred: {e}")

    # Close the database connection
    conn.close()

    # Define the prompt for the AI agent
    prompt = f"""
    You are an expert in computer equipment with a deep understanding of various technical
    specifications and requirements.
    Your task is to recommend computer products based on user needs. You will be provided
    with the user requirements query and the list of products available in our store.
    Use your expertise to recommend to the user the best products that will fit his needs.

    Your answer must list all the products that might big good fit for the user. It must be
    comprehensive and concise as it will be used by the Sale agent to guide the user.
    For example:
    Based on the user requirements, these are are our best options:
    1. **Laptop X**: Features an Intel i7 processor, NVIDIA RTX 3070 graphics card, 16GB RAM, and 512GB SSD. Price: $1499.99
    2. **Laptop Y**: Comes with an Intel i7 processor, NVIDIA RTX 3070 graphics card, 32GB RAM, and 1TB SSD. Price: $1799.99
    """

    message = f"""
    USER QUERY: {user_query}
    PRODUCTS: {products}
    """

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": message}
    ]

    # Request to the AI agent to generate the SQL query
    response = completion(
        model="groq/llama3-70b-8192",
        messages=messages,
        temperature=0.1
    )

    # Extract the SQL queries from the response
    output = response.choices[0].message.content

    return output


def generate_stripe_payment_link(name: str, price: float, quantity: int) -> str:
    """Generate a stripe payment link for a customer based on a single query string."""
    conn = sqlite3.connect("./database.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM products WHERE model = '{name}' AND price = {price}"
    price_id = None
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            price_id = row[-2]
    except Exception as e:
        print(f"An error occurred: {e}")

    # Close the database connection
    conn.close()

    if not price_id:
        return "Price ID not found"

    stripe.api_key = os.getenv("STRIPE_API_KEY")
    session = stripe.checkout.Session.create(
      success_url="https://example.com/success",
      line_items=[{"price": price_id, "quantity": 1}],
      mode="payment",
    )
    return session.url


def generate_calendly_invitation_link(query: str) -> str:
    '''Generate a calendly invitation link based on the single query string'''
    api_key = os.getenv("CALENDLY_API_KEY")
    event_type_uuid = os.getenv("CALENDLY_EVENT_TYPE_UUID")
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    url = 'https://api.calendly.com/scheduling_links'
    payload = {
        "max_event_count": 1,
        "owner": f"https://api.calendly.com/event_types/{event_type_uuid}",
        "owner_type": "EventType"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        data = response.json()
        return f"url: {data['resource']['booking_url']}"
    else:
        return "Failed to create Calendly link"