import tkinter as tk
from tkinter import scrolledtext
import openai

client = openai.OpenAI(api_key="sk-你的API金鑰")

def ask_gpt():
    question = entry.get()
    if not question.strip():
        return
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message.content
        output.config(state='normal')
        output.insert(tk.END, "🧑 你問了：" + question + "\n")
        output.insert(tk.END, "🤖 GPT 回答：\n" + answer + "\n\n")
        output.config(state='disabled')
        entry.delete(0, tk.END)
    except Exception as e:
        output.config(state='normal')
        output.insert(tk.END, f"❌ 發生錯誤：{str(e)}\n")
        output.config(state='disabled')

root = tk.Tk()
root.title("Thonny AI 小助手")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame, width=60)
entry.pack(side=tk.LEFT, padx=5)
ask_btn = tk.Button(frame, text="問 AI", command=ask_gpt)
ask_btn.pack(side=tk.LEFT)

output = scrolledtext.ScrolledText(root, width=80, height=20, state='disabled')
output.pack(padx=10, pady=10)

root.mainloop()
