from os import getenv
from openai import OpenAI

# Ключ читаємо з змінної середовища
client = OpenAI(api_key=getenv("OPENAI_API_KEY"))

resp = client.chat.completions.create(
    model="gpt-4o-mini",  # легка, дешева модель для старту
    messages=[
        {"role": "user", "content": "Привіт! Скажи, що це тест з мого локального проєкту."}
    ]
)

print(resp.choices[0].message.content)
