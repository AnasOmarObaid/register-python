import sys


class Student:
    counter = 0
    school = 'alnjar'
    laptop = ''

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def getNme(self):
        return self.name

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setGender(self, gender):
        self.gender = gender

    def getGender(self):
        return self.gender

    def setLaptop(self, laptop):
        self.laptop = laptop

    def getLaptop(self):
        return self.laptop

    def info(self):
        print(
            f'welcome {self.name} your gender is {self.gender}, age is {self.age}, your school is {self.school} ')

    def checkLaptop(self):
        if self.laptop == '':
            return False
        return True

    @classmethod
    def setCounter(cls):
        cls.counter += 1

    @classmethod
    def getCounter(cls):
        return cls.counter

    @staticmethod
    def printInfo():
        print('this is student class.................')

    class Laptop:
        student = ''

        def __init__(self, brand, cpu, ram, student):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram
            self.student = student

        def info(self):
            print(f'the brand is {self.brand} and cpu is {self.cpu}, ram is {self.ram}, this laptop belong to {self.student.getNme()}')

class Course:
    pass

students = []

num = int(input('enter the number of student: '))

for i in range(num):
    name = input(f'enter the name of student {i + 1}) ')
    age = int(input(f'enter the age of student {i + 1}) '))
    gender = input(f'enter the gender of student {i + 1}) ')
    student = Student(name, age, gender)
    Student.setCounter()
    ask = input('###### do you want add laptop from this student? answer y or y ######: ')
    if ask.lower() == 'yes' or ask.lower() == 'y':
        brand = input('enter the brand: ')
        cpu = input('enter the type of cpu: ')
        ram = int(input('enter the number of ram: '))
        student.setLaptop(Student.Laptop(brand, cpu, ram, student))
    students.append(student)
    print('##########################################################################################')

for student in students:
    student.info()
    if student.checkLaptop():
        student.getLaptop().info()
