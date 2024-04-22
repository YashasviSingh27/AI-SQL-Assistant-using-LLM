import sqlite3

# Connect to the database
connection = sqlite3.connect("student.db")
cursor = connection.cursor()

# Create the STUDENT table
table_student = """
CREATE TABLE IF NOT EXISTS STUDENT (
    Student_Name VARCHAR(25),
    Student_Subject VARCHAR(25),
    Student_Section VARCHAR(25),
    Student_Marks INT
);
"""
cursor.execute(table_student)

# Create the TEACHER table
table_teacher = """
CREATE TABLE IF NOT EXISTS TEACHER (
    Teacher_Name VARCHAR(25),
    Teacher_Subject VARCHAR(25),
    Teacher_Experience INT
);
"""
cursor.execute(table_teacher)

# Create the EXPERIENCE table
table_experience = """
CREATE TABLE IF NOT EXISTS EXPERIENCE (
    Teacher_Name VARCHAR(25),
    Teacher_Designation VARCHAR(25),
    Teacher_Experience INT
);
"""
cursor.execute(table_experience)

# Insert data into the STUDENT table
student_data = [
    ('Krish', 'Data Science', 'A', 90),
    ('Sudhanshu', 'Data Science', 'A', 99),
    ('Darius', 'Data Science', 'A', 86),
    ('Vikash', 'Devops', 'A', 50),
    ('Dipesh', 'Devops', 'A', 35),
    ('Vibhor', 'Data Science', 'A', 45),
    ('Yash', 'Cloud', 'B', 93),
    ('Vishesh', 'Data Science', 'B', 98),
    ('Aman', 'Cloud', 'B', 85),
    ('vanya', 'Devops', 'B', 53),
    ('Raju', 'Cloud', 'B', 37),
    ('Vasu', 'Cloud', 'B', 67),
    ('Krish', 'Devops', 'A', 86),
    ('Sudhanshu', 'Devops', 'A', 86),
    ('Darius', 'Devops', 'A', 86),
    ('Vikash', 'Data Science', 'A', 69),
    ('Dipesh', 'Data Science', 'A', 51),
    ('Vibhor', 'Devops', 'A', 67),
    ('Yash', 'Data Science', 'B', 93),
    ('Vishesh', 'Cloud', 'B', 89),
    ('Aman', 'Devops', 'B', 91),
    ('vanya', 'Data Science', 'B', 91),
    ('Raju', 'Data Science', 'B', 73),
    ('Vasu', 'Devops', 'B', 78),
    ('Krish', 'Cloud', 'A', 79),
    ('Krish', 'Oops', 'A', 71),
    ('Krish', 'Blockchain', 'A', 95),
    ('Sudhanshu', 'Cloud', 'A', 54),
    ('Sudhanshu', 'Oops', 'A', 92),
    ('Sudhanshu', 'Blockchain', 'A', 69),
    ('Darius', 'Cloud', 'A', 67),
    ('Darius', 'Oops', 'A', 93),
    ('Darius', 'Blockchain', 'A', 64),
    ('Vikash', 'Cloud', 'A', 64),
    ('Vikash', 'Oops', 'A', 83),
    ('Vikash', 'Blockchain', 'A', 41),
    ('Dipesh', 'Cloud', 'A', 79),
    ('Dipesh', 'Oops', 'A', 89),
    ('Dipesh', 'Blockchain', 'A', 90),
    ('Vibhor', 'Cloud', 'A', 81),
    ('Vibhor', 'Oops', 'A', 73),
    ('Vibhor', 'Blockchain', 'A', 75),
    ('Yash', 'Devops', 'B', 91),
    ('Yash', 'Oops', 'B', 83),
    ('Yash', 'Blockchain', 'B', 99),
    ('Vishesh', 'Devops', 'B', 91),
    ('Vishesh', 'Oops', 'B', 90),
    ('Vishesh', 'Blockchain', 'B', 89),
    ('Aman', 'Data Science', 'B', 83),
    ('Aman', 'Oops', 'B', 85),
    ('Aman', 'Blockchain', 'B', 89),
    ('vanya', 'Cloud', 'B', 83),
    ('vanya', 'Oops', 'B', 69),
    ('vanya', 'Blockchain', 'B', 94),
    ('Raju', 'Devops', 'B', 90),
    ('Raju', 'Oops', 'B', 47),
    ('Raju', 'Blockchain', 'B', 86),
    ('Vasu', 'Data Science', 'B', 81),
    ('Vasu', 'Oops', 'B', 84),
    ('Vasu', 'Blockchain', 'B', 90)
    
]
cursor.executemany("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", student_data)

# Insert data into the TEACHER table
teacher_data = [
    ('Mr. Sumit', 'Data Science', 5),
    ('Ms. John', 'Devops', 7),
    ('Dr. Patel', 'Cloud', 10),
    ('Dr. Ravi', 'Oops', 11),
    ('Ms. Tanu', 'Blockchain', 15)
]
cursor.executemany("INSERT INTO TEACHER VALUES (?, ?, ?)", teacher_data)

# Insert data into the EXPERIENCE table
experience_data = [
    ('Mr. Sumit', 'Professor', 5),
    ('Ms. John', 'Assistant Professor', 7),
    ('Dr. Patel', 'Associate Professor', 10),
    ('Dr. Ravi', 'Associate Professor', 11),
    ('Ms. Tanu', 'Assistant Professor', 15)
]
cursor.executemany("INSERT INTO EXPERIENCE VALUES (?, ?, ?)", experience_data)

# Perform join operations to combine STUDENT, TEACHER, and EXPERIENCE tables
join_query = """
CREATE TABLE IF NOT EXISTS STUDENT_TEACHER_EXPERIENCE AS
SELECT STUDENT.Student_Name, STUDENT.Student_Subject, STUDENT.Student_Section, STUDENT.Student_Marks,
       TEACHER.Teacher_Name, TEACHER.Teacher_Subject, TEACHER.Teacher_Experience,
       EXPERIENCE.Teacher_Designation
FROM STUDENT
JOIN TEACHER ON STUDENT.Student_Subject = TEACHER.Teacher_Subject
JOIN EXPERIENCE ON TEACHER.Teacher_Name = EXPERIENCE.Teacher_Name;
"""
cursor.execute(join_query)

# Print the combined data
print("Combined records:")
combined_records = cursor.execute("SELECT * FROM STUDENT_TEACHER_EXPERIENCE")
for row in combined_records:
    print(row)

# Commit changes and close connection
connection.commit()
connection.close()
