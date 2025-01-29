# !pip install openai
# user --upgrade to retrieve newer version if needed

from openai import OpenAI
import os

# A recommended way to store the key is in the environment variable. For this demo, it is in a file.
key_location = r'C:\Users\vange\Workspace_JLAB\GenAI\GenAIkey.txt'

with open(key_location, 'r') as file:
    key = file.readline().strip()

client = OpenAI(api_key=key)

# Set the prompt
prompt = "To succeed in life"

# Note: completion is legacy, but i still wanted to show you.

# Set the completion parameters
completion_params = {
    "model": "davinci-002",
    "prompt": prompt,
    "max_tokens": 50 #maximum number of tokens for the completion
}

# Call the OpenAI API to generate a completion
response = client.completions.create(**completion_params)

# Extract the generated completion from the API response
completion_text = response.choices[0].text.strip()

print(response)

# Set parameters
conversation = [
    {"role": "user", "content": "How can I succeed in life?"}
]

# Create a chat completion and invoke it
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=conversation
)

# Extract and print the reply
reply = response.choices[0].message

print(reply)
