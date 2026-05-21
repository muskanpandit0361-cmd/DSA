class Student:
    @staticmethod    #decorator
    def get_personal_detail(firstname,lastname):
        print("your personal detail= ",firstname,lastname)

    @staticmethod
    def contact_details(mobil_no,roll_no):
        print("your contact detail= ",mobil_no,roll_no)

Student.get_personal_detail("Muskan","Pandit")
Student.contact_details(9876543210,27)            