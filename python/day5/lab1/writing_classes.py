
#(1)
class Student:

     def __init__(self,name,age,curclass):
        self.studentname=name
        self.studentage=age
        self.currentclass=curclass #(2)
        
     def avgTestScore(self,mark1,mark2,mark3): #(2)
         avg = (mark1+mark2+mark3)/3
         return avg
        

ashley = Student("Ashley",16,"maths")
jake = Student("jake",15,"ict")

print(ashley.studentage)

#(2)
print(ashley.avgTestScore(50,47,80))