def quick_sort(items):
    n = len(items)

    # Base case
    if n <= 1:
        return items

    # Pick pivot
    pivot = items.pop(n/2)

    less = []
    greater = []

    for v in items:
        if v < pivot:
            less.append(v)
        else:
            greater.append(v)

    return quick_sort(less) + [pivot] + quick_sort(greater)


def merge(left, right):
    """ Nick is really bad at merging """
    return quick_sort(left + right)


def merge_sort(items):
    """
    Divide the set into two groups, until there are only two elements.

    Then, sort on the way up.
    """
    n = len(items)

    # Base case
    if n <= 1:
        return items

    # Split
    mid = n / 2
    left  = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    # Merge
    return merge(left, right)

def selection_sort():
    """
    Iterate through a list to find the smallest element.

    Then, find the next small it and insert it at the correct location.
    And so on.
    """
    pass

def insertion_sort():
    """
    Starting with the second element, insert that element where it belongs.

    I.e. anything past the pivot is a new frontier to be moved into the
    'sorted' area
    """
    pass
