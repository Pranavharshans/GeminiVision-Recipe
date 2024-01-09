# Gemini Vision Recipe Generator

Gemini Vision Recipe Generator is a Python program that harnesses the power of Gemini Pro Vision and the Google GenerativeAI API to provide personalized recipe instructions based on culinary prompts and ingredient queries. The program excels in utilizing images to identify available ingredients, ensuring tailored recipe suggestions.

## Features

- **Gemini Pro Vision Integration**: Utilize Gemini Pro Vision for image-based culinary queries.
- **Ingredient-based Recipes**: Identify available ingredients from images and generate recipes accordingly.
- **GenerativeAI API**: Leverage the Google GenerativeAI API for advanced natural language generation.
- **Safety Settings**: Ensure content appropriateness with included safety settings.

## Usage

1. Acquire an API key 
2. Insert the obtained API key into the `api_key` variable in the `recipe_generator.py` file.
3. Customize the `input_prompt`, `image_loc`, and `question_prompt` variables based on your culinary needs.
4. Run the program:

    ```
    python recipe_generator.py
    ```



## How it Works

1. **Gemini Pro Vision**: The program uses Gemini Pro Vision to process images and extract information about available ingredients.
2. **GenerativeAI Recipe Generation**: Leveraging the GenerativeAI API, the program generates detailed recipe instructions based on culinary prompts and identified ingredients.

Feel free to explore and experiment with different culinary prompts, images, and questions to enhance your cooking experience!

