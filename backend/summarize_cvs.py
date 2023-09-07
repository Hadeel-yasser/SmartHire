import os
import openai
openai.api_type = "azure"
openai.api_version = "2023-05-15" 
openai.api_base = os.getenv(" https://trippee.openai.azure.com")  # Your Azure OpenAI resource's endpoint value.
openai.api_key = "1b9551b253a44d549f9f610a17dc2e22"
#openai.api_key = os.getenv("1b9551b253a44d549f9f610a17dc2e22")

response = openai.ChatCompletion.create(
    engine="gpt-35-turbo", # The deployment name you chose when you deployed the GPT-35-Turbo or GPT-4 model.
    messages=[
        {"role": "system", "content": "Assistant is an intelligent chatbot designed to help users answer their tax related questions."
"Instructions: "
"- Only answer questions related to taxes. "
"- If you're unsure of an answer, you can say 'I donot know' or 'I am not sure' and recommend users go to the IRS website for more information. "},
{"role": "user", "content": "When are my taxes due?"}
    ]
)

print(response)

print(response['choices'][0]['message']['content'])