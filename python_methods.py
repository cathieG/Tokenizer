# Commonly used import statements
import os
import sys
import re
import json
import time
import math
import random
import requests
import collections
import itertools
import functools
import statistics
import datetime
import hashlib
import multiprocessing
import threading
from collections import Counter

# String manipulation
def to_upper(s):
    return s.upper()

def to_lower(s):
    return s.lower()

def remove_whitespace(s):
    return s.strip()

def split_string(s, delimiter=" "):
    return s.split(delimiter)

def join_strings(lst, delimiter=" "):
    return delimiter.join(lst)

def replace_substring(s, old, new):
    return s.replace(old, new)

# List operations
def remove_duplicates(lst):
    return list(set(lst))

def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]

def chunk_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

def list_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def list_union(lst1, lst2):
    return list(set(lst1) | set(lst2))

# Dictionary operations
def merge_dicts(d1, d2):
    return {**d1, **d2}

def invert_dict(d):
    return {v: k for k, v in d.items()}

# File handling
def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def write_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def append_to_file(file_path, content):
    with open(file_path, 'a') as f:
        f.write(content)

def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def write_json(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Math operations
def factorial(n):
    return math.factorial(n)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Random operations
def random_int(a, b):
    return random.randint(a, b)

def random_choice(lst):
    return random.choice(lst)

def shuffle_list(lst):
    random.shuffle(lst)
    return lst

# Date & Time
def get_current_time():
    return datetime.datetime.now()

def format_time(dt, fmt="%Y-%m-%d %H:%M:%S"):
    return dt.strftime(fmt)

def parse_time(s, fmt="%Y-%m-%d %H:%M:%S"):
    return datetime.datetime.strptime(s, fmt)

# Hashing
def sha256_hash(s):
    return hashlib.sha256(s.encode()).hexdigest()

# HTTP Requests
def fetch_url(url):
    response = requests.get(url)
    return response.text if response.status_code == 200 else None

# Multithreading & Multiprocessing
def run_in_thread(target, *args):
    thread = threading.Thread(target=target, args=args)
    thread.start()
    return thread

def run_in_process(target, *args):
    process = multiprocessing.Process(target=target, args=args)
    process.start()
    return process

# Functional Programming
def apply_function(lst, func):
    return list(map(func, lst))

def filter_list(lst, func):
    return list(filter(func, lst))

def reduce_list(lst, func):
    return functools.reduce(func, lst)

# Algorithms
def binary_search(lst, target):
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Regular Expressions
def find_all(pattern, text):
    return re.findall(pattern, text)

def match_pattern(pattern, text):
    return re.match(pattern, text)

def replace_pattern(pattern, replacement, text):
    return re.sub(pattern, replacement, text)

# Set Operations
def set_difference(s1, s2):
    return s1 - s2

def set_intersection(s1, s2):
    return s1 & s2

def set_union(s1, s2):
    return s1 | s2

# Statistics
def mean(lst):
    return statistics.mean(lst)

def median(lst):
    return statistics.median(lst)

def mode(lst):
    return statistics.mode(lst)

def standard_deviation(lst):
    return statistics.stdev(lst)

# Miscellaneous
def is_palindrome(s):
    return s == s[::-1]

def reverse_string(s):
    return s[::-1]

def count_occurrences(lst, item):
    return lst.count(item)

def chunk_string(s, size):
    return [s[i:i+size] for i in range(0, len(s), size)]

def read_file(file_path):
    """Reads and returns the content of a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []

def count_lines(file_path):
    """Counts the number of lines in a text file."""
    lines = read_file(file_path)
    return len(lines)

def count_words(file_path):
    """Counts the number of words in a text file."""
    lines = read_file(file_path)
    return sum(len(line.split()) for line in lines)

def most_common_words(file_path, n=10):
    """Finds the most common words in a text file."""
    lines = read_file(file_path)
    words = re.findall(r'\b\w+\b', ' '.join(lines).lower())  # Extract words
    return Counter(words).most_common(n)

def find_lines_containing(file_path, keyword):
    """Finds lines that contain a specific keyword."""
    lines = read_file(file_path)
    return [line.strip() for line in lines if keyword.lower() in line.lower()]

def replace_word_in_file(file_path, old_word, new_word, output_path):
    """Replaces a word in a text file and writes the output to a new file."""
    lines = read_file(file_path)
    new_lines = [line.replace(old_word, new_word) for line in lines]
    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)
    print(f"Replaced '{old_word}' with '{new_word}' in {file_path}. Output saved to {output_path}.")

def count_character_frequency(file_path):
    """Counts the frequency of characters in a text file."""
    lines = read_file(file_path)
    text = ''.join(lines).lower()
    return Counter(text)

def file_summary(file_path):
    """Provides a summary of the file (line count, word count, most common words)."""
    return {
        "line_count": count_lines(file_path),
        "word_count": count_words(file_path),
        "most_common_words": most_common_words(file_path, 5)
    }

def main():
    # String operations
    s = "  Hello, World!  "
    print("Uppercase:", to_upper(s))
    print("Lowercase:", to_lower(s))
    print("Without Whitespace:", remove_whitespace(s))
    
    # List operations
    numbers = [1, 2, 2, 3, 4, 4, 5]
    print("Unique elements:", remove_duplicates(numbers))
    print("Chunked list:", chunk_list(numbers, 2))

    # Dictionary operations
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    print("Merged dictionary:", merge_dicts(d1, d2))

    # File handling
    file_path = "test.txt"
    write_file(file_path, "This is a test file.\nHello, World!")
    print("File content:", read_file(file_path))

    # Math operations
    print("Factorial of 5:", factorial(5))
    print("Fibonacci(10):", fibonacci(10))
    
    # Random
    print("Random integer between 1 and 10:", random_int(1, 10))
    print("Shuffled list:", shuffle_list(numbers[:]))

    # Date & Time
    current_time = get_current_time()
    print("Current time:", format_time(current_time))

    # Hashing
    print("SHA-256 hash of 'password':", sha256_hash("password"))

    # Web request (if internet access is available)
    # print("Fetching example.com:", fetch_url("https://example.com"))

    # Algorithms
    sorted_list = quick_sort([4, 2, 9, 1, 5, 6])
    print("Sorted list:", sorted_list)

    # Regular expressions
    text = "Hello, my email is example@email.com"
    print("Extracted emails:", find_all(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text))

    # Statistics
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Mean:", mean(data))
    print("Standard deviation:", standard_deviation(data))

if __name__ == "__main__":
    main()