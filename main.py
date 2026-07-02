from InquirerPy import prompt
from questions import Questions, writefile

question_manager = Questions()
answers = prompt(question_manager.get_questions())

# Create a template for the readme
template = f"""
# User Information
- Name: {answers['Name']}
- Project: {answers['Project_Title']}
## Project Description
- Description: {answers['Project_Description']}
## Installation
- Instructions: {answers['Installation_Instructions']}
## Usage Information
- Information: {answers['Usage_Information']}
## License
- Product License: {answers['License']}
## Contact Information
- Information: {answers['Contact_Information']}
# Disclaimer
- All rights reserved, Copyright (C) 2026 Jay Dewhurst"""

# write to a file called README.md
file_writer = writefile()
file_writer.write(template)

print("README.md created successfully.")

