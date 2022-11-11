import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


def insertion_sorting(size):
    """
    This method for insertion sort.
    :param size:
    :return:
    """
    try:
        a = []
        for i in range(size):
            val = int(input("Enter number: "))
            a.append(val)
        for i in range(1, size):
            t = a[i]
            j = i - 1
            while j >= 0 and t < a[j]:
                a[j + 1] = a[j]
                j = j - 1
            a[j + 1] = t
        print('sorted list is ', a)
    except Exception as e:
        logging.exception(e)



if __name__ == "__main__":
    size = int(input("Enter a size of list: "))
    insertion_sorting(size)