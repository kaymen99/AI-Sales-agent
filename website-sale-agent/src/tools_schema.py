tools = [
    {
        "type": "function",
        "function": {
            "name": "get_store_info",
            "description": "Retrieve detailed information about TechNerds' business, services, and products based on the provided query.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "A query used to search for specific information about TechNerds. This could include business details, services offered, or product information."
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_product_recommendation",
            "description": "Retrieve product recommendation from our computer equipement expert based on the user requirements and the product category.",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_category": {
                        "type": "string",
                        "description": "The category of the product you want to find."
                    },
                    "user_query": {
                        "type": "string",
                        "description": "A query used to search for specific information about the product or service."
                    }
                },
                "required": ["product_category", "user_query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "generate_calendly_invitation_link",
            "description": "Generate a Calendly invitation link based on the single query string.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The query string representing the invite subject."
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "send_email",
            "description": "Send an email",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The query string representing the invite subject."
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "generate_stripe_payment_link",
            "description": "Generate a Stripe payment link based on the single query string.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The name of the product or service."
                    },
                    "price": {
                        "type": "number",
                        "description": "The price of the product or service."
                    },
                    "quantity": {
                        "type": "number",
                        "description": "The quantity of the product or service."
                    }
                },
                "required": ["name", "price", "quantity"]
            }
        }
    }
]