# This code adheres to the dependency inversion principle.
# We now have an abstract base class on which we base all of the
# classes related to Authorization so we can easily add new
# verification class and provide a shared interface so they
# can be used interchangably.
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

class Authorizer(ABC):
    # This -> is a function return type hint
    # in Python indicating that a boolean is the
    # expected return value. This is mostly for
    # documentation, code clarity, and to
    # assist other python tools. This is especially
    # helpful when you write an abstract method
    # where there is no implementation.
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class Authorizer_SMS(Authorizer):

    def __init__(self):
        self.authorized = False


    def verify_code(self, code):
        print(f"Verifying SMS code {code}")
        self.authorized = True


    def is_authorized(self):
        return self.authorized

class Authorizer_Google(Authorizer):

    def __init__(self):
        self.authorized = False


    def verify_code(self, code):
        print(f"Verifying Google auth code {code}")
        self.authorized = True


    def is_authorized(self):
        return self.authorized

class Authorizer_Robot(Authorizer):

    def __init__(self):
        self.authorized = False


    def not_a_robot(self):
        self.authorized = True


    def is_authorized(self):
        return self.authorized


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):
    # This notation of variable: type is also a type hint
    # for function/method parameters. For this
    # function the hint indicates that the authorizer
    # parameter should be of type Authorizer. This is
    # mostly for documentation, code clarity, and to
    # assist other python tools.
    def __init__(self, security_code, authorizer: Authorizer):
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
    def __init__(self, email_address, authorizer: Authorizer):
        self.email_address = email_address
        self.authorizer = authorizer


    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"


def main():
    # Now we can take any authorizor
    order1 = Order()
    order1.add_item("Keyboard", 1, 50)
    order1.add_item("SSD", 1, 150)
    order1.add_item("USB cable", 2, 5)

    order2 = Order()
    order2.add_item("GPU", 1, 2000)
    order2.add_item("Bluetooth Mouse", 1, 50)
    order2.add_item("CPU", 2, 300)

    #   Robot Authorizor    
    authorizer = Authorizer_Robot()
    authorizer.not_a_robot()
    processor = PaypalPaymentProcessor("dguarnera@wooster.edu", authorizer)
    processor.pay(order1)
    print(f"Payment: ${order1.total_price()}")

    #   Google Authorizor
    authorizer = Authorizer_Google()
    authorizer.verify_code('myfakecode')
    processor = DebitPaymentProcessor("dguarnera@wooster.edu", authorizer)
    processor.pay(order2)
    print(f"Payment: ${order2.total_price()}")


if __name__ == "__main__":
    main()
