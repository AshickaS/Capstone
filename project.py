import openai

def generate_response(query):
    client = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[{"role": "user", "content": query}],
    )
    return client.choices[0].message["content"].strip()