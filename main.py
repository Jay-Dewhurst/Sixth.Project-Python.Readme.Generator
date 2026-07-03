# Resources needed for Program to run
from InquirerPy import prompt
from questions import Questions, writefile
from effects import display_table, loading_simulation, setup_logging, print_header

# Variables for the Question class and Rich logger definitions
question_manager = Questions()
answers = prompt(question_manager.get_questions())

logger = setup_logging()
print_header()
display_table()
loading_simulation()

# Created a template for the Readme Generator to use for writing template and displaying the Rich logger
template = f"""# Welcome to the Readme Generator Program!

## Author name and Project Title
- Name: {answers['Name']}
- Project Title: {answers['Project_Title']}
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
### Disclaimer
- All rights reserved, Copyright (C) 2026 Jay Dewhurst"""

# Writes and logs to a file called README.md
file_writer = writefile()
file_writer.write(template)

logger.info("README.md created successfully.")