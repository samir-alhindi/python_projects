studentGrades: dict = {"Samir" : 9999999,
                       "Yahya" : 100,
                       "Abdulrahman" : 150,
                       "Muhammed khair" : 100,
                       "Malaz" : 200,
                       "Mustafa" : 200,}

#Prints keys:
for name in studentGrades:
    print(name)

#prints the values:
for grade in studentGrades:
    print(studentGrades.get(grade))

#print the key value pairs:
for key in studentGrades:
    print(f"{key} : {studentGrades.get(key)}")