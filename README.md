<!--
Title: AI Sales Agent for Computer Equipment Ecommerce | Automated Customer Engagement & Sales
Description: Enhance your computer equipment Ecommerce with an AI sales agent. Automate customer engagement, product recommendations, consultation scheduling, and Stripe payment facilitation.
Keywords: AI Sales Agent, Ecommerce, Customer Support and assistance, Product Recommendations, Consultation Scheduling, Stripe Payments, AI Automated Sales, Python, AI Agents, AI Tools, Calendly Integration.
Author: kaymen99
-->

<meta name="title" content="AI Sales Agent for Computer Equipment Ecommerce Store | AI Automated Customer Sales">
<meta name="description" content="Enhance your Ecommerce store with an AI sales agent. Automate customer assistance and support, product recommendations, Calendly consultation scheduling, and Stripe payment facilitation.">
<meta name="keywords" content="AI Sales Agent, Ecommerce, Customer Support and assistance, Product Recommendations, Consultation Scheduling, Stripe Payments, AI Automated Sales, Python, AI Agents, AI Tools, Calendly Integration">
<meta name="author" content="kaymen99">

# AI Sales Agent

I built an AI sales agent for a computer equipement Ecommerce website, the agent will streamline the customer engagement and sales processes, by automating the process of providing **product recommendations**, **answering customers enquires**, **scheduling consultations**, and facilitating **purchases through Stripe**.

<br/>
<p align="center">
  <img src="https://github.com/user-attachments/assets/c59e4b71-fd5f-4713-9097-0c076e54afa2" alt="AI Sales agent flowchart">
</p>

## Features

- **Customer Engagement**: Interact with customers in a friendly and professional manner, offering accurate information about products and services.
- **Product Recommendations**: Provide personalized product suggestions based on customer needs and preferences.
- **Consultation Scheduling**: Schedule consultations with tech experts for complex inquiries.
- **Purchase Facilitation**: Facilitate payments with Stripe by generating payment links for customers ready to buy, ensuring a smooth transaction process.

### Agent Tools

- **get_store_info**: This leverages RAG search to retrieve general information about the TechNerds business, services, and products. All informations are retrieved from the docs `files/Docs.txt`.
- **get_product_recommendation**: Uses an expert product recommendation agent to find the best products the store can offer based on customer requirements.
- **generate_calendly_invitation_link**: Provide a link for scheduling a consultation with a tech expert through Calendly.
- **generate_stripe_payment_link**: Create a Stripe payment link for customer purchases.

## How to Run

### Prerequisites

- Python 3.9+
- Calendly API key
- Stripe API key
- Groq API key
- Necessary Python libraries (listed in `requirements.txt`)

### Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/kaymen99/ai-sales-agent.git
   cd ai-sales-agent/website-sale-agent
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory of the project and add your API keys:

   ```env
   CALENDLY_API_KEY=your_calendly_api_key
   CALENDLY_EVENT_TYPE_UUID=your_calendly_event_id
   STRIPE_API_KEY=your_stripe_api_key
   GROQ_API_KEY=your_stripe_api_key
   ```

### Running the Application

1. To run the project, you must first create the products database (unless you have one already) by executing:

   ```sh
   python create_database.py
   ```

2. **Then start the Sales bot by running:**

   ```sh
   python main.py
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Contact

If you have any questions or suggestions, feel free to contact me at `aymenMir1001@gmail.com`.
