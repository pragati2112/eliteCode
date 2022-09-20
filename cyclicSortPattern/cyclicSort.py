def cycleSort(array):
    writes = 0

    # Loop through the array to find cycles to rotate.
    for cycleStart in range(0, len(array) - 1):
        item = array[cycleStart]
        pos = cycleStart

        # Find where to put the item.
        for i in range(cycleStart + 1, len(array)):
            if array[i] < item:
                pos += 1

        # If the item is already there, this is not a cycle.
        if pos == cycleStart:
            continue

        # Otherwise, put the item there or right after any duplicates.
        while item == array[pos]:
            pos += 1
            array[pos], item = item, array[pos]
            writes += 1

        # Rotate the rest of the cycle.
        while pos != cycleStart:
            # Find where to put the item.
            pos = cycleStart

        for i in range(cycleStart + 1, len(array)):
            if array[i] < item:
                pos += 1

        # Put the item there or right after any duplicates.
        while item == array[pos]:
            pos += 1
            array[pos], item = item, array[pos]
            writes += 1
    print(array)
    return array


def main():
    nums = [4, 0, 3, 1]
    print(cycleSort(nums))


main()
