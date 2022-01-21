from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ma9xc.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

# Student Info
harry = {
    "student_id": "1007",
    "first_name": "Harry",
    "last_name": "Potter",
    "enrollments": [
        {
            "term": "Spring 2022",
            "gpa": "3.5",
            "start_date": "February 22, 2022",
            "end_date": "May 15, 2022",
            "courses": [
                {
                    "course_id": "Mag420",
                    "description": "Defense Against the Dark Arts",
                    "instructor": "Alastor Moody",
                    "grade": "A"
                },
                {
                    "course_id": "POT310",
                    "description": "Potions",
                    "instructor": "Severus Snape",
                    "grade": "B+"
                }
            ]
        }
    ]
}

ron = {
    "student_id": "1008",
    "first_name": "Ronald",
    "last_name": "Weasley",
    "enrollments": [
        {
            "term": "Spring 2022",
            "gpa": "3.0",
            "start_date": "February 22, 2022",
            "end_date": "May 15, 2022",
            "courses": [
                {
                    "course_id": "Mag420",
                    "description": "Defense Against the Dark Arts",
                    "instructor": "Alastor Moody",
                    "grade": "B-"
                },
                {
                    "course_id": "POT310",
                    "description": "Potions",
                    "instructor": "Severus Snape",
                    "grade": "C"
                }
            ]
        }
    ]
}

hermione = {
    "student_id": "1009",
    "first_name": "Hermione",
    "last_name": "Granger",
    "enrollments": [
        {
            "term": "Spring 2022",
            "gpa": "4.5",
            "start_date": "February 22, 2022",
            "end_date": "May 15, 2022",
            "courses": [
                {
                    "course_id": "Mag420",
                    "description": "Defense Against the Dark Arts",
                    "instructor": "Alastor Moody",
                    "grade": "A++"
                },
                {
                    "course_id": "POT310",
                    "description": "Potions",
                    "instructor": "Severus Snape",
                    "grade": "A++"
                }
            ]
        }
    ]
}

# Student Collection
students = db.students

print(" -- INSERT STATEMENTS --")
harry_student_id = students.insert_one(harry).inserted_id
print( " Inserted student record Harry Potter into the students collection with document id " + str(harry_student_id))

ron_student_id = students.insert_one(ron).inserted_id
print( " Inserted student record Ronald Weasley into the students collection with document id " + str(ron_student_id))

hermione_student_id = students.insert_one(hermione).inserted_id
print( " Inserted student record Hermione Granger into the students collection with document id " + str(hermione_student_id))

input("\n\n End of program, press any key to continue...")