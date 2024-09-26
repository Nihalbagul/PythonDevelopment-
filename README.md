
---

# Python Command-Line File Processing Tool

This project is a Python command-line tool that processes text files and performs various operations such as word count, character count, line count, word search, and word replacement. The project is documented using Sphinx to provide a detailed user guide and API documentation.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Command-Line Options](#command-line-options)
- [Documentation](#documentation)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Word Count: Count the total number of words in a text file.
- Character Count: Count the total number of characters in a text file.
- Line Count: Count the number of lines in a text file.
- Find a Word: Search for a specific word in the file and display its frequency.
- Replace a Word: Replace a word in the text file and save the modified file.

## Requirements

- Python 3.7+
- Sphinx (for documentation)

## Installation

### 1. Clone the repository
```bash
git clone (https://github.com/Nihalbagul/PythonDevelopment)
cd PythonDevelopment
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Build Documentation (optional)
```bash
cd docs
make html
```

## Usage

To use the command-line tool, run the following command:
```bash
python src/text_processor.py --file <path_to_file> [options]
```

### Example:
```bash
python src/text_processor.py --file sample.txt --word-count --char-count --find "example" --replace "old" "new"
```

## Command-Line Options

- `--file` or `-f`: The path to the input text file (required).
- `--word-count` or `-wc`: Display the total word count.
- `--char-count` or `-cc`: Display the total character count.
- `--line-count` or `-lc`: Display the total line count.
- `--find` or `-find`: Search for a specific word in the text file.
- `--replace` or `-r`: Replace a word in the text file with another word.

### Example Output:
```bash
Word Count: 1200
Character Count: 7200
The word "example" occurs 5 times.
"old" was replaced with "new" and saved to updated_sample.txt
```

## Documentation

The project documentation is generated using Sphinx. To view the documentation:

1. Navigate to the `docs/` directory:
   ```bash
   cd docs
   ```

2. Build the HTML documentation:
   ```bash
   make html
   ```

3. Open the generated documentation in your browser:
   ```bash
   open _build/html/index.html
   ```

The documentation includes:
- User Guide
- Installation Instructions
- API Reference

## Directory Structure

```
project/
│
├── docs/                 # Sphinx documentation files
│   ├── _build/           # Generated HTML files
│   ├── conf.py           # Sphinx configuration file
│   ├── index.rst         # Main documentation file
│   └── other .rst files  # Documentation sections
│
├── src/                  # Python source files
│   └── text_processor.py # Main CLI tool
│
├── tests/                # Test files
│   └── test_text_processor.py
│
├── requirements.txt      # Python dependencies
└── README.md             # Project README
```

## Contributing

Feel free to contribute by submitting pull requests, creating issues, or suggesting improvements!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This `README.md` gives a structured overview of the project, how to use the tool, and how to contribute. You can customize the details like the repository URL, usage examples, or other details based on your project’s specifics.

Let me know if you need any changes or additions!
