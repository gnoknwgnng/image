import streamlit as st
import requests
import base64
import json
from PIL import Image
import io

# Function to get objects from Google Lens API (Placeholder, you need to replace with actual API call)
def get_objects_from_image(image_data):
    # This is a placeholder function. Replace with actual Google Lens API call.
    objects = ["cat", "tree", "sun"]  # Dummy objects for testing
    return objects

# Function to generate story using Gemini API
def generate_story(objects):
    api_key = "AIzaSyAdUgcDM3IAsgb_Q_8a9m-iIXg3p35VR48"  # Replace with your Gemini API key
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateText?key={api_key}"
    headers = {"Content-Type": "application/json"}
    prompt = f"Write a short story including these objects: {', '.join(objects)}."
    data = {"prompt": prompt, "max_tokens": 100}
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        try:
            response_data = response.json()
            return response_data.get("choices", [{}])[0].get("text", "No story generated.")
        except json.JSONDecodeError:
            return "Error parsing response."
    else:
        return f"Error {response.status_code}: {response.text}"

# Streamlit UI
st.title("AI Story Generator from Images")
st.write("Upload an image, and AI will generate a story based on detected objects.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Convert image to bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format=image.format)
    img_bytes = img_bytes.getvalue()
    
    # Detect objects (Replace with actual API call)
    objects = get_objects_from_image(img_bytes)
    st.write("Objects detected:", objects)
    
    # Generate Story
    if objects:
        story = generate_story(objects)
        st.subheader("Generated Story:")
        st.write(story)
    else:
        st.write("No objects detected in the image.")
