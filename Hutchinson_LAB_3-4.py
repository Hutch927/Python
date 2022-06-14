# Create a dictionary to store information about a student. the keys should include entries for the first name,
# last name, email address, and major. Print each piece of information from your dictionary.

student_0 = {"first name": "Frederick", "last Name": "Hutchinson", "email address": "fhutchin@norwich.edu",
             "major": "CS"}
for key, value in student_0.items():
    print(f"{key.title()}: {value}")

