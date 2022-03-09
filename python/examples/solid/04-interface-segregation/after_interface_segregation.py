# This code adheres to the the interface segregation principle.
# In this instance we break up the single PaymentProcessor abstract
# base class into two. One of these support SMS verification, while
# the other does not. This allows for derived classes needing that
# functionality to inherit from the SMS PaymentProcessor class while others
# can simply use the original PaymentProcessor Class. Note that each
# the SMS version of the PaymentProcessor still inherits from the
# PaymentProcessor base class to ensure that the pay function is still
# implemented. A downside to this implementation is we are starting to
# create a class hierarchy to define subsets of behavior. One for
# SMS and one for non-sms behaviors. This can become problematic if
# there end up being a variety or payment classes needing verification
# methods, or even worse, require a combination of methods.
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


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class PaymentProcessor_SMS(PaymentProcessor):
    # This -> is a function return type hint
    # in Python indicating that a boolean is the
    # expected return value. This is mostly for
    # documentation, code clarity, and to
    # assist other python tools. This is especially
    # helpful when you write an abstract method
    # where there is no implementation.
    @abstractmethod
    def auth_sms(self, code) -> bool:
        pass


    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor_SMS):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False


    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True


    def pay(self, order):
        if not self.verified:
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


class PaypalPaymentProcessor(PaymentProcessor_SMS):
    def __init__(self, email_address):
        self.email_address = email_address
        self.verified = False


    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True


    def pay(self, order):
        if not self.verified:
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
    processor = PaypalPaymentProcessor("dguarnera@wooster.edu")
    processor.auth_sms(465839)
    processor.pay(order)


if __name__ == "__main__":
    main()
