from transformers import pipeline
from PIL import Image

def generate_caption(image_path):
    """
    Generates a caption for a given image using a pre-trained model.
    """
    try:
        # Load the pre-trained image-captioning model from Hugging Face
        # The first time you run this, it will download the model (it's a few GBs)
        captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

        # Open the image file
        image = Image.open(image_path)
        
        # Generate the caption
        result = captioner(image)
        
        # The result is a list of dictionaries, we extract the caption text
        caption = result[0]['generated_text']
        
        return caption

    except FileNotFoundError:
        return f"Error: The file '{image_path}' was not found."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # IMPORTANT: Replace "dog_on_beach.jpg" with the actual path to your image file
    image_file = "dog_on_beach.jpg" 
    
    print(f"Analyzing '{image_file}'...")
    
    # Generate the caption and print it
    generated_caption = generate_caption(image_file)
    
    print("\n✨ AI-Generated Caption:")
    print(generated_caption)