import sys


class Student:
    counter = 0
    school = 'alnjar'
    laptop = ''

    def __init__(self, name, age, gender, laptop):
        self.name = name
        self.age = age
        self.gender = gender
        self.laptop = laptop

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

    def info(self):
        print(
            f'welcome {self.name} your gender is {self.gender}, age is {self.age}, your school is {self.school} ')

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
        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def info(self):
            print(f'the brand is {self.brand} and cpu is {self.cpu}, ram is {self.ram}')


class Course:
    pass


s = Student('anas', 19, 'male', Student.Laptop('msi', 'i7', '16'))
s.info()
s.laptop.info()

s2 = Student('karam', 30, 'male', Student.Laptop('hp', 'i5', '8'))
s2.info()
s2.laptop.info()

s3 = Student('nes', 30, 'female', Student.Laptop('hp', 'i5', '8'))
s3.info()
s3.laptop.info()

# sys.exit()
# students = []
# num = int(input('enter the number of student: '))
#
# for i in range(num):
#     name = input(f'enter the name of student{i + 1}) ')
#     age = int(input(f'enter the age of student{i + 1}) '))
#     gender = input(f'enter the gender of student{i + 1}) ')
#     student = Student(name, age, gender)
#     Student.setCounter()
#     students.append(student)
#     print('##########################################################################################')
#
# for student in students:
#     student.info()
