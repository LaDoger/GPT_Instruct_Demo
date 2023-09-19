import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = input('>>> Your Insturctions: (e.g. write a haiku)\n')

print('>>> AI Completion:')

completion = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    max_tokens=4000
)

print(completion.choices[0].text.strip())