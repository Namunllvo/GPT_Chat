import openai

openai.api_key = ""
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="""Fix grammar errors:
    -Is They got a boys
    -You are a girl""".strip(),
)

print(response)
print(response.choices[0].text.strip())

response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {"role":"system", "content": "당신은 지식이 풍부한 교수입니다."},
        {"role":"user", "content": "서울의 수도는 어디인가요?"}
    ]
)
print(response)
print(response["choices"][0]["message"]["content"])