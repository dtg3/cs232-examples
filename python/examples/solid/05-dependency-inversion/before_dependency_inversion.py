# This code violates the dependency inversion principle.
# Since the SMSAuthorizor class in a concrete implementation
# the only type of Authorizor we have is for SMS. If we need
# to allow for any other method of payment authorization we
# have no abstract base class or interface on which to base
# our specific implementations. This limits our ability to
# have a shared consistent interface for other classes.
from abc import ABC
from abc import abstractmethod

class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"


    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)


    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

class SMSAuthorizer:

    def __init__(self):
        self.authorized = False


    def verify_code(self, code):
        print(f"Verifying SMS code {code}")
        self.authorized = True


    def is_authorized(self):
        return self.authorized


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: SMSAuthorizer):
        self.security_code = security_code
        self.authorizer = authorizer
    

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code


    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentProcessor(PaymentProcessor):

    def __init__(self, email_address, authorizer: SMSAuthorizer):
        self.email_address = email_address
        self.authorizer = authorizer


    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"


def main():
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)

    print(order.total_price())
    authorizer = SMSAuthorizer()
    authorizer.verify_code(465839)
    processor = PaypalPaymentProcessor("dguarnera@wooster.edu", authorizer)
    processor.pay(order)


if __name__ == "__main__":
    main()
