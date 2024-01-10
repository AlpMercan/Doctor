from openai import OpenAI


def query_model(prompt, system_message):
    client = OpenAI(api_key="Your Key")
    response = client.chat.completions.create(
        model="YourModel",  # Replace with your actual model name
        messages=[
            {
                "role": "system",
                "content": system_message,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    return response.choices[0].message.content.strip()


def main():
    system_message = (
        "Your system message here."  # Replace with your system message if you have one
    )
    user_input = input("Enter your prompt: ")
    response = query_model(user_input, system_message)
    print("Model response:", response)


if __name__ == "__main__":
    main()
