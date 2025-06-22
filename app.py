import gradio as gr
import random

def generate_random_number():
    return f"Random: {random.randint(1, 1000)}"

with gr.Blocks() as demo:
    output = gr.Markdown()
    demo.load(fn=generate_random_number, inputs=None, outputs=output, every=5)

demo.launch(server_name="0.0.0.0")