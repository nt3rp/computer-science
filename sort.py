def quick_sort(items):
    # This implementation will use more memory than necessary
    # as we create new lists. We could *not* do this, but the below
    # is pretty simple code.

    # TODO: Do this creating as few lists as possible.
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

def selection_sort(items):
    """
    Iterate through a list to find the smallest element.

    Then, find the next small it and insert it at the correct location.
    And so on.
    """

    results = []

    while items:
        min_v = None
        for item in items:
            if min_v is None or item < min_v:
                min_v = item
        results.append(min_v)
        items.remove(min_v)

    return results

def insertion_sort():
    """
    Starting with the second element, insert that element where it belongs.

    I.e. anything past the pivot is a new frontier to be moved into the
    'sorted' area
    """
    pass
