from abc import ABC, abstractmethod

class Person(ABC):
    school = 'al-esra'
    laptop = ''

    def __init__(self, name, age, gender, pid):
        self.name = name
        self.age = age
        self.gender = gender
        self.pid = pid

    @abstractmethod
    def setName(self, name):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def setAge(self, age):
        pass

    @abstractmethod
    def getAge(self):
        pass

    @abstractmethod
    def setGender(self, gender):
        pass

    @abstractmethod
    def getGender(self):
        pass

    @abstractmethod
    def setPid(self, pid):
        pass

    @abstractmethod
    def getPid(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Student(Person):

    def __init__(self, name, age, gender, pid, course, grade):
        super().__init__(name, age, gender, pid)
        self.course = course
        self.grade = grade

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setGender(self, gender):
        self.gender = gender

    def getGender(self):
        return self.gender

    def setPid(self, pid):
        self.pid = pid

    def getPid(self):
        return self.pid

    def setCourse(self, course):
        self.course = course

    def getCourse(self):
        return self.course

    def setGrade(self, grade):
        self.grade = grade

    def getGrade(self):
        return self.grade

    def setLaptop(self, laptop):
        self.laptop = laptop
        self.laptop.student = self

    def getLaptop(self):
        return self.laptop

    def checkLaptop(self):
        if self.laptop != '':
            return True
        return False

    def info(self):

        print(f'your name is {self.getName()}, your age is {self.getAge()},your gender is {self.getGender()} your pid is {self.pid} ,your course {self.course}, your grade is {self.grade}, your '
              f'school is {self.school}')
        if self.laptop != '':
            self.laptop.info()
            print(f'this laptop belong to {self.getLaptop().getStudent().getName()}')
        else:
            print('this student dont have any laptop!!!')
        print('*************************************************************************************')

    class Laptop:
        student = ''

        def __init__(self, brand, cpu, ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def setBrand(self, brand):
            self.brand = brand

        def getBrand(self):
            return self.brand

        def setCpu(self, cpu):
            self.cpu = cpu

        def getCpu(self):
            return self.cpu

        def setRam(self, ram):
            self.ram = ram

        def getRam(self):
            return self.ram

        def checkLaptop(self):
            if self.student != '':
                return True
            return False

        def setStudent(self, student):
            self.student = student
            self.student.laptop = self

        def getStudent(self):
            return self.student

        def info(self):
            print(f'the laptop brand is {self.brand}, the cpu is {self.cpu}, the ram is {self.ram}')


class Master(Person):
    salary_type = '$'

    def __init__(self, name, age, gender, pid, salary, course):
        super().__init__(name, age, gender, pid)
        self.salary = salary
        self.course = course

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setGender(self, gender):
        self.gender = gender

    def getGender(self):
        return self.gender

    def setPid(self, pid):
        self.pid = pid

    def getPid(self):
        return self.pid


    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setCourse(self, course):
        self.course = course

    def getCourse(self):
        return self.course

    def setSalaryType(self, salary_type):
        self.salary_type = salary_type

    def getSalaryType(self):
        return self.salary_type

    @classmethod
    def changeSalaryType(cls, salary_type):
        cls.salary_type = salary_type

    def info(self):
        print(f'your name is {self.getName()}, your age is {self.getAge()},your gender is {self.getGender()} your pid is {self.pid}, the salary is {self.getSalary()}{self.salary_type}, the courses is {self.getCourse()}')




st = Student('anas', 20, 'male', 23221, 'python', 89)
laptop = Student.Laptop('msi', 'cor i7', 16)
st.setLaptop(laptop)
st.info()


st = Student('wesam', 23, 'female', 23221, 'c++', 89)
laptop = Student.Laptop('dell', 'cor i5', 8)
st.setLaptop(laptop)
st.info()

st = Student('eman', 40, 'female', 23221, 'c++', 89)
laptop = Student.Laptop('apple', 'cor i3', 4)
laptop.setStudent(st)
st.info()
