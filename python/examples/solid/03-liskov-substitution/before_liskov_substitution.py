# This code violates the liskov substitution principle
# as abstract class interface assumes that a security
# code is required for all of the payment methods. However,
# if we look at the PayPal method, we only need an email
# address. The liskov principle states that "An Object in a
# program should be replaceable with an instance of subtypes
# without affecting program correctness." The Paypal payment
# class does not require an security code, and as such the
# behavior of the pay method in the super class does not
# fit with this subclass type.
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
    def pay(self, order, security_code):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code):
        print("Processing paypal payment type")
        print(f"Using email address: {security_code}")
        order.status = "paid"


def main():
    order = Order()
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)

    print(order.total_price())
    processor = PaypalPaymentProcessor()
    processor.pay(order, "dguarnera@wooster.edu")


if __name__ == "__main__":
    main()
