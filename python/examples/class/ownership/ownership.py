"""
This program demonstrates the idea of object ownership.

After running this program you will see text added to the files shared_log.txt
and list_three_log.txt. If these files did not exist before this program was
run they will be created. If they already exist messages will be appended to
these files.
"""

from datetime import datetime


class Logger:
    """
    Provides logging functionality. Log messages are appended to the file with
    the name given to the intializer.
    """

    def __init__(self, log_filename):
        """
        Initialize a Logger object.

        Args:
            log_filename (str): name of the file to write to
        """
        self._log_filename = log_filename

    def log(self, message):
        """
        Log a message. Messages will be logged with the following format:

        <timestamp> <message>

        Args:
            message (str): the message to log
        """
        with open(self._log_filename, 'a') as f:
            log_line = '{} {}\n'.format(datetime.now(), message)
            f.write(log_line)


class ItemList:
    """
    Keeps track of a list of items. Each time an item is added to the list,
    a message is logged.
    """
    def __init__(self, list_name, logger):
        """
        Initialize an ItemList.

        Args:
            list_name (str): the name of the list
            logger (Logger): Logging object used to write log messages
        """
        self._list_name = list_name
        self._list = []
        self._logger = logger

    def add_item(self, item):
        """
        Add an item to the list. This action is logged.

        Args:
            item: item to add to the list
        """
        self._list.append(item)
        message = '{} added to list {}'.format(item, self._list_name)
        self._logger.log(message)

    def get_list(self):
        """
        Return the list of items.

        :return: list of items
        """
        return self._list


def main():
    # This Logger object will write to shared_log.txt and will be shared by
    # two ItemList objects. Neither of the lists will own this object.
    shared_logger = Logger('shared_log.txt')

    list_one = ItemList('List One', shared_logger)
    list_two = ItemList('List Two', shared_logger)

    # Here we create an ItemList and create its logger within the call to the
    # initializer. The only reference to the logger created here will be
    # stored within this ItemList, and when the ItemList ceases to exist so
    # will the logger. The logger created here will be owned by the ItemList.
    list_three = ItemList('List Three', Logger('list_three_logger.txt'))

    # After the next 3 lines are executed, 2 lines will be appended to
    # shared_log.txt and one line will be appended to list_three_logger.txt
    list_one.add_item('Bananas')
    list_two.add_item('Oranges')
    list_three.add_item('Grapes')


if __name__ == '__main__':
    main()
