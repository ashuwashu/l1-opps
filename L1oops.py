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
        

    def show_details(self):


