import os
from ollama import generate


# input file is in data folder with name groceries.txt
input_file = os.path.join('data', 'groceries.txt')
output_file = os.path.join('data', 'categorized_groceries.txt')

model = 'llama3.2'

if not os.path.exists(input_file):
    print(f'File {input_file} not found')
    exit(1)

with open(input_file, 'r') as f:
    groceries = f.read().strip()


prompt = f"""
You are a grocery categorization assistant. Your task is to organize an uncategorized list of grocery items into logical and meaningful categories.

Here is the uncategorized list of groceries:
{groceries}

Instructions:
1. Categorize Items Dynamically: Group items into categories that are logical based on the list provided. Use common categories when they apply (e.g., Produce, Dairy, Meat, Condiments, Personal Care), but feel free to create new, contextually appropriate categories if needed.
2. Avoid Redundancy: Ensure that each item is assigned to only one category.
3. Sort Alphabetically: Within each category, list items in alphabetical order.
4. Exclude Empty Categories: Do not create categories that have no items.
5. Concise Output: Format the response to include only the category name followed by the list of items. Do not include additional text, explanations, or metadata in your response.
"""

response = generate(model=model, prompt=prompt, options=dict(temperature=0.4) )

categorized_groceries = response.response

with open(output_file, 'w') as f:
    f.write(categorized_groceries)

print(f'Groceries categorized and saved to {output_file}')
print(categorized_groceries)