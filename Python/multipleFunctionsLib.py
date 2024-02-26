class FunctionAllMethods:
    def Subfields():
        lists = [
        "Machine Learning",
        "Neural Networks",
        "Vision",
        "Robotics",
        "Speech Processing",
        "Natural Language Processing"
        ]
        return lists
     # Create a function that checks whether the given number is Odd or Even
    def OddEven(number):
        if number % 2 == 0:
            return number
        else:
            return 0
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
