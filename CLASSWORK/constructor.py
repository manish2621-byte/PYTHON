# class student :
#     def __init__(self,name,email,age):
#         self.name=name
#         self.email=email
#         self.age=age
        
#     def display(self):
#         print(self.name,self.email,self.age)
        
# s= student("vivek","vivek@example.com",22)
# s.display()

# s= student("manish","manish@example.com",25)
# s.display()



# class product :
#     def __init__(self,price,quantity,product_name):
#         self.price=price
#         self.quantity=quantity
#         self.product_name=product_name

#     def display(self):
#         print(self.product_name, self.price, self.quantity)
        
# p= product(10000,5,"samsung tv")
# p.display()

# p= product(5000,10,"samsung mobile")
# p.display()

class student :
    
    #class attribute
    clg = 'SDCET'
    
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
        
    def display(self):
        print(self.name,self.email,self.age,self.clg)
        
    @classmethod
    def run(cls):
        print(cls.clg)
        
    @staticmethod
    def show():
        print("show calling")

student.clg = 'SDCET'
s = student("vivek","vivek@example.com",22)
s.display()
student.run()
student.show()
        
        
