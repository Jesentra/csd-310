from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ma9xc.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# Student Collection
students = db.students

# Use the find() command
student_list = students.find({})

print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

# Update Script
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Scarface"}})

# Making a variable for the find_one
harry = students.find_one({"student_id": "1007"})

# Second Display Message
print("\n -- DISPLAYING STUDENT DOCUMENT 1007 --")

# Finding updated student
print(" Student ID: " + harry["student_id"] + "\n First Name: " + harry["first_name"] + "\n Last Name: " + harry["last_name"])

input("\n\n End of program, press any key to continue...")