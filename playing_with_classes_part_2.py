# def func():

#     global a
#     print('Value of a is: ',a)
#     a = 50
#     print('Updated local Value of a is: ',a)
# # When the compiler see it for the first time then compiler treat a as a global variable and assign value to it but then when func() call value will be modified.
# a = 25
# print('Updated global Value of a is: ',a)
# func()

# 🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎
# class Student:
#     def __init__(self):

#         self.student_name = 'Terrance Morales'
#         self.marks = 93
# print(f"Student Name: {getattr(Student,'student_name')}")
# print(f"Marks: {getattr(Student, 'marks')}")

# 🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎
# class Staff:
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def show_details(self):
#         print("Salary: ", self.salary)
#         print("Role:", self.role)
#         print("Department:", self.dept)
#         print("Uniform: ",self.uniform)


# class Teacher(Staff):
#     def __init__(self, role, dept, salary, uniform):
#         super().__init__(role, dept, salary)

#         self.uniform = uniform


# teacher = Teacher(
#     role="Teacher",
#     dept="Computer science",
#     salary="80K",
#     uniform="White Shirt & blue Jeans",
# )

# teacher.show_details()
# # To find whether the teacher instance belong to Staff or not because Staff class is the parent class of teacher
# print(isinstance(teacher,Staff))
# # To check whether Staff is the subclass of Teacher class or not (It will show false )
# print(issubclass(Staff,Teacher))

# 🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎
# Create a class Teacher with name, age, and salary attributes, where salary must be a private attribute that cannot be accessed outside the class.
# class Teacher:

#     def __init__(self,name,age,salary):
#         self.name = name
#         self.age = age
#         self.__salary = salary

#     def show_detail(self):
#         print('Name: ',self.name)
#         print('Age: ',self.age)
#         print('Salary: ',self.__salary)

# teacher = Teacher(name='AsadPro3.1',age=23,salary=35000)
# # teacher.show_detail()

# # The following will not be accessible bcz it's private
# # print(teacher.__salary)

# # Below code will show all the attribute of the Teacher class belongs to it.
# print(dir(Teacher))


# 🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎🌎
# Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method.


class Stack:
    def __init__(self):

        self.__stack = []

    def push(self, item):
        """Push method will push item to the stack"""
        self.__stack.append(item)

    def pop(self):
        remove_item = self.__stack.pop()
        print("Popped item: ", remove_item)

    def traverse(self):
        for item in self.__stack:
            print(f"Item: {item} Digit address: ", id(item))
            # Showing the memory address of a variable
            print(f"Item: {item} Memory address: ", hex(id(item)))

    def show_className(self):
        print("Class name is: ",self.__class__.__name__)


stack = Stack()

# push item to the stack
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)

# pop items from the stack
stack.pop()
stack.pop()

stack.traverse()

stack.show_className()