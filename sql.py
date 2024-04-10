import sqlite3

# Connect to the database
connection = sqlite3.connect("student.db")
cursor = connection.cursor()

# Create the STUDENT table
table_student = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    SUBJECT VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""
cursor.execute(table_student)

# Create the TEACHER table
table_teacher = """
CREATE TABLE IF NOT EXISTS TEACHER (
    NAME VARCHAR(25),
    SUBJECT VARCHAR(25),
    EXPERIENCE INT
);
"""
cursor.execute(table_teacher)

# Create the EXPERIENCE table
table_experience = """
CREATE TABLE IF NOT EXISTS EXPERIENCE (
    NAME VARCHAR(25),
    DESIGNATION VARCHAR(25),
    EXPERIENCE INT
);
"""
cursor.execute(table_experience)

# Insert data into the STUDENT table
student_data = [
    ('Krish', 'Data Science', 'A', 90),
    ('Sudhanshu', 'Data Science', 'B', 100),
    ('Darius', 'Data Science', 'A', 86),
    ('Vikash', 'DEVOPS', 'A', 50),
    ('Dipesh', 'DEVOPS', 'A', 35),
    ('Yash', 'Cloud', 'A', 93),
    ('Vishesh', 'Data Science', 'B', 98),
    ('Aman', 'Cloud', 'A', 85),
    ('vanya', 'DEVOPS', 'A', 53),
    ('Raju', 'Cloud', 'A', 37)
]
cursor.executemany("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", student_data)

# Insert data into the TEACHER table
teacher_data = [
    ('Mr. Smith', 'Data Science', 5),
    ('Ms. Johnson', 'DEVOPS', 7),
    ('Dr. Patel', 'Cloud', 10)
]
cursor.executemany("INSERT INTO TEACHER VALUES (?, ?, ?)", teacher_data)

# Insert data into the EXPERIENCE table
experience_data = [
    ('Mr. Smith', 'Professor', 5),
    ('Ms. Johnson', 'Instructor', 7),
    ('Dr. Patel', 'Associate Professor', 10)
]
cursor.executemany("INSERT INTO EXPERIENCE VALUES (?, ?, ?)", experience_data)

# Perform join operations to combine STUDENT, TEACHER, and EXPERIENCE tables
join_query = """
CREATE TABLE IF NOT EXISTS STUDENT_TEACHER_EXPERIENCE AS
SELECT STUDENT.NAME AS Student_Name, STUDENT.SUBJECT AS Student_Subject, STUDENT.SECTION, STUDENT.MARKS,
       TEACHER.NAME AS Teacher_Name, TEACHER.SUBJECT AS Teacher_Subject, TEACHER.EXPERIENCE AS Teacher_Experience,
       EXPERIENCE.DESIGNATION AS Teacher_Designation
FROM STUDENT
JOIN TEACHER ON STUDENT.SUBJECT = TEACHER.SUBJECT
JOIN EXPERIENCE ON TEACHER.NAME = EXPERIENCE.NAME;
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
