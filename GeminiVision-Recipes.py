import google.generativeai as genai
from pathlib import Path



import google.generativeai as genai
from pathlib import Path




# Insert your  API key here
api_key = ""
genai.configure(api_key=api_key)

# Configurations
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 8192,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Model Instance
model = genai.GenerativeModel(
    model_name="gemini-pro-vision",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

# Image Input Function
def input_image_setup(file_loc):
    if not (img := Path(file_loc)).exists():
        raise FileNotFoundError(f"Could not find image: {img}")

    image_parts = [{"mime_type": "image/jpeg", "data": Path(file_loc).read_bytes()}]
    return image_parts

# Response Function
def generate_gemini_response(input_prompt, image_loc, question_prompt):
    image_prompt = input_image_setup(image_loc)
    prompt_parts = [input_prompt, image_prompt[0], question_prompt]
    response = model.generate_content(prompt_parts)
    return response.text


input_prompt = """You are an cullinary expert and the best chef in the world who is known for giving detailed recipie instructions. provide recipes to users with the ingredients they have. give details instructions on how to prepare the dish
"""# change according to use case

image_loc = "food1.jpg"# image location

print("Fetching best recipes for you:")

question_prompt = "What are the different types of dishes i can prepare with this ingredients and give  very long detailed instruction"  # question to be asked to the image using Gemini Vision

result = generate_gemini_response(input_prompt, image_loc, question_prompt)

print(result)
