import gradio

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [{"role": "system", "content": "You area financial experts that specialize in real estate investment and negotiation"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = client.chat.completions.create(
         model="gpt-4o-mini",
         messages = messages
    )
    
    ChatGPT_reply = response.choices[0].message.content

    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs= "text", outputs = "text", title= "My saveing Assistant")

demo.launch(share=True)