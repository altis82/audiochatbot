import openai

openai.api_type = "azure"
openai.api_key = "token"
openai.api_base = "url"
openai.api_version = "2023-03-15-preview"
# Use ChatCompletion for generating responses
def chatgpt(text):
    response = openai.ChatCompletion.create(
        engine="gpt-4",
        messages=[
            {"role": "user", "content": text}
        ]
    )

    # Print the response
    output=response.choices[0].message['content'].strip()
    print(output)
    return output

chatgpt("hello world")