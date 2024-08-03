import sqlite3
from pydantic import Field
from .base_tool import BaseTool
from src.agents.agent import PatchLiteLLM
from src.agents.models import models_list


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
        (
            "model",
            "processor",
            "memory",
            "storage",
            "display",
            "graphics",
            "cooling",
            "dpi",
            "type",
            "capacity",
            "read_speed",
            "write_speed",
            "display_type",
            "resolution",
            "refresh_rate",
            "size",
            "connectivity",
            "stripe_price_id",
            "price",
        )
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
    prompt = """
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
        {"role": "user", "content": message},
    ]

    # Request to the AI agent to generate the SQL query
    client = PatchLiteLLM(models_list)
    response = client.completion(
        model="groq/mixtral-8x7b-32768", messages=messages, temperature=0.1
    )

    # Extract the SQL queries from the response
    output = response.choices[0].message.content

    return output


class GetProductRecommendation(BaseTool):
    """
    A tool that retrieves products from the database based on a user query by leveraging an AI agent to generate search queries.
    """

    product_category: str = Field(description="Product category")
    user_query: str = Field(description="User query")

    def run(self):
        return get_product_recommendation(self.product_category, self.user_query)
