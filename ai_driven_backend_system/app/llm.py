import time
import google.generativeai as genai
import typing_extensions as typing

# openai.api_key = "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"

GOOGLE_API_KEY = "AIzaSyCSGnOZFgFu4eerDCkM0GWKo2sFd3yQddw"

genai.configure(api_key=GOOGLE_API_KEY)

insert_prompts = [
    {
        "prompt": "Add a key-value pair with 'my.test' as the key and 'my.value' as the value",
        "content": """
            {
                "action": "Insert",
                "key": "my.test",
                "value": "my.value"
            }
        """
    },
    {
        "prompt": "Create a new entry using 'my.test' for the key and 'my.value' for the value",
        "content": """
            {
                "action": "Insert",
                "key": "my.test",
                "value": "my.value"
            }
        """
    },
    {
        "prompt": "Create a new entry using 'my.test' for the key and 'my.value' for the value",
        "content": """
            {
                "action": "Insert",
                "key": "my.test",
                "value": "my.value"
            }
        """
    },
    {
        "prompt": "Create a new entry using 'my.test' for the key and 'my.value' for the value",
        "content": """
            {
                "action": "Insert",
                "key": "my.test",
                "value": "my.value"
            }
        """
    },
    {
        "prompt": "Input a record where the key is 'my.test' and the corresponding value is 'my.value'",
        "content": """
            {
                "action": "Insert",
                "key": "my.test",
                "value": "my.value"
            }
        """
    },
    {
        "prompt": "Enter a new item with 'my.test' as its identifier and 'my.value' as its content",
        "content": """
            {
                "action": "Insert",
                "key": "my.test",
                "value": "my.value"
            }
        """
    },
    {
        "prompt": "Introduce an element with the key 'my.test' mapped to the value 'my.value'",
        "content": """
            {
                "action": "Insert",
                "key": "my.test",
                "value": "my.value"
            }
        """
    },
    {
        "prompt": "Store a new entry associating the key 'my.test' with the value 'my.value'",
        "content": """
            {
                "action": "Insert",
                "key": "my.test",
                "value": "my.value"
            }
        """
    },
    {
        "prompt": "Register 'my.test' as a key with its associated value 'my.value'",
        "content": """
            {
                "action": "Insert",
                "key": "my.test",
                "value": "my.value"
            }
        """
    },
    {
        "prompt": "Append a new key-value combination: 'my.test' paired with 'my.value'",
        "content": """
            {
                "action": "Insert",
                "key": "my.test",
                "value": "my.value"
            }
        """
    },
    {
        "prompt": "Include a new record consisting of the key 'my.test' and value 'my.value'",
        "content": """
            {
                "action": "Insert",
                "key": "my.test",
                "value": "my.value"
            }
        """
    },
    {
        "prompt": "Set up an entry where 'my.test' serves as the key and 'my.value' as its corresponding value",
        "content": """
            {
                "action": "Insert",
                "key": "my.test",
                "value": "my.value"
            }
        """
    },
    {
        "prompt": "Put in a new item with 'my.test' acting as the key and 'my.value' as the associated value",
        "content": """
            {
                "action": "Insert",
                "key": "my.test",
                "value": "my.value"
            }
        """
    },
    {
        "prompt": "Log a new entry pairing the key 'my.test' with the value 'my.value'",
        "content": """
            {
                "action": "Insert",
                "key": "my.test",
                "value": "my.value"
            }
        """
    },
]

