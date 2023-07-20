# Exercise 1

students = [
    'Alex',
    'Aaron',
    'Andrew',
    'Carneala',
    'Cesar'
]

print(f"The second student's name is {students[1]}")

# Exercise 2

foods = ('apple', 'burger', 'cake', 'rice', 'steak')
for food in foods:
    print(f"{food} is a good food")

# Exercise 3

for food in foods[-2:]:
    print( f"{food}" )

this is how i originally solved it prior to reading the 'Using for loop':
last_two_foods = foods[-2:]
print( f"{last_two_foods}" )

# Exercise 4

home_town = {
    'city': 'Chicago',
    'state': 'Illinois',
    'population': 2665000
}

print( f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}" )

# Exercise 5

for key, val in home_town.items():
    print( f"{key} = {val}" )

# Exercise 6

cohort = []
for idx, student in enumerate(students):
    
    cohort.append({
        'student': student,
        'fav_food': foods[idx]
        })
    
for item in cohort:
    print(item)

# Exercise 7

awesome_students = [f"{student} is awesome!" for student in students]
print(awesome_students)

for awe_stu in awesome_students:
    print(awe_stu)

# Exercise 8

contains_a_foods = [f"{food} contains letter a" for food in foods if 'a' in food]
# print(contains_a_foods)
for food in contains_a_foods:
    print(food)

 



