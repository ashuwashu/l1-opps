class Pet():
    def __init__(self):
        print("A new pet as been created")
        self.name=""
        self.type=""
        self.age=0
        self.breed=""
        self.origin=""

    def enter_details(self):
        print("Enter the pet name🐾:")
        self.name=input()
        print("Enter pet type")
        self.type=input()
        print("Enter pets age")
        self.age=input()
        print("enter the breed of the chosen animal")
        self.breed=input()
        print("where is your pets origin?")
        self.origin=input()
        

    def show_details(self):
        print("Pet Details")
        print("Pet Name Is:", self.name)
        print("Pet Type Is:", self.type)
        print("Pet Age Is:", self.age)
        print("Pet breed Is:", self.breed)
        print("Pet Origin Is:", self.origin)



pet1 = Pet()
pet1.enter_details()
pet1.show_details()


