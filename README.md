# AI Grocery Categorizer

A small AI agent designed to automatically categorize a list of groceries. This project was created as part of my journey learning AI development using Ollama. Inspired by [this tutorial video](https://youtu.be/GWB9ApTPTv4?si=Fqzjl97_90uSWh-2) while learning AI and Ollama, this project explores the application of AI to solve everyday problems.

---

## Features
- **Efficient Categorization**: Automatically groups grocery items into predefined categories.
- **File Input and Output**: Reads grocery items from `groceries.txt` and saves categorized items to `categorized_groceries.txt` in the `data` folder.
- **Educational Focus**: Created as a learning project while exploring Ollama's capabilities.

---

## Table of Contents
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Examples](#examples)
- [Tech Stack](#tech-stack)
- [License](#license)

---

## Getting Started

### Prerequisites
- Python 3.8+
- [Ollama](https://www.ollama.com/) installed and configured

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/benincasantonio/ollama-groceries-categorizer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ollama-groceries-categorizer
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Ensure Ollama is running on your local machine.

---

## Usage
1. Prepare an input file:
   - Add uncategorized grocery items, one per line, in the `data/groceries.txt` file.

2. Run the script:
   ```bash
   python app.py
   ```

3. View results:
   - Categorized items will appear in the console.
   - The categorized list will be saved to `data/categorized_groceries.txt`.

### Example Input File (`groceries.txt`)
```
Milk
Bread
Apples
Chicken
Shampoo
```

### Example Output File (`categorized_groceries.txt`)
```
Dairy:

    Milk

Meat:

    Chicken

Produce:

    Apples

Personal Care:

    Shampoo

Bakery:

    Bread
```

---

## Tech Stack
- **Python**: Core scripting language.
- **Ollama**: AI model powering the categorization logic.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- Inspired by [this tutorial video](https://youtu.be/GWB9ApTPTv4?si=Fqzjl97_90uSWh-2) while learning AI and Ollama.
- Special thanks to Ollama for their AI tools and resources.

---

Feel free to contribute, suggest enhancements, or use this project as a foundation for your own AI experiments!
