from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse # Import FileResponse
from PIL import Image
from transformers import pipeline
import io

# Create an instance of the FastAPI class
app = FastAPI(title="Project Visionary API")

# Load the AI model once when the application starts
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

def generate_caption(image_bytes):
    """
    Generates a caption for a given image in bytes.
    """
    try:
        # Open the image from bytes
        image = Image.open(io.BytesIO(image_bytes))
        
        # Generate the caption
        result = captioner(image)
        
        # Extract the caption text
        caption = result[0]['generated_text']
        return caption
        
    except Exception as e:
        return f"An error occurred: {e}"

@app.post("/analyze/")
async def analyze_image(file: UploadFile = File(...)):
    """
    This endpoint receives an image, generates a caption, and returns it.
    """
    # Read the content (bytes) of the uploaded file
    image_bytes = await file.read()
    
    # Generate the caption from the image bytes
    caption = generate_caption(image_bytes)
    
    # Return the filename and the generated caption
    return {"filename": file.filename, "caption": caption}

@app.get("/")
async def read_root():
    # Return the HTML file as the response for the root URL
    return FileResponse('index.html')