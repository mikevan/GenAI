import os
import requests
import json


# A recommended way to start the key is in an environment variable. For this demo, I'm storing it in a file.
key_location = r'C:\Users\vange\Workspace_JLAB\GenAI\GenAIkey.txt'

with open(key_location, 'r') as file:
    key = file.readline().strip()

prompt = "To succeed in life"

# Set the endpoint for GPT-3.5 chat completions
endpoint = "https://api.openai.com/v1/chat/completions"

# Look out for drecations
# Endpoint = "https://api.openai.com/v1/engines/gpt-3.5-turbo-instruct/completions"

# Set headers (include your API key for authentication
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {key}"
}

# Set the parameters

max_tokens = 50

# Construct the request payload
payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": prompt}],
    "max_tokens": max_tokens
}

# Make the API request
response = requests.post(endpoint, headers=headers, json=payload)

#Extract the generated completion from the API response
completion_text = response.json()["choices"][0]["message"]["content"].strip()

# Print the generated completion
print("Generated completion for prompt '" + prompt + "'\n" + completion_text)

print(json.dumps(response.json(), indent=2))