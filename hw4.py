class Contact:
    def __init__(self, name, school, major, phone_number):
        self.name = name
        self.school = school
        self.major = major
        self.phone_number = phone_number

    def print_info(self):
        print("Name: ", self.name)
        print("School: ", self.school)
        print("Major: ", self.major)
        print("Phone_number: ", self.phone_number)


if input("What's your name: ") == Contact().name:
    print_info()