update_prompts = [
    {
        "prompt": "Update the value of key 'my.test' to 'my.new.value'",
        "content": """
            {
                "action": "Update",
                "key": "my.test",
                "value": "my.new.value"
            }
        """
    },
    {
        "prompt": "Modify the entry with key 'my.test' to have the value 'my.new.value'",
        "content": """
            {
                "action": "Update",
                "key": "my.test",
                "value": "my.new.value"
            }
        """
    },
    {
        "prompt": "Change the value associated with key 'my.test' to 'my.new.value'",
        "content": """
            {
                "action": "Update",
                "key": "my.test",
                "value": "my.new.value"
            }
        """
    },
    {
        "prompt": "Revise the 'my.test' key's value to 'my.new.value'",
        "content": """
            {
                "action": "Update",
                "key": "my.test",
                "value": "my.new.value"
            }
        """
    },
    {
        "prompt": "Alter the existing entry for 'my.test', setting its value to 'my.new.value'",
        "content": """
            {
                "action": "Update",
                "key": "my.test",
                "value": "my.new.value"
            }
        """
    },
    {
        "prompt": "Overwrite the value of key 'my.test' with 'my.new.value'",
        "content": """
            {
                "action": "Update",
                "key": "my.test",
                "value": "my.new.value"
            }
        """
    },
    {
        "prompt": "Replace the current value of 'my.test' with 'my.new.value'",
        "content": """
            {
                "action": "Update",
                "key": "my.test",
                "value": "my.new.value"
            }
        """
    },
    {
        "prompt": "Adjust the value linked to key 'my.test' to be 'my.new.value'",
        "content": """
            {
                "action": "Update",
                "key": "my.test",
                "value": "my.new.value"
            }
        """
    },
    {
        "prompt": "Refresh the entry for 'my.test' with the new value 'my.new.value'",
        "content": """
            {
                "action": "Update",
                "key": "my.test",
                "value": "my.new.value"
            }
        """
    },
    {
        "prompt": "Set the new value 'my.new.value' for the existing key 'my.test'",
        "content": """
            {
                "action": "Update",
                "key": "my.test",
                "value": "my.new.value"
            }
        """
    },
    {
        "prompt": "Reassign the value of key 'my.test' to 'my.new.value'",
        "content": """
            {
                "action": "Update",
                "key": "my.test",
                "value": "my.new.value"
            }
        """
    },
]

delete_prompts = [
    {
        "prompt": "Remove the entry for 'my.test'",
        "content": """
            {
                "action": "Delete",
                "key": "my.test",
                "value": ""
            }
        """
    },
    {
        "prompt": "Delete 'my.test' from the list",
        "content": """
            {
                "action": "Delete",
                "key": "my.test",
                "value": ""
            }
        """
    },
    {
        "prompt": "Eliminate 'my.test' from the database",
        "content": """
            {
                "action": "Delete",
                "key": "my.test",
                "value": ""
            }
        """
    },
    {
        "prompt": "Erase 'my.test' from the system",
        "content": """
            {
                "action": "Delete",
                "key": "my.test",
                "value": ""
            }
        """
    },
]

few_shot_prompt = """
    Parse a user's instruction into valid JSON:

    EXAMPLE:
    Add a key-value pair with 'my.test' as the key and 'my.value' as the value
    JSON Response:
    ```
    {
        "action": "Insert",
        "key": "my.test",
        "value": "my.value"
    }
    ```

    EXAMPLE:
    Update the value of key 'my.test' to 'my.new.value'
    JSON Response:
    ```
    {
        "action": "Update",
        "key": "my.test",
        "value": "my.new.value"
    }
    ```

    EXAMPLE:
    Remove the entry for 'my.test'
    JSON Response:
    ```
    {
        "action": "Delete",
        "key": "my.test",
        "value": ""
    }
    ```
"""

class Schema(typing.TypedDict):
    action: str
    key: str
    value: str | None = ""

def parse_from_llm(user_query: str):
    model = genai.GenerativeModel(
        'gemini-1.5-flash-latest',
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json",
            response_schema=Schema,
        ))
    
    # response = model.generate_content([few_shot_prompt, user_query])
    response = model.generate_content([user_query])
    print(response.text)

    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",  # Use gpt-3.5-turbo or gpt-4
    #     messages=messages,
    #     max_tokens=50,  # Adjust as needed
    #     temperature=0  # Lower temperature for more deterministic results
    # )

    # print(response['choices'][0]['message']['content'].strip())

current_time = time.time()
parse_from_llm("Insert key: 1 whose value: 2")
print(time.time() - current_time)