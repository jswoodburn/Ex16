from person import Person

class Customer(Person):

    def __init__(self, first_name, surname, age, email, postcode, phone_number, order_number):
        super().__init__(first_name, surname, age, email)
        self.postcode = postcode
        self.phone_no = phone_number
        self.order_no = order_number

    def make_phone_no_uk(self):
        return f"+44 {self.phone_no[1:5]}-{self.phone_no[5:8]}-{self.phone_no[8:]}"

