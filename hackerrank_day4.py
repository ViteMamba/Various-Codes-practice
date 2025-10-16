class Person:
    def __init__(self,initialAge):
        self.age = initialAge
        
    def age_check (self):
        if (self.age < 0):
            self.age = 0
            print("Age is not valid, setting age to 0.")
    def yearPasses(self):
        self.age+=1        

    def amIold(self):
        if self.age<13:
            print("You are young")
        elif self.age>13 and self.age<18:
                print("You are a teenager.")
        else:
                print("you are old")
                
        self.yearPasses()
        
        if self.age<13:
            print("You are young")
        elif self.age>13 and self.age<18:
                print("You are a teenager.")
        else:
                print("you are old")

n = int(input())
for i in range(n):
    m = int(input())
    
    s = Person(m)
    s.age_check()
    
    s.amIold()
    