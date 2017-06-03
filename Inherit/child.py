from parent import Parent

class Child(Parent):
    def __init__(self, name, ethnicity, wealth):
        print("Child Constructor called")
        Parent.__init__(self, name, ethnicity)
        self.wealth = wealth

ford = Child("Harrison", "White", "$2B")
print(ford.name, ford.wealth)
        
