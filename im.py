import requests
import json
import streamlit as st

# Set up API details
HUGGINGFACE_API_KEY = "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"  # Replace with your Hugging Face API key
MODEL = "meta-llama/Llama-2-7b-chat-hf"  # Changed to LLaMA 2
API_URL = f"https://api-inference.huggingface.co/models/{MODEL}"

headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

# Streamlit UI
st.title("Image Object Story Generator")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Display image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Simulating object detection (Replace this with actual detection)
    detected_objects = ["cat", "tree", "sun"]
    st.write("**Objects detected:**", detected_objects)

    # Convert detected objects into a story prompt
    story_prompt = f"Write a short creative story including {', '.join(detected_objects)}."

    # Call Hugging Face API
    response = requests.post(API_URL, headers=headers, json={"inputs": story_prompt})

    if response.status_code == 200:
        result = response.json()
        if isinstance(result, list) and "generated_text" in result[0]:
            story = result[0]["generated_text"]
            st.write("## Generated Story:")
            st.write(story)
        else:
            st.write("**Error:** Unexpected response format from the model.")
    else:
        st.write(f"**Error {response.status_code}:** {response.text}")
