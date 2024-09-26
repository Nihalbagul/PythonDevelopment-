import argparse
import os
from typing import List

def count_words(file_path: str) -> int:
    """Counts the number of words in a file.
    
    Parameters:
    file_path (str): The path to the text file.
    
    Returns:
    int: The total word count.
    
    Raises:
    FileNotFoundError: If the file does not exist.
    """
    try:
        with open(file_path, 'r') as file:
            return sum(len(line.split()) for line in file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

def count_chars(file_path: str) -> int:
    """Counts the number of characters in a file."""
    try:
        with open(file_path, 'r') as file:
            return sum(len(line) for line in file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

def count_lines(file_path: str) -> int:
    """Counts the number of lines in a file."""
    try:
        with open(file_path, 'r') as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

def find_word(file_path: str, word: str) -> int:
    """Finds the frequency of a specific word in a file."""
    try:
        with open(file_path, 'r') as file:
            return sum(line.lower().count(word.lower()) for line in file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

def replace_word(file_path: str, old_word: str, new_word: str, output_file: str) -> None:
    """Replaces a word in a file and saves it as a new file."""
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            updated_data = data.replace(old_word, new_word)
        with open(output_file, 'w') as file:
            file.write(updated_data)
        print(f'"{old_word}" was replaced with "{new_word}" and saved to {output_file}')
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

def main():
    parser = argparse.ArgumentParser(description="Process a text file.")
    parser.add_argument("-f", "--file", required=True, help="Path to the text file.")
    parser.add_argument("-wc", "--word-count", action="store_true", help="Count the words in the file.")
    parser.add_argument("-cc", "--char-count", action="store_true", help="Count the characters in the file.")
    parser.add_argument("-lc", "--line-count", action="store_true", help="Count the lines in the file.")
    parser.add_argument("-find", "--find", help="Find a specific word in the file.")
    parser.add_argument("-r", "--replace", nargs=2, metavar=('old_word', 'new_word'), help="Replace a word in the file.")
    
    args = parser.parse_args()
    
    if not os.path.isfile(args.file):
        print(f"Error: File '{args.file}' not found.")
        return

    if args.word_count:
        print(f"Word Count: {count_words(args.file)}")
    
    if args.char_count:
        print(f"Character Count: {count_chars(args.file)}")
    
    if args.line_count:
        print(f"Line Count: {count_lines(args.file)}")
    
    if args.find:
        word_freq = find_word(args.file, args.find)
        print(f'The word "{args.find}" occurs {word_freq} times.')
    
    if args.replace:
        old_word, new_word = args.replace
        output_file = f"updated_{os.path.basename(args.file)}"
        replace_word(args.file, old_word, new_word, output_file)

if __name__ == "__main__":
    main()
