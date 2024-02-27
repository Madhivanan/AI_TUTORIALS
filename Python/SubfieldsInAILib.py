class SubfieldsInAI():
     # Create a class and function, and list out the items in the list
    def Subfields():
        lists = [
            "Machine Learning",
            "Neural Networks",
            "Vision",
            "Robotics",
            "Speech Processing",
            "Natural Language Processing"
        ]
        for name in lists:
            print(name)
    

    
class OddEven():
     # Create a function that checks whether the given number is Odd or Even
    def oddEven(number):
        if number % 2 == 0:
            return number
        else:
            return 0
        
        
class ElegiblityMarriage():
    # Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female

    def Elegible(gender, age):
        if gender.lower() == "male":
            if age > 21:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif gender.lower() == "female":
            if age > 18:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        else:
            print("Gender not valid")
            

class FindPercent():
    # calculate the percentage of your 10th mark
    

    def percentage():
        Subject1= 98
        Subject2= 87
        Subject3= 95
        Subject4= 95
        Subject5= 93
        total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        print(f"Total : {total}")
        percentage = total / 5
        print(f"Percentage: {percentage}")
        
class Triangle():
    #print area and perimeter of triangle using class and functions

    def triangle():
        height = int(input("Height:"))
        breadth = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        triangle = height * breadth / 2
        print(f"Area of Triangle: {triangle}")
        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        breadth1 = int(input("Breadth:"))
        perimeter = height1 + height2 + breadth1
        print("Perimeter formula: Height1+Height2+Breadth")
        print(f"Perimeter of Triangle: {perimeter}")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
