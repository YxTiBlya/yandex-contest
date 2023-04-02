n, m = map(int, input().split())
students = list(map(int, input().split()))
dt = {student: 0 for student in students}
students.sort()

maxv = 1
right = 1
for left in range(len(students)):
    while right < len(students) and students[right] - students[left] <= m:
        right += 1
    maxv = max(maxv, right-left)

curr = 1
for student in students:
    dt[student] = curr
    curr += 1
    if curr > maxv:
        curr = 1

print(maxv)
for k, v in dt.items():
    print(v, end=" ")