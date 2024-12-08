marks = (7, 5, 5, 7, 6, 2, 8, 9, 10, 7)

print(marks)
print(marks[2:-2])

for i in range(len(marks)):
  print(i,marks[i])
  
print("The total amount of people who took the test is: ", len(marks))

max_value = max(marks)
print("The best mark in the test is: ",max_value, "out of 10")

min_value = min(marks)
print("The worst mark in the test is: ", min_value, "out of 10")

print("The average score of the test is: ", sum(marks)/len(marks), "out of 10")
print("The range of marks in the test is: ", max_value-min_value, "out of 10")