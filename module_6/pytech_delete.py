from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ma9xc.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# Set students query
students = db.students

# Set student list query
student_list = students.find({})

# Set loop and print

print("\n --DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print(" Student_ID:" + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

# New Student
new_student = {
    "student_id": "1010",
    "first_name": "Jason",
    "last_name": "Fox"
}

# Insert new Student
new_student_id = students.insert_one(new_student).inserted_id

# Insert output
print("\n -- INSERT STATEMENTS --")
print(" Inserted student record into the students collection with document_id " + str(new_student_id))

# Call for new guy
new_student_doc = students.find_one({"student_id": "1010"})

# find_one() print for new guy
print("\n -- DISPLAYING NEW STUDENT -- ")
print( " Student ID: " + new_student_doc["student_id"] + "\n First Name: " + new_student_doc["first_name"] + "\n Last Name: " + new_student_doc["last_name"] + "\n")

# Call delete one method
deleted_new_guy_doc = students.delete_one({"student_id": "1010"})

# Find all students
new_student_list = students.find({})

# Displaying List after Deletion Display
print(" -- DISPLAYING STUDENTS FROM find() QUERY AFTER DELETING NEW STUDENT --")

# loop for display of all students
for doc in new_student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

input("\n\n End of program, press any key to continue...")