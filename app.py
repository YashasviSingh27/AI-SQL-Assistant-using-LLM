from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure Google Generative AI with your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    sql = sql.strip("`")
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

prompt = [
    """
    You are an expert in converting English questions to SQL queries!
The SQL database contains a joined table named STUDENT_TEACHER_EXPERIENCE.
This table combines data from STUDENT, TEACHER, and EXPERIENCE tables.
The columns in the table are: Student_Name, Student_Subject, Student_Section, Student_Marks, Teacher_Name, Teacher_Subject, Teacher_Experience, Teacher_Designation.

For example:
Example 1 - Show me the average marks scored by students taught by each teacher.
The SQL command will be something like this: 
SELECT Teacher_Name, AVG(Student_Marks) AS Avg_Marks
FROM STUDENT_TEACHER_EXPERIENCE
GROUP BY Teacher_Name;

Example 2 - Provide all the data.
The SQL command will be something like this:
SELECT * FROM STUDENT_TEACHER_EXPERIENCE;

Example 3 - List all the students who scored above 80 marks in subjects taught by teachers with more than 5 years of experience.
The SQL command will be something like this: 
SELECT Student_Name, Student_Subject, Student_Marks, Teacher_Name, Teacher_Subject, Teacher_Experience, Teacher_Designation
FROM STUDENT_TEACHER_EXPERIENCE
WHERE Student_Marks > 80 AND Teacher_Experience > 5;

Example 4 - Find the total number of students taught by each teacher, categorized by their designation.
The SQL command will be something like this: 
SELECT Teacher_Name, Teacher_Designation, COUNT(Student_Name) AS Num_Students
FROM STUDENT_TEACHER_EXPERIENCE
GROUP BY Teacher_Name, Teacher_Designation;

Example 5 - Show me the average marks scored by students taught by each teacher for a particular subject.
The SQL command will be something like this: 
SELECT Teacher_Name, Teacher_Subject, AVG(Student_Marks) AS Avg_Marks
FROM STUDENT_TEACHER_EXPERIENCE
GROUP BY Teacher_Name, Teacher_Subject;

Example 6 - Show me the highest marks scored by students taught by each teacher for a particular subject.
The SQL command will be something like this: 
SELECT Teacher_Name, Teacher_Subject, MAX(Student_Marks) AS Max_Marks
FROM STUDENT_TEACHER_EXPERIENCE
GROUP BY Teacher_Name, Teacher_Subject;

Example 7 - Provide the highest marks in each subject along with the teacher's name.
The SQL command will be something like this:
SELECT Teacher_Name, Teacher_Subject, MAX(Student_Marks) AS Max_Marks
FROM STUDENT_TEACHER_EXPERIENCE
GROUP BY Teacher_Name, Teacher_Subject;

Example 8 - Provide the name of the student who has the highest marks overall.
The SQL command will be something like this:
SELECT Student_Name
FROM STUDENT_TEACHER_EXPERIENCE
WHERE Student_Marks = (SELECT MAX(Student_Marks) FROM STUDENT_TEACHER_EXPERIENCE);

Please provide your English question, and I will generate the corresponding SQL query for you.
    The SQL code should not have ``` in the beginning or end, and the output should not contain the word "sql".
    """
]

st.set_page_config(page_title="Welcome To UPES Database")
st.header("WELCOME TO UPES DATABASE")

st.write("This Database contains:")
st.write("- Student's Information regarding their Name, Subject opted, Section, Marks.")
st.write("- Teacher's Information regarding their Subject, Experience, and Designation.")

st.subheader("This SQL Buddy Provides the Data In Simple Language")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    response = read_sql_query(response, "student.db")

    if response:  
        st.subheader("The Response is")
        st.dataframe(response, height=400)  
    else:
        st.subheader("No results found for your query.")

