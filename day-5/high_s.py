student_score = input("Input a list of student score ").split()
for n in range(0, len(student_score)):
  student_score[n] = int(student_score[n])

high_score = 0
for score in student_score:
  if score > high_score:
    high_score = score
print(f"The high score is {high_score}")