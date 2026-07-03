from InquirerPy import prompt
from questions import Questions, writefile
from effects import display_table, loading_simulation, setup_logging, print_header

question_manager = Questions()
answers = prompt(question_manager.get_questions())

logger = setup_logging()
print_header()
display_table()
loading_simulation()

# Create a template for the readme
template = f"""# User Information
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

logger.info("README.md created successfully.")