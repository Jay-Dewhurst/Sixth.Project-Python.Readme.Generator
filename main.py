from InquirerPy import prompt

# Get user input with Inquirer
questions = [
    {"type": "input", "name": "Name", "message": "What is the Author's name?"},
    {"type": "input", "name": "Project_Title", "message": "What is the Project Title?"},
    {"type": "input", "name": "Project_Description", "message": "What is your Project Description?", "multiline": True},
    {"type": "input", "name": "Installation_Instructions", "message": "Please enter the Installation Instructions:"},
    {"type": "input", "name": "Usage_Information", "message": "Please enter the Usage Information:"},
    {"type": "list", "name": "License", "message": "Please choose a License", "choices":
        [
        "MIT License",
        "Apache License 2.0",
        "GNU GPL v3",
        "GNU LGPL v3",
        "Mozilla Public License 2.0",
        "Creative Commons",
        "Unlicense",
        ],
        },
    {"type": "input", "name": "Contact_Information", "message": "Please any contact information:"},
]

answers = prompt(questions)

# Create a template for the readme
template = f"""
# User Information
- Name: {answers['Name']}
- Project: {answers['Project_Title']}
## Project Description
- Description {answers['Project_Description']}
## Installation
- Instructions {answers['Installation_Instructions']}
## Usage Information
- Information {answers['Usage_Information']}
## License
- Product License {answers['License']}
## Contact Information
- Information {answers['Contact_Information']}
# Disclaimer
- All rights reserved, Copyright (C) 2026 Jay Dewhurst"""

# TODO: consider moving this in to a class or a function to make it more reusable
# write to a file called README.md
with open("README.md", "w") as f:
    f.write(template)

print("README.md created successfully.")