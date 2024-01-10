from openai import OpenAI

system_message = "Your system message here."


def query_model(prompt, system_message):
    client = OpenAI(api_key="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")
    response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0613:personal::8fOMgPCA",  # Replace with your actual model name
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
