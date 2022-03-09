# This code violates the interface segregation principle
# as all subclasses of the PaymentProcessor abstract base
# class, must implement the auth_sms method (text message
# verification of payment). The problem is that some of the
# subclasses cannot use this function like the class for 
# Credit card payment. This class has no choice but to
# implement this function, and since there is no acceptable
# behvior it throws an exception if it is used. This is the
# result of trying to tie the interface too closely to the
# implementation and/or create a "one size fits all" abstraction.
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


class DebitPaymentProcessor(PaymentProcessor):
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


    def auth_sms(self, code):
        raise Exception("Credit card payments don't support SMS code authorization.")


    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
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
    processor = DebitPaymentProcessor("2349875")
    processor.auth_sms(465839)
    processor.pay(order)


if __name__ == "__main__":
    main()
