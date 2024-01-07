student_names = []
marks = []
no_of_student=int(input("enter number of student:"))
for x in range(0,no_of_student):
   student_name,mark=input("enter a name & mark:").split(" ")
   student_names.append(student_name)
   marks.append(mark)
print(student_names,marks)
index=marks.index(max(marks))
print("the hight mark is:",student_names[index])



