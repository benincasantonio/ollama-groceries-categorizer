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
You are a grocery categorization assistant. Your role is to organize an uncategorized list of groceries into logical and meaningful categories.

Instructions:
1. Organize the given items into generic categories that make sense like Produce, Dairy, Meat, Frozen, Beverages, Personal Care, Pet Food etc. Make sure to create new categories if needed.
2. Ensure items appear in only one category.
3. Ensure that items within each category are alphabetically ordered.

Here is the uncategorized list of groceries:
{groceries}
"""

response = generate(model=model, prompt=prompt)

categorized_groceries = response.response

with open(output_file, 'w') as f:
    f.write(categorized_groceries)

print(f'Groceries categorized and saved to {output_file}')
print(categorized_groceries)