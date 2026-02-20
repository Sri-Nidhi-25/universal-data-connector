import json
import os
from typing import cast
from dotenv import load_dotenv
from groq import Groq
from groq.types.chat import ChatCompletionToolParam, ChatCompletionMessageParam
from app.connectors.crm_connector import CRMConnector
from app.connectors.support_connector import SupportConnector
from app.connectors.analytics_connector import AnalyticsConnector

load_dotenv()

# class LLMService:
#     def __init__(self):
#         self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#     def chat(self, message: str):
#         response = self.client.chat.completions.create(
#             model="llama-3.1-8b-instant",  # fast + free tier friendly
#             messages=[
#                 {"role": "system", "content": "Be concise and clear."},
#                 {"role": "user", "content": message}
#             ],
#             temperature=0.3,
#             max_tokens=200
#         )

#         return response.choices[0].message.content
TOOLS: list[ChatCompletionToolParam] = [
    {
        "type": "function",
        "function": {
            "name": "get_crm_data",
            "description": "Fetch CRM customer data",
            "parameters": {
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "integer",
                        "description": "Number of customers to return"
                    }
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_support_data",
            "description": "Fetch support ticket data",
            "parameters": {
                "type": "object",
                "properties": {
                    "limit": {
                        "type": "integer"
                    }
                }
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_analytics_data",
            "description": "Fetch analytics metrics",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    }
]

class LLMService:

    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.crm = CRMConnector()
        self.support = SupportConnector()
        self.analytics = AnalyticsConnector()

    def _apply_business_rules(self, data):
        """Apply business rules to transform data"""
        # Add your business logic here
        return data

    def _optimize_for_voice(self, data):
        """Optimize data for voice output"""
        # Add voice optimization logic here
        return data

    def process_message(self, user_message: str) -> str:

        # First LLM call (with tools enabled)
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a SaaS data assistant."},
                {"role": "user", "content": user_message}
            ],
            tools=TOOLS,
            tool_choice="auto"
        )

        message = response.choices[0].message
        # cast the object into the param type accepted by `create`
        message_param = cast(ChatCompletionMessageParam, message)

        # If no tool was called → return normal reply
        if not message.tool_calls:
            return message.content or ""

        # If tool was called
        tool_call = message.tool_calls[0]
        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments or "{}")

        # Route to correct connector
        data = self._execute_tool(function_name, arguments)

        # Apply business logic
        data = self._apply_business_rules(data)
        data = self._optimize_for_voice(data)

        # Second LLM call (with tool result)
        final_response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a SaaS data assistant."},
                {"role": "user", "content": user_message},
                message_param,
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(data)
                }
            ]
        )

        return final_response.choices[0].message.content or ""
    

    def _execute_tool(self, function_name: str, arguments: dict):

        if function_name == "get_crm_data":
            return self.crm.fetch(limit=arguments.get("limit", 10))

        elif function_name == "get_support_data":
            return self.support.fetch(limit=arguments.get("limit", 10))

        elif function_name == "get_analytics_data":
            return self.analytics.fetch()

        else:
            raise ValueError(f"Unknown tool: {function_name}")