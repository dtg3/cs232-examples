"""
This program demonstrates the template method pattern.

This program simulates the a Crypto currency trading
application that helps you decide if you should buy,
sell, or do nothing with the coins.
"""
from abc import ABC
from abc import abstractmethod


class TradingBot(ABC):
    """
    Trading bot clas will allow users to determine trading advice
    for cryptocurrencies based on (artifical) trend data.

    The majority of the trading process is in place with the
    exception of a few functions should_buy() and should_sell().
    These two functions are the template methods that are
    overridden to provide unique features from each subclass, but
    are intended to work within the structure already in place,
    in this case the check_prices() function.
    """


    def connect(self):
        """Simple print function to indicate the process is starting"""
        print(f"Connecting to Crypto exchange...")


    def get_market_data(self):
        """Collect fake crypto market data"""
        return [10, 12, 18, 14]


    def check_prices(self, coin):
        """
        Function that uses the template methods in order to provide
        the Crypto currency advice

        Args:
            coin (str): a simple string that represents the currency
                in question (only used for the print statements)
        """
        self.connect()
        prices = self.get_market_data()
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}!")
        elif should_sell:
            print(f"You should sell {coin}!")
        else:
            print(f"No action needed for {coin}.")


    @abstractmethod
    def should_buy(self, prices) -> bool:
        """
        Template method to provide the Crypto currency advice

        Args:
            prices (List[int]): the historical list of currency values
        Returns:
            bool: true of false indication for buying the currency
        """
        pass


    @abstractmethod
    def should_sell(self, prices) -> bool:
        """
        Template method to provide the Crypto currency advice

        Args:
            prices (List[int]): the historical list of currency values
        Returns:
            bool: true of false indication for selling the currency
        """
        pass


class AverageTrader(TradingBot):
    """
    Average trader bot checks how the average currency price compares
    to the most recent values (last item in list)
    """


    def list_average(self, price_list):
        """
        Helper function to calculate the average price of all currency
        values in the list

        Args:
            price_list (List[int]): the historical list of currency values
        Returns:
            float: the average of the currency values in price_list
        """
        return sum(price_list) / len(price_list)


    def should_buy(self, prices):
        """
        Determine if the average curreny price makes the currency worth buying

        Args:
            price_list (List[int]): the historical list of currency values
        Returns:
            bool: is the most recent currency value less than the average price
        """
        return prices[-1] < self.list_average(prices)


    def should_sell(self, prices):
        """
        Determine if the average curreny price makes the currency worth selling

        Args:
            price_list (List[int]): the historical list of currency values
        Returns:
            bool: is the most recent currency value more than the average price
        """
        return prices[-1] > self.list_average(prices)


class MinMaxTrader(TradingBot):
    """
    MinMax trader bot checks how the current currency price
    (last item in list) compares largest and smallest values
    in the list 
    """


    def should_buy(self, prices):
        """
        Determine if the current currency price is the same as the
        lowest curreny price

        Args:
            price_list (List[int]): the historical list of currency values
        Returns:
            bool: is the most recent currency value equal to the minimum value
        """
        return prices[-1] == min(prices)


    def should_sell(self, prices):
        """
        Determine if the current currency price is the same as the
        highest curreny price

        Args:
            price_list (List[int]): the historical list of currency values
        Returns:
            bool: is the most recent currency value equal to the maximum value
        """
        return prices[-1] == max(prices)


def main():
    application = AverageTrader()
    application.check_prices("BTC/USD")


if __name__ == "__main__":
    main()
