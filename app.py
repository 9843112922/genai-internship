from groq import Groq

client = Groq(
    api_key="API-KEY"
)

question = input("Ask something: ")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": question,
        }
    ],
    model="llama-3.1-8b-instant",
)

print("\nAI Answer:")
print(chat_completion.choices[0].message.content)
