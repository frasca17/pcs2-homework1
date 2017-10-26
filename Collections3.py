from collections import namedtuple
n = int(input())
columns = input()
Student = namedtuple('Student', columns)
students = []
for i in range(n):
    s = input().split()
    students.append(Student(*s))

print(sum([int(s.MARKS) for s in students])/len(students))