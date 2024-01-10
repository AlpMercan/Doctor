import tkinter as tk
from tkinter import scrolledtext, font
from openai import OpenAI


def query_model(prompt, system_message):
    client = OpenAI(api_key="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")
    response = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0613:personal::8fOMgPCA",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content.strip()


def count_tokens(text):
    return len(text.split())


def get_response():
    user_input = user_input_txt.get("1.0", tk.END).strip()
    tokens = count_tokens(user_input)
    token_count_var.set(f"Estimated tokens: {tokens}")
    response = query_model(user_input, system_message)
    response_txt.delete("1.0", tk.END)
    response_txt.insert(tk.END, response)


# GUI setup
window = tk.Tk()
window.title("OpenAI Model Query")
window.geometry("600x400")
system_message = "Your system message here."
# Styling
font_title = font.Font(family="Helvetica", size=12, weight="bold")
font_text = font.Font(family="Helvetica", size=10)
padding = {"padx": 10, "pady": 5}
bg_color = "#f0f0f0"
window.configure(bg=bg_color)

# Configure grid
window.columnconfigure(0, weight=1)
for i in range(5):
    window.rowconfigure(i, weight=1)

# User input label
user_input_lbl = tk.Label(
    window, text="Enter your prompt:", font=font_title, bg=bg_color
)
user_input_lbl.grid(row=0, column=0, sticky="nsew", **padding)

# User input text area
user_input_txt = scrolledtext.ScrolledText(window, height=10, font=font_text)
user_input_txt.grid(row=1, column=0, sticky="nsew", **padding)

# Token count label
token_count_var = tk.StringVar()
token_count_lbl = tk.Label(
    window, textvariable=token_count_var, bg=bg_color, font=font_text
)
token_count_lbl.grid(row=2, column=0, sticky="nsew", **padding)

# Response label
response_lbl = tk.Label(window, text="Model response:", font=font_title, bg=bg_color)
response_lbl.grid(row=3, column=0, sticky="nsew", **padding)

# Response text area
response_txt = scrolledtext.ScrolledText(window, height=10, font=font_text)
response_txt.grid(row=4, column=0, sticky="nsew", **padding)

# Query button
query_btn = tk.Button(window, text="Get Response", command=get_response, font=font_text)
query_btn.grid(row=5, column=0, sticky="nsew", **padding)

window.mainloop()
