"""
This program demonstrates the strategy pattern using composition.

This program allows for a help ticket system to be supplied
different "strategies" for processing help tickets that are
in the help desk.
"""
import string
import random
from abc import ABC
from abc import abstractmethod


def generate_id(length=8):
    """Free function to simply generate a random id for each ticket"""
    # helper function for generating an id
    return ''.join(random.choices(string.ascii_uppercase, k=length))


class SupportTicket:
    """
    Simple data class (sometimes called a POD (plain old data) class)
    to hold data about a support ticket.

    Attributes:
        id (str): Identifier of the help ticket
        customer (str): Name of the person who placed the help ticket
        issue (str): Description of the issue for the ticket
    """
    def __init__(self, customer, issue):
        self.id = generate_id()
        self.customer = customer
        self.issue = issue


class TicketOrderingStrategy(ABC):
    """
    Abstract base class to provide a consistent interface for each
    strategy.
    """


    @abstractmethod
    def create_ordering(self, list):
        """
        function to establish an ordering for a list of suport tickets

        Args:
            list: collection of all help tickets
        Returns:
            a new list in the proper order
        """
        pass


class FIFOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list):
        return list.copy()


class FILOOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list):
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy


class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list):
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy


class BlackHoleStrategy(TicketOrderingStrategy):
    def create_ordering(self, list):
        return []


class CustomerSupport:
    """
    Customer support help ticket system. Store and manage help tickets

    Attributes:
        tickets (List[SupportTicket]): list of all help tickets
    """


    def __init__(self, processing_strategy):
        self.tickets = []
        self.processing_strategy = processing_strategy


    def create_ticket(self, customer, issue):
        """
        Add a new help ticket to the list.

        Args:
            customer (str): Name of the person who submitted the ticket
            issue (str): Description of the problem in the ticket
        """
        self.tickets.append(SupportTicket(customer, issue))


    def process_tickets(self):
        """
        Process all help tickets using the ordering strategy provided

        Args:
            ordering (func): a function to determine how the support
                tickets will be processed.
        """
        # create the ordered list
        ticket_list = self.processing_strategy.create_ordering(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            self.process_ticket(ticket)


    def process_ticket(self, ticket):
        """
        Process a single ticket to complete the ticket

        Args:
            ticket (SupportTicket): help ticket to be processed
        """
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")


# create the application
app = CustomerSupport(RandomOrderingStrategy())

# register a few tickets
app.create_ticket("John Smith", "My computer makes strange sounds!")
app.create_ticket("Linus Sebastian", "I can't upload any videos, please help.")
app.create_ticket("Arjan Egges", "VSCode doesn't automatically solve my bugs.")

# process the tickets
app.process_tickets()
