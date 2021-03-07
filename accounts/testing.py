# from account import Account
#
# jackie = Account("jackie", "woodburn", "1995-05-10")
# print(jackie.name)
# print(jackie.age)
# print(jackie.balance)
#
# amber = Account("amber", "shand", "1997-03-19", "10000")
# print(amber.name, amber.age, amber.balance)
# print(type(amber.get_friendly_balance()))
#
# print(amber.deposit(100))
# print(amber.withdraw(430))
# print(amber.check_balance())


from current_account import CurrentAccount

# jessie = CurrentAccount("jessie", "auguste", "1995-05-10", 1000, 12000, recommended=True)
# print(jessie.check_balance())
#
# print(jessie.no_of_friends)
# print(jessie.recommend_a_friend())
# print(jessie.no_of_friends)
# print(jessie.check_balance())
# print(jessie.recommend_a_friend())
# print(jessie.recommend_a_friend())
# print(jessie.recommend_a_friend())
# print(jessie.recommend_a_friend())
# print(jessie.recommend_a_friend())
# print(jessie.check_balance())
#
# jessie.withdraw(100)
#
# print(jessie.check_balance())
#
# vicky = CurrentAccount("vicky", "QA", "1980-05-10", 1000, 10)
#
# print(vicky.check_balance())
# print(vicky.withdraw(20))
# print(vicky.withdraw(-300))
# print(vicky.withdraw(991))

from savings_account import SavingsAccount

michelle = SavingsAccount("michelle", "obama", "1995-05-10", 2.5, 150)

# print(michelle.withdraw(-1))

print(michelle.calculate_future_value("2031-03-08"))
