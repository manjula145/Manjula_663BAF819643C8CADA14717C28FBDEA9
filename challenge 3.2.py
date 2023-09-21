class Student :

  def __init__(self,  name,  roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):

  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)


  return sorted_students

students = [                            Student("shyam","A2004",7.8), 
    Student("dhass","A1234",8.9),
    Student("anandhi","A4567",8.1),
    Student("kani","A9876",8.7),]


sorted_students =                              sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll number:{},CGPA:{}".format(student.name,student.roll_number, student.cgpa))
   