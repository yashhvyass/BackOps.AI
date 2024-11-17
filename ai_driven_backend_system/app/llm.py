# import json
# import google.generativeai as genai
# import typing_extensions as typing

# GOOGLE_API_KEY = "AIzaSyCSGnOZFgFu4eerDCkM0GWKo2sFd3yQddw"

# genai.configure(api_key=GOOGLE_API_KEY) 

# few_shot_prompt = """
#     Parse a user's instruction into valid JSON:

#     EXAMPLE:
#     Add a key-value pair with 'my.test' as the key and 'my.value' as the value
#     JSON Response:
#     ```
#     {
#         "action": "Insert",
#         "key": "my.test",
#         "value": "my.value"
#     }
#     ```

#     EXAMPLE:
#     Update the value of key 'my.test' to 'my.new.value'
#     JSON Response:
#     ```
#     {
#         "action": "Update",
#         "key": "my.test",
#         "value": "my.new.value"
#     }
#     ```

#     EXAMPLE:
#     Remove the entry for 'my.test'
#     JSON Response:
#     ```
#     {
#         "action": "Delete",
#         "key": "my.test",
#         "value": ""
#     }
#     ```
# """

# class Schema(typing.TypedDict):
#     action: str
#     key: str
#     value: str | None = ""

# def parse_from_llm(user_query: str):
#     model = genai.GenerativeModel(
#         'gemini-1.5-flash-latest',
#         generation_config=genai.GenerationConfig(
#             response_mime_type="application/json",
#             response_schema=Schema,
#         ))

#     response = model.generate_content([user_query])

#     return json.loads(response.text)

import json
from openai import OpenAI

OpenAI_API_KEY = "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"

client = OpenAI(api_key=OpenAI_API_KEY)

user_request = "Make an entry to my table with key 'name' and value is 'dhruv'. Also remove data with key 'email' and value 'dgb@gmail.com'. also change my existing name from dhruv to dev"

def parse_from_llm(user_request):
    # Call OpenAI API
    completion = client.chat.completions.create(
        model="gpt-4o-2024-05-13",
        messages=[
            {
                "role": "user",
                "content": "You are an assistant that parses natural language requests into structured JSON for backend operations. "
                           "Here are some examples:\n\n"
                           "Example 1:\n"
                           "Input: \"Insert an entry with key 'user.name' and value 'John Doe'.\"\n"
                           "Output: [{\n"
                           "    \"action\": \"insert\",\n"
                           "    \"key\": \"user.name\",\n"
                           "    \"value\": \"John Doe\"\n"
                           "}]\n\n"
                           "Example 2:\n"
                           "Input: \"Update the value of key 'project.status' to 'completed'.\"\n"
                           "Output: [{\n"
                           "    \"action\": \"update\",\n"
                           "    \"key\": \"project.status\",\n"
                           "    \"value\": \"completed\"\n"
                           "}]\n\n"
                           "Example 3:\n"
                           "Input: \"Delete the entry with key 'session.id'.\"\n"
                           "Output: [{\n"
                           "    \"action\": \"delete\",\n"
                           "    \"key\": \"session.id\",\n"
                           "    \"value\": null\n"
                           "}]"
            },
            {
                "role": "user",
                "content": f"Input: \"{user_request}\""
            }
        ]
    )
    # Return the structured JSON from the API response
    response_text=completion.choices[0].message.content

    cleaned_response = response_text.strip().replace("```json", "").replace("```", "").strip()

    try:
        response_json = json.loads(cleaned_response)  # Parse the string as a JSON list
        return response_json
    except json.JSONDecodeError as e:
        raise e
    
# print(parse_from_llm("Insert key: Dev with value: Patel. Update key: Dev with value: Ashishkumar"))