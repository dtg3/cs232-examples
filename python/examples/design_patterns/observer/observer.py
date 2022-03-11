"""
This program demonstrates the observer design pattern.

This program allows classes to subscribe to a "subject" (some
kind of class that can provide information) and observe changes
made to the state of the subject. The subject is responsible for
notifying the observers so they can take actions based on the
content.
"""
from abc import ABC
from abc import abstractmethod
import os


class Subject(ABC):
    """
    Subject abstract base class defines the core interface
    for all Subject subclasses
    """


    @abstractmethod
    def attach(self, observer) -> None:
        """
        The attach function is responsible for adding new observers
        that can be notified in changes to the subject

        Args:
            observer (Observer): An observer that can be added to the 
                subject for the state
        """
        pass


    @abstractmethod
    def detach(self, observer) -> None:
        """
        The detach function is responsible for removing observers
        from the subject to prevent them from receiving subject
        notifications

        Args:
            observer (Observer): The observer to be removed from the
                subject
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        The notify function will contact all observers to let them know
        that new subject state information is available
        """
        pass


class LogData(Subject):
    """
    LogData is a concrete Subject that reads log data from
    a file to notify observers of data from that file.


    Attributes:
        message (str): Data read from a log file
        _observers (List[Observers]): Observers that are subscribed to
            the LogData subject
        _log_filename (str): file name of the log file
    """


    def __init__(self, log_filename):
        self.message = None
        # Note that observer subscriber "lists" can be organized in more
        # comprehensive ways stored (categorized by event type, data, etc.).
        # This list is just one type of (simple) approach.
        self._observers = []
        self._log_filename = self._get_absolute_file_path(log_filename)


    def attach(self, observer) -> None:
        print(f"Attach {type(observer).__name__} observer")
        self._observers.append(observer)


    def detach(self, observer) -> None:
        print(f"Remove {type(observer).__name__} observer")
        self._observers.remove(observer)


    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)


    def read_log_file(self) -> None:
        """
        Process the input log file to read in data and notify
        subject observers of new data received.

        Usually, the subscription logic is only a fraction of what a Subject
        can do. Subjects commonly hold some important business logic (like
        this function) that triggers a notification method whenever something
        important is about to happen (or after it).
        """
        with open(self._log_filename, 'r') as input_file:
            for line in input_file:
                self.message = line.strip()
                self.notify()


    def _get_absolute_file_path(self, filename):
        """
        Helper function to locate the absolute path of the filename
        based on the location of this script.

        Args:
            filename (str): name of the log text file 
        """
        absolute_path_to_script = os.path.realpath(__file__)
        absolute_path_to_directory = os.path.dirname(absolute_path_to_script)
        return os.path.join(absolute_path_to_directory, filename)


class Observer(ABC):
    """
    Observer abstract base class defines the core interface
    for all observer subclasses
    """


    @abstractmethod
    def update(self, subject) -> None:
        """
        Update describes what action should be taken when an observer
        is notified of new subject state content.

        Args:
            subject (Subject): The subject instance that contains data for the
                observer to utilize on update.
        """
        pass


class ErrorListener(Observer):
    """
    ErrorListener only responds to ERROR messages in the log file
    """


    def update(self, subject) -> None:
        if "ERROR" in subject.message:
            print(f"{self.__class__.__name__} received: \"{subject.message}\"")


class LogListener(Observer):
    """
    LogListener responds to any type of message in the log file
    """


    def update(self, subject) -> None:
        print(f"{self.__class__.__name__} received: \"{subject.message}\"")


def main():
    subject = LogData("log.txt")
    error_observer = ErrorListener()
    subject.attach(error_observer)
    log_data_observer = LogListener()
    subject.attach(log_data_observer)
    subject.read_log_file()

    # Only Error Listener
    subject.detach(log_data_observer)
    subject.read_log_file()


if __name__ == "__main__":
    main()
