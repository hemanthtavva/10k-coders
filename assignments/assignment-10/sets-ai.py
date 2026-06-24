# 


# Task 1: Student Enrollment Analysis

python_students = {"Ravi", "Anu", "Sai", "Kiran", "Teja"}
sql_students = {"Sai", "Teja", "Rahul", "Anu", "Priya"}

print("Python Students:", python_students)
print("SQL Students:", sql_students)

print("Students enrolled in both courses:")
print(python_students & sql_students)

print("Students enrolled only in Python:")
print(python_students - sql_students)

print("Students enrolled only in SQL:")
print(sql_students - python_students)

print("All students enrolled in either course:")
print(python_students | sql_students)

print("Students enrolled in exactly one course:")
print(python_students ^ sql_students)


# Task 2: Employee Skills Management

team_a_skills = {"Python", "SQL", "Git", "Docker"}
team_b_skills = {"Java", "SQL", "AWS", "Git"}

print("\nTeam A Skills:", team_a_skills)
print("Team B Skills:", team_b_skills)

print("Common skills between the teams:")
print(team_a_skills & team_b_skills)

print("Skills available only in Team A:")
print(team_a_skills - team_b_skills)

print("Skills available only in Team B:")
print(team_b_skills - team_a_skills)

print("All skills available in the organization:")
print(team_a_skills | team_b_skills)

team_a_skills.add("Linux")
team_b_skills.remove("Java")

print("Updated Team A Skills:")
print(team_a_skills)

print("Updated Team B Skills:")
print(team_b_skills)


# Task 3: Online Store Customers

amazon_customers = {"Ravi", "Anu", "Kiran", "Sai", "Teja"}
flipkart_customers = {"Sai", "Teja", "Rahul", "Priya", "Anu"}

print("\nAmazon Customers:", amazon_customers)
print("Flipkart Customers:", flipkart_customers)

print("Customers who shopped on both platforms:")
print(amazon_customers & flipkart_customers)

print("Customers who purchased only from Amazon:")
print(amazon_customers - flipkart_customers)

print("Customers who purchased only from Flipkart:")
print(flipkart_customers - amazon_customers)

print("All unique customers:")
print(amazon_customers | flipkart_customers)

print("Customers who purchased from exactly one store:")
print(amazon_customers ^ flipkart_customers)


# Task 4: Programming Languages Survey

batch_1 = {"Python", "Java", "C", "SQL"}
batch_2 = {"Python", "Java", "React", "JavaScript"}

print("\nBatch 1 Languages:", batch_1)
print("Batch 2 Languages:", batch_2)

print("Languages known by both batches:")
print(batch_1 & batch_2)

print("Languages known only by Batch 1:")
print(batch_1 - batch_2)

print("Languages known only by Batch 2:")
print(batch_2 - batch_1)

print("Is Batch 1 a subset of Batch 2?")
print(batch_1.issubset(batch_2))

print("Is Batch 2 a superset of Batch 1?")
print(batch_2.issuperset(batch_1))


# Task 5: Website Visitor Analysis

day_1_visitors = {"user1", "user2", "user3", "user4", "user5"}
day_2_visitors = {"user3", "user4", "user5", "user6", "user7"}

print("\nDay 1 Visitors:", day_1_visitors)
print("Day 2 Visitors:", day_2_visitors)

print("Returning visitors:")
print(day_1_visitors & day_2_visitors)

print("Visitors who visited only on Day 1:")
print(day_1_visitors - day_2_visitors)

print("Visitors who visited only on Day 2:")
print(day_2_visitors - day_1_visitors)

print("All unique visitors across both days:")
print(day_1_visitors | day_2_visitors)

print("Visitors who visited on exactly one day:")
print(day_1_visitors ^ day_2_visitors)