beginning = "Hello, class. Yesterday {} students " \
            "finished their class work".format(input("How many students finished their work? "))
marks = {}
results = "I have following marks for today. "
for i in range(int(beginning.split()[3])):
    name = input("Name of {} student: ".format(i+1)).title()
    grade = input("And his/her grade: ")
    marks[name] = grade
    results += f"{name} got {grade}. "

print(beginning)
print(results)
