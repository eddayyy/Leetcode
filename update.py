import json
import os
from tabulate import tabulate

# Load existing problems metadata
def load_problems_metadata():
    print("Loading existing problems metadata...")
    if os.path.exists('metadata.json'):
        with open('metadata.json', 'r') as f:
            return json.load(f)
    return {}

# Save problems metadata
def save_problems_metadata(problems_metadata):
    print("Saving updated problems metadata...")
    with open('metadata.json', 'w') as f:
        json.dump(problems_metadata, f, indent=4)

# Detect new solutions in the solutions directory
def detect_new_solutions(problems_metadata):
    print("Detecting new solutions in the solutions directory...")
    solution_files = os.listdir('solutions')
    new_solutions = 0
    for solution_file in solution_files:
        problem_number, extension = os.path.splitext(solution_file)
        problem_number = problem_number.strip()  # Strip any surrounding whitespace
        if problem_number not in problems_metadata:
            title, category, difficulty = extract_problem_info(f'solutions/{solution_file}', extension)
            if title and category and difficulty:
                problems_metadata[problem_number] = {
                    "title": title,
                    "category": category,
                    "difficulty": difficulty
                }
                new_solutions += 1
                print(f"New solution detected: {problem_number} - {title}")
    if new_solutions == 0:
        print("No new solutions found.")
    else:
        print(f"{new_solutions} new solutions added.")
    return new_solutions, problems_metadata

# Extract problem info from solution file
def extract_problem_info(file_path, extension):
    print(f"Extracting problem info from {file_path}...")
    title = category = difficulty = None
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    if extension == '.py':
        comment_prefix = '#'
    elif extension == '.cpp':
        comment_prefix = '//'
    elif extension == '.js':
        comment_prefix = '//'
    else:
        return None, None, None

    for line in lines:
        if line.strip().startswith(comment_prefix):
            line = line.strip()[len(comment_prefix):].strip()
            if line.startswith('Title:'):
                title = line[len('Title:'):].strip()
            elif line.startswith('Category:'):
                category = line[len('Category:'):].strip()
            elif line.startswith('Difficulty:'):
                difficulty = line[len('Difficulty:'):].strip()
            elif line.startswith('Diffuclty:'):  # Handling the typo
                difficulty = line[len('Diffuclty:'):].strip()

    return title, category, difficulty

# Generate Markdown table
def generate_markdown_table(problems_metadata):
    print("Generating Markdown table...")
    table_data = []
    for problem_number, data in sorted(problems_metadata.items(), key=lambda x: int(x[0])):
        solution_link = f"./solutions/{problem_number}.{'py' if os.path.exists(f'solutions/{problem_number}.py') else 'cpp' if os.path.exists(f'solutions/{problem_number}.cpp') else 'js'}"
        difficulty_badge = {
            "Easy": "![Easy](https://img.shields.io/badge/-Easy-brightgreen)",
            "Medium": "![Medium](https://img.shields.io/badge/-Medium-yellow)",
            "Hard": "![Hard](https://img.shields.io/badge/-Hard-red)"
        }[data['difficulty']]
        table_data.append([
            problem_number,
            f"[{data['title']}]({f'https://leetcode.com/problems/{data["title"].lower().replace(" ", "-").replace("(", "").replace(")", "").replace("'", "")}/'})",
            data['category'],
            difficulty_badge,
            f"[Solution]({solution_link})"
        ])
    return tabulate(table_data, headers=["Problem Number", "Title", "Category", "Difficulty", "Solution Link"], tablefmt="github")

# Update README.md and index.md
def update_markdown_files(problems_metadata):
    table_md = generate_markdown_table(problems_metadata)

    readme_content = f"""
# LeetCode Solutions

Welcome to my LeetCode repository! This [website](https://leetcode.eduardonunez.dev) contains my solutions to various LeetCode problems that I've solved. The solutions are organized by problem number, Data Structure & Algorithm category, and difficulty.

## Table of Contents

- [About](#about)
- [Solutions](#solutions)

## About

This repository serves as a collection of my solutions to various Data Structures, Algorithms, & Object-Oriented Design challenges on [LeetCode](https://leetcode.com/).

## Solutions

{table_md}
"""

    print("Updating README.md and index.md...")
    with open('README.md', 'w') as f:
        f.write(readme_content)

    with open('index.md', 'w') as f:
        f.write(readme_content)
    print("README.md and index.md updated successfully.")

if __name__ == "__main__":
    print("Starting update process...")
    # Load existing metadata
    problems_metadata = load_problems_metadata()
    # Detect new solutions
    new_solutions, updated_metadata = detect_new_solutions(problems_metadata)
    # Save updated metadata if there are new solutions
    if new_solutions > 0:
        save_problems_metadata(updated_metadata)
        # Update markdown files
        update_markdown_files(updated_metadata)
    else:
        print("No changes detected, skipping write operations.")
    print("Update process completed.")
