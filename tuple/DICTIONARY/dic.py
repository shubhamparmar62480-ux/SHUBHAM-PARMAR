student = {
    "name" : "shubham",
    "age" : 19,
    "course" : "AIML",
    "marks" : 85
}

print(student)

print(student["name"])

print(student.keys())# sari keys print karega

print(student.values()) # sari values print karega

print(student.items()) # key + value dono print karega


student = {
    "name" : "shubham",
    "age" : 19,
    "course" : "AIML",
    "marks" : 85
}

student.update({"city" : "bhopal"})# new value add/update
print(student)


student = {
    "name" : "shubham",
    "age" : 19,
    "course" : "AIML",
    "marks" : 85
}

print(student.get("age"))# key ki value batata hai


student = {
    "name" : "shubham",
    "age" : 19,
    "course" : "AIML",
    "marks" : 85
}

student.pop("marks")# key delete karta hai
print(student)


student = {
    "name" : "shubham",
    "age" : 19,
    "course" : "AIML",
    "marks" : 85
}
