from dotenv import load_dotenv

load_dotenv()
import openai
import json


def find_product(sql_query):
    # Execute query here
    results = [
        {"name": "pen", "color": "blue", "price": 1.99},
        {"name": "pen", "color": "red", "price": 1.78},
    ]
    return results


functions = [
    {
        "name": "find_product",
        "description": "Get a list of products from a sql query",
        "parameters": {
            "type": "object",
            "properties": {
                "sql_query": {
                    "type": "string",
                    "description": "A SQL query",
                }
            },
            "required": ["sql_query"],
        },
    }
]


def run(user_question):
    # Send the question and available functions to GPT
    messages = [{"role": "user", "content": user_question}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613", messages=messages, functions=functions
    )
    response_message = response["choices"][0]["message"]

    # Append the assistant's response to the messages
    print(response_message)
    messages.append(response_message)
    

    # Call the function and add the results to the messages
    if response_message.get("function_call"):
        function_name = response_message["function_call"]["name"]
        if function_name == "find_product":
            function_args = json.loads(
                response_message["function_call"]["arguments"]
            )
            products = find_product(function_args.get("sql_query"))
        else:
            # Handle error
            products = []
        # Append the function's response to the messages
        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": json.dumps(products),
            }
        )
        # Get a new response from GPT so it can format the function's response into natural language
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )
        return second_response


print(run("I need the top 2 products where the price is less than 2.00"))
