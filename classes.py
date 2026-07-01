class Database:
	"""Represents a simple database to store records."""
	def __init__(self):
		self.records = []

	def add_new(self, record):
		"""Adds a new record to the database."""
		self.records.append(record)
		print(f"New record added: {record}")

	def get_records(self):
		"""Returns all records in the database."""
		return self.records

# Storing Questions and Answers in the database
class Question1(Database):
	"""Represents a question and answer database."""
	
	def add_new(self, name, message,):
		"""Adds a new question and answer record."""
		record = {"Type": "input", "name": name, "Message": message,}
		super().add_new(record)

class Question2(Database):
	"""Represents a question and answer database."""

	def add_new(self, name, message,):
		"""Adds a new question and answer record."""
		record = {"Type": "input", "name": name, "Message": message,}
		super().add_new(record)

class Question3(Database):
	"""Represents a question and answer database."""

	def add_new(self, name, message,):
		"""Adds a new question and answer record."""
		record = {"Type": "input", "name": name, "Message": message,}
		super().add_new(record)

class Question4(Database):
	"""Represents a question and answer database."""

	def add_new(self, name, message,):
		"""Adds a new question and answer record."""
		record = {"Type": "input", "name": name, "Message": message,}
		super().add_new(record)

class Question5(Database):
	"""Represents a question and answer database."""

	def add_new(self, name, message,):
		"""Adds a new question and answer record."""
		record = {"Type": "list", "name": name, "choices": message}
		super().add_new(record)

class Question6(Database):
	"""Represents a question and answer database."""

	def add_new(self, name, message,):
		"""Adds a new question and answer record."""
		record = {"Type": "input", "name": name, "Message": message,}
		super().add_new(record)

# Outputting the questions and answers in a list of dictionaries
if __name__ == "__main__":
	Database()

	#Database instances
	question1_db = Question1()
	question2_db = Question2()
	question3_db = Question3()
	question4_db = Question4()
	question5_db = Question5()
	question6_db = Question6()

	# Add records
	question1_db.add_new("project title", "Project Title:")
	question2_db.add_new("project description", "Project Description:")
	question3_db.add_new("install instructions", "Installation Instructions:")
	question4_db.add_new("usage information", "Usage Information:")
	question5_db.add_new("license", 
		[
		"MIT License",
		"Apache License 2.0",
		"GNU GPL v3",
		"GNU LGPL v3",
		"Mozilla Public License 2.0",
		"Creative Commons",
		"Unlicense"
		])
	question6_db.add_new("contact details", "Contact Details & Author Name")

	#Retrieve and print records
	print("\nQuestion 1:", question1_db.get_records())
	print("\nQuestion 2:", question2_db.get_records())
	print("\nQuestion 3:", question3_db.get_records())
	print("\nQuestion 4:", question4_db.get_records())
	print("\nQuestion 5:", question5_db.get_records())
	print("\nQuestion 6:", question6_db.get_records())

