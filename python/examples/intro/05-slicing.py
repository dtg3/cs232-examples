"""Slicing and Indices

Demonstration of using Python
indices and slicing for iterables
"""


def indexingExample(container):
    """Accessing elements
    
    Args:
        container (iterable): Any indexable container
    """

    # Containers that can be indexed can use both
    # positive and negative values.
    # Positive indexing moves "forward" in the
    # container (left -> right)
    # ---------------------------
    # | 0 | 1 | 2 | 3 | ... | n |
    # ---------------------------
    # Negative indexing moves "backward" in the
    # container (right -> left)
    # ---------------------------
    # | -n | ... | -3 | -2 | -1 |
    # ---------------------------
    # Positive indexes go from 0 to length-1
    print(container[0])
    print(container[len(container) - 1])
    # Negative indexes go from -1 to -length
    print(container[-1])
    print(container[-len(container)])
    # Any values that are too positive or negative
    # will result in an error


def slicingExample(container):
    """Slicing allows you to take a linear
    subset of a container to produce a new
    container:

    container[start:stop:step]

    Note that the stop index is NOT inclusive
    
    Args:
        container (iterable): Any indexable container
    """

    print(container[0:3])

    # The starts and ends are optional
    print(container[:]) # Slice beginning to end
    print(container[1:]) # Slice index 1 to the end
    print(container[:3]) # Slice beginning to index 2
    print(container[-2:]) # Slice second to last to end

    # The step controls how we increment to the next item
    print(container[::2]) # Slice every other item
    print(container[-1::-1]) # Slice in reverse!


def main():
    # Iterable data types that can be
    # used with indexing and slicing
    my_string = "Hello World!"
    my_list = ["apples", "oranges", "pears", "bananas", "berries"]
    my_tuple = ("a", "b", "c", "d", "e")

    indexingExample(my_string)
    indexingExample(my_list)
    indexingExample(my_tuple)

    slicingExample(my_string)
    slicingExample(my_list)
    slicingExample(my_tuple)

if __name__ == "__main__":
    main()
