
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __ge__(self, other):
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2
        if m1 > m2 :
            return True
        return False

s1 = Student(20, 40)

s2 = Student(10,30)

s3 = Student.__add__(s1, s2)


if s1.__ge__(s2):
    print('s1 is win')
else:
    print('s2 is win')