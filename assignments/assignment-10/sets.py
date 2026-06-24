# Task 1: Student Enrollment Analysis
# Sample Data:
# Python Students: Ravi, Anu, Sai, Kiran, Teja
# SQL Students: Sai, Teja, Rahul, Anu, Priya

python_students = {"Ravi", "Anu", "Sai", "Kiran", "Teja"}
sql_students = {"Sai", "Teja", "Rahul", "Anu", "Priya"}

# 1. Find students enrolled in both courses.
both_courses = python_students.intersection(sql_students)
print(both_courses)

#2. Find students enrolled only in Python.
python_only = python_students.difference(sql_students)
print(python_only)

#3. Find students enrolled only in SQL.
sql_only = sql_students.difference(python_students)
print(sql_only)

# 4. Find all students enrolled in either course.
all_students = python_students.union(sql_students)
print(all_students)


#5. Find students enrolled in exactly one course.
one_course = python_students.symmetric_difference(sql_students)
print(one_course)


# Task 2: Employee Skills Management
# Sample Data:
# Team A Skills: Python, SQL, Git, Docker
# Team B Skills: Java, SQL, AWS, Git


team_a_skills = {"Python", "SQL", "Git", "Docker"}
team_b_skills = {"Java", "SQL", "AWS", "Git"}


#1. Find common skills between the teams.
common_skills = team_a_skills.intersection(team_b_skills)
print(common_skills)


#2. Find skills available only in Team A.
team_a_only = team_a_skills.difference(team_b_skills)
print(team_a_only)


#3. Find skills available only in Team B.
team_b_only = team_b_skills.difference(team_a_skills)
print(team_b_only)


#4. Find all skills available in the organization.
all_skills = team_a_skills.union(team_b_skills)
print(all_skills)


#5. Add Linux to Team A and remove Java from Team B.
team_a_skills.add("Linux")
team_b_skills.discard("Java")


# Task 3: Online Store Customers
# Sample Data:
# Amazon Customers: Ravi, Anu, Kiran, Sai, Teja
# Flipkart Customers: Sai, Teja, Rahul, Priya, Anu


amazon_customers = {"Ravi", "Anu", "Kiran", "Sai", "Teja"}
flipkart_customers = {"Sai", "Teja", "Rahul", "Priya", "Anu"}

#1. Find customers who shopped on both platforms.
both_platforms = amazon_customers.intersection(flipkart_customers)
print(both_platforms)


# 2. Find customers who purchased only from Amazon.
amazon_only = amazon_customers.difference(flipkart_customers)
print(amazon_only)


#3. Find customers who purchased only from Flipkart.
flipkart_only = flipkart_customers.difference(amazon_customers)
print(flipkart_only)


#4. Find all unique customers.
all_customers = amazon_customers.union(flipkart_customers)
print(all_customers)


# 5. Find customers who purchased from exactly one store.
exactly_one_store = amazon_only.union(flipkart_only)
print(exactly_one_store)    


# Task 4: Programming Languages Survey
# Sample Data:
# Batch 1: Python, Java, C, SQL
# Batch 2: Python, Java, React, JavaScript


batch_1={"Python", "Java", "C", "SQL"}
batch_2={"Python", "Java", "React", "JavaScript"}


# 1. Find languages known by both batches.
common_languages = batch_1.intersection(batch_2)
print(common_languages)


#2. Find languages known only by Batch 1.
batch_1_only = batch_1.difference(batch_2)
print(batch_1_only)


#3. Find languages known only by Batch 2.
batch_2_only = batch_2.difference(batch_1)
print(batch_2_only)


#4. Check whether Batch 1 is a subset of Batch 2.
is_subset = batch_1.issubset(batch_2)
print(is_subset)


#5. Check whether Batch 2 is a superset of Batch 1.
is_superset = batch_2.issuperset(batch_1)
print(is_superset)