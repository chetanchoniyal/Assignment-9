'''Q1'''
'''Defining the Circle class'''
class Circle():
    def __init__(self, rad):
        self.radius = rad
    '''Initializing class with a Radius rad'''

    def getArea(self):
        return self.radius ** 2 * 3.14
    '''getArea() method is used to calculate the Area'''

    def getCircumference(self):
        return 2 * self.radius * 3.14
    '''getCircumferece() method is used to calculate the Circumference'''

NewCircle = Circle(int(input("Enter the Radius: ")))
'''This will create object of Circle class '''
print(NewCircle.getArea())
'''This will calculate and print the area of circle'''
print(NewCircle.getCircumference())
'''This will calculate and print the Circumference of circle'''

'''Q2'''
'''Defining the Student Class'''
class Student():
    def __init__(self):
        self.name = input("Enter the Name of Student: ")

        self.roll = int(input("Enter the Roll number of the Student: "))


    def display(self):
        '''Display method to display Details of Student'''
        print("Name: ", self.name)
        print("Roll Number: ", self.roll)

NewStudent = Student()
'''Creating Object of Student Class'''
NewStudent.display()
'''Calling display() method to print details of students'''

'''Q3'''
class Temprature():
    '''Defining Temprature Class'''
    def convertFahrenheit(self):
        cel = int(input("Enter the Temprature in Celcius: "))
        fah = (cel * 1.8) + 32
        print("Temprature in Fahrenheit: ", fah)
        ''' convertFahrenheit() method to convert Celcius to Fahrenheit'''
    def convertCelsius(self):
        fah = int(input("Enter the Temprature in Fahrenheit: "))
        cel = (fah - 32) / 1.8
        print("Temprature in Celcius: ", cel)
        ''' convertCelcius() method to convert Fahrenheit to Celcius'''

NewTemprature = Temprature()
NewTemprature.convertCelsius()
NewTemprature.convertFahrenheit()

'''Q4'''
class MovieDetails():
    def __init__(self):
        self.name = input("Enter the Name of the Movie: ")
        self.artistname = input("Enter the Name of the Artist: ")
        self.release = input("Enter the Year of Release: ")
        self.ratings = int(input("Enter the Ratings out of 10: "))

    def display(self):
        print("Name: ", self.name)
        print("Artist Name: ", self.artistname)
        print("Year of Release: ", self.release)
        print("Ratings(out of 10): ", self.ratings)

    def update(self):
        self.name = input("Enter the Updated Movie Name: ")
        self.artistname = input("Enter the Updated Name of the Artist: ")
        self.release = input("Enter the Updated Year of Release:")
        self.ratings = input("Enter the Updated Ratings:")
        self.display()

NewMovie = MovieDetails()
NewMovie.display()
NewMovie.update()

'''Q5'''
class Expenditure():
    def __init__(self):
        self.expenditure = int(input("Enter the Expenditure: "))
        self.savings = int(input("Enter the Savings: "))

    def display(self):
        print("Expenditure: ", self.expenditure)
        print("Savings: ", self.savings)

    def calTotalSalary(self):
        self.totalSal = self.expenditure + self.savings

    def displayTotalSalay(self):
        print("Total Salary: ", self.totalSal)

NewExpenditure = Expenditure()
NewExpenditure.display()
NewExpenditure.calTotalSalary()
NewExpenditure.displayTotalSalay()