class A:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        print("Name:", self.name)
        print("Email:", self.email)
        print("Phone:", self.phone)


class C(A):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


obj = C("Manish", "manish@gmail.com", "9876543210")
obj.display()