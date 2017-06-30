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

def run():
    Kim_Ji_Eun = Contact('김지은', '서울대학교', '인문학부', '01028208432')
    Kim_Tae_Hoon = Contact('김태훈', '한양대학교', '정보시스템학과', '01077100271')
    Kim_Ji_Eun.print_info()

if input("What's your name: ") == self.name:
    print_info()


if __name__ == "__main__":
    run()