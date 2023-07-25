student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

totals = 0
for height in student_heights:
    totals += height
#print(totals)

no_items = 0
for item in student_heights:
    no_items += 1
#print(no_items)

average = round(totals / no_items)
print(average)