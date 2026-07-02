# collection of question objects for the InquirerPy prompt
class Questions:
    def __init__(self):
        self.questions = [
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

    def get_questions(self):
        return self.questions

    def add_question(self, question):
        self.questions.append(question)

class writefile:
    def __init__(self, filename="README.md"):
        self.filename = filename

    def write(self, content):
        with open(self.filename, "w") as f:
            f.write(content)