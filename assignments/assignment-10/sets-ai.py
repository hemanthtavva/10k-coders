# ==========================================
# Python Sets – Practice Tasks
# ==========================================

# ==========================================
# Task 1: Student Enrollment Analysis
# ==========================================

print("===== Task 1: Student Enrollment Analysis =====")

python_students = {"Ravi", "Anu", "Sai", "Kiran", "Teja"}
sql_students = {"Sai", "Teja", "Rahul", "Anu", "Priya"}

print("Python Students:", python_students)
print("SQL Students:", sql_students)

# 1. Find students enrolled in both courses.
both_courses = python_students.intersection(sql_students)
print("\nStudents enrolled in both courses:")
print(both_courses)

# 2. Find students enrolled only in Python.
python_only = python_students.difference(sql_students)
print("\nStudents enrolled only in Python:")
print(python_only)

# 3. Find students enrolled only in SQL.
sql_only = sql_students.difference(python_students)
print("\nStudents enrolled only in SQL:")
print(sql_only)

# 4. Find all students enrolled in either course.
all_students = python_students.union(sql_students)
print("\nAll students enrolled in either course:")
print(all_students)

# 5. Find students enrolled in exactly one course.
one_course = python_students.symmetric_difference(sql_students)
print("\nStudents enrolled in exactly one course:")
print(one_course)


# ==========================================
# Task 2: Employee Skills Management
# ==========================================

print("\n\n===== Task 2: Employee Skills Management =====")

team_a_skills = {"Python", "SQL", "Git", "Docker"}
team_b_skills = {"Java", "SQL", "AWS", "Git"}

print("Team A Skills:", team_a_skills)
print("Team B Skills:", team_b_skills)

# 1. Find common skills between the teams.
common_skills = team_a_skills.intersection(team_b_skills)
print("\nCommon skills between Team A and Team B:")
print(common_skills)

# 2. Find skills available only in Team A.
team_a_only = team_a_skills.difference(team_b_skills)
print("\nSkills available only in Team A:")
print(team_a_only)

# 3. Find skills available only in Team B.
team_b_only = team_b_skills.difference(team_a_skills)
print("\nSkills available only in Team B:")
print(team_b_only)

# 4. Find all skills available in the organization.
all_skills = team_a_skills.union(team_b_skills)
print("\nAll skills available in the organization:")
print(all_skills)

# 5. Add Linux to Team A and remove Java from Team B.
team_a_skills.add("Linux")
team_b_skills.discard("Java")

print("\nUpdated Team A Skills:")
print(team_a_skills)

print("\nUpdated Team B Skills:")
print(team_b_skills)


# ==========================================
# Task 3: Online Store Customers
# ==========================================

print("\n\n===== Task 3: Online Store Customers =====")

amazon_customers = {"Ravi", "Anu", "Kiran", "Sai", "Teja"}
flipkart_customers = {"Sai", "Teja", "Rahul", "Priya", "Anu"}

print("Amazon Customers:", amazon_customers)
print("Flipkart Customers:", flipkart_customers)

# 1. Find customers who shopped on both platforms.
both_platforms = amazon_customers.intersection(flipkart_customers)
print("\nCustomers who shopped on both platforms:")
print(both_platforms)

# 2. Find customers who purchased only from Amazon.
amazon_only = amazon_customers.difference(flipkart_customers)
print("\nCustomers who purchased only from Amazon:")
print(amazon_only)

# 3. Find customers who purchased only from Flipkart.
flipkart_only = flipkart_customers.difference(amazon_customers)
print("\nCustomers who purchased only from Flipkart:")
print(flipkart_only)

# 4. Find all unique customers.
all_customers = amazon_customers.union(flipkart_customers)
print("\nAll unique customers:")
print(all_customers)

# 5. Find customers who purchased from exactly one store.
exactly_one_store = amazon_customers.symmetric_difference(flipkart_customers)
print("\nCustomers who purchased from exactly one store:")
print(exactly_one_store)


# ==========================================
# Task 4: Programming Languages Survey
# ==========================================

print("\n\n===== Task 4: Programming Languages Survey =====")

batch_1 = {"Python", "Java", "C", "SQL"}
batch_2 = {"Python", "Java", "React", "JavaScript"}

print("Batch 1 Languages:", batch_1)
print("Batch 2 Languages:", batch_2)

# 1. Find languages known by both batches.
common_languages = batch_1.intersection(batch_2)
print("\nLanguages known by both batches:")
print(common_languages)

# 2. Find languages known only by Batch 1.
batch_1_only = batch_1.difference(batch_2)
print("\nLanguages known only by Batch 1:")
print(batch_1_only)

# 3. Find languages known only by Batch 2.
batch_2_only = batch_2.difference(batch_1)
print("\nLanguages known only by Batch 2:")
print(batch_2_only)

# 4. Check whether Batch 1 is a subset of Batch 2.
is_subset = batch_1.issubset(batch_2)
print("\nIs Batch 1 a subset of Batch 2?")
print(is_subset)

# 5. Check whether Batch 2 is a superset of Batch 1.
is_superset = batch_2.issuperset(batch_1)
print("\nIs Batch 2 a superset of Batch 1?")
print(is_superset)


# ==========================================
# Task 5: Website Visitor Analysis
# ==========================================

print("\n\n===== Task 5: Website Visitor Analysis =====")

day_1_visitors = {"user1", "user2", "user3", "user4", "user5"}
day_2_visitors = {"user3", "user4", "user5", "user6", "user7"}

print("Day 1 Visitors:", day_1_visitors)
print("Day 2 Visitors:", day_2_visitors)

# 1. Find returning visitors.
returning_visitors = day_1_visitors.intersection(day_2_visitors)
print("\nReturning visitors:")
print(returning_visitors)

# 2. Find visitors who visited only on Day 1.
day_1_only = day_1_visitors.difference(day_2_visitors)
print("\nVisitors who visited only on Day 1:")
print(day_1_only)

# 3. Find visitors who visited only on Day 2.
day_2_only = day_2_visitors.difference(day_1_visitors)
print("\nVisitors who visited only on Day 2:")
print(day_2_only)

# 4. Find all unique visitors across both days.
all_visitors = day_1_visitors.union(day_2_visitors)
print("\nAll unique visitors:")
print(all_visitors)

# 5. Find visitors who visited on exactly one day.
exactly_one_day = day_1_visitors.symmetric_difference(day_2_visitors)
print("\nVisitors who visited on exactly one day:")
print(exactly_one_day)