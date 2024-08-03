import stripe
import os, sqlite3
from pydantic import Field
from .base_tool import BaseTool


def generate_stripe_payment_link(name: str, price: float, quantity: int) -> str:
    # Stripe API key
    stripe.api_key = os.getenv("STRIPE_API_KEY")
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

    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": price_id, "quantity": 1}],
        mode="payment",
    )
    return session.url


class GenerateStripePaymentLink(BaseTool):
    """
    A tool that generate a stripe payment link for a customer based on a single query string.
    """

    name: str = Field(description="Name of the product")
    price: float = Field(description="Price of the product")
    quantity: int = Field(description="Quantity of the product")

    def run(self):
        return generate_stripe_payment_link(self.name, self.price, self.quantity)
