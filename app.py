from transformers import pipeline
import gradio as gr

summarization_pipeline = pipeline("summarization")


def summarize_text(input_text):
    summary = summarization_pipeline(input_text)[0]["summary_text"]
    return summary


with gr.Blocks() as application_ui:
    source_text = gr.Textbox(placeholder="Enter text block to summarize", lines=4)
    gr.Interface(fn=summarize_text, inputs=source_text, outputs="text")

if __name__ == "__main__":
    application_ui.launch(share=True)
