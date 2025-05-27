import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def get_chat_completion(user_input):
    system_prompt = "You are a helpful assistant that provides clear and concise responses."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    assistant_response = response.choices[0].message.content
    total_tokens = response.usage.total_tokens
    
    return assistant_response, total_tokens

def main():
    user_input = input("\nEnter your query: ")
    response, tokens = get_chat_completion(user_input)
    print("\nAssistant's response:")
    print(response)
    print(f"\nTotal tokens used: {tokens}")

if __name__ == "__main__":
    main()
