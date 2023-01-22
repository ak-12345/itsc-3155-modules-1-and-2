from gzip import _GzipReader


x = int(input("Enter your grade: "))
# I am thinking java in my head, Never underestimate python and its simplicity
if 90 < x < 100:
    grade = 'A'
elif 80 < x < 89:
    grade = 'B'
elif 70 < x < 79:
    grade = 'C'
elif 60 < x < 69:
    grade = 'D'
else:
    grade = 'F'
print(grade)