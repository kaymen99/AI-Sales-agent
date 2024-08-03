import os
import requests
from pydantic import Field
from .base_tool import BaseTool

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

class GenerateCalendlyInvitationLink(BaseTool):
    """
    A tool that generate a calendly invitation link for a customer based on a single query string.
    """
    query: str = Field(description='Query string')

    def run(self):
        return generate_calendly_invitation_link(self.query)