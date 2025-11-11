def process_receipt(image,user_prompt):
    image_path = os.path.join(UPLOAD_DIR, "uploaded_receipt.png")
    image.save(image_path)
    system_prompt = """
               You are a specialist in comprehending receipts.
               Input images in the form of receipts will be provided to you,
               and your task is to respond to questions based on the content of the input image.
               """

    output = gemini_output(image_path, system_prompt, user_prompt)


    return output

# Gradio interface
import gradio as gr
with gr.Blocks() as app:
    gr.Markdown("## Receipt Data Extraction")
    gr.Markdown("Upload a receipt image and provide a custom prompt for extracting information.")

    with gr.Row():
        image_input = gr.Image(label="Upload Receipt Image", type="pil")
        user_prompt_input = gr.Textbox(label="User Prompt", placeholder="E.g., 'Convert invoice data to JSON format'")

    output_display = gr.Textbox(label="Output")
    submit_button = gr.Button("Process Receipt")
    submit_button.click(fn=process_receipt,
                        inputs=[image_input, user_prompt_input],
                        outputs=output_display)

app.launch(share=True)
