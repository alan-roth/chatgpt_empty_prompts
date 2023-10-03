import openai

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUR_API_KEY'


# Initialize the OpenAI API client
openai.api_key = api_key

# Start a new conversation
conversation = [
    {"role": "user", "content": ""}
]

# Generate a response from ChatGPT-3.5 for the first user message
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation
)

# Extract and print the assistant's reply for the first turn
assistant_reply = response['choices'][0]['message']['content']
conversation.append({"role": "assistant", "content": assistant_reply})
print("Assistant:", assistant_reply)
