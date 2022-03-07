# This code adheres to the the interface segregation principle.
# Unlike the other solution that used inheritance to solve the
# problem, this version favors a composition based solution.
# While we are only using the one PaymentProcessor abstract
# base class, notice how we have moved the authorization
# functionality out of the Payment Processor and into it's own
# class (SMSAuthorizer). This allows us to flatten the class
# hierarchy by allowing other classes to contain an instance of the
# SMSAuthorizer class to support this feature when necessary.
# Another advantage is that the method of SMSAuthentication can be
# further abstracted so that the PaymentProcessor subclasses only
# need to ensure that they use the SMSAuthorizer object to verify
# the SMS code without having to be concerned about the
# implementation details.
from abc import ABC, abstractmethod


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

    # This -> is a function return type hint
    # in Python indicating that a boolean is the
    # expected return value. This is mostly for
    # documentation, code clarity, and to
    # assist other python tools.
    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    # This notation of variable: type is also a type hint
    # for function/method parameters. Again, it serves the
    # same purpose as the return type hints.
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
    processor = PaypalPaymentProcessor("hi@arjancodes.com", authorizer)
    processor.pay(order)


if __name__ == "__main__":
    main()
