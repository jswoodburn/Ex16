from person import Person

# vicky = Person(firstname="Victorious")
# print(vicky.surname)

# vicky = Person("vicky", "QA", "30", "vicky@qa.com")
# print(vicky.age)
# # vicky.change_age(300)
# # print(vicky.age)
#
# vicky.change_surname("woodburn")
# print(vicky.surname)
#
# print(vicky.return_full_name())
#
# print(vicky.mage)
# vicky.mage=31
# print(vicky.mage)

# from employee import Employee
#
# amber = Employee("Amber", "Shand", "23", "amberleeshand@gmail.com", "Tech", "6190658", "1997-02-06", "Junior Software "
#                                                                                                     "Engineer", "100000")
# print(amber.calculate_years_of_service())

from customer import Customer

jackie = Customer("jackie", "woodburn", 25, "jackie.woodburn@gmail.com", "SW19 7AB", "07512656497", "001")
print(jackie.make_phone_no_uk())

print(jackie.return_full_name())
