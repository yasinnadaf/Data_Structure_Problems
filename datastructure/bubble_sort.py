import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


def bubble_sort(size):
    """
    This function is for bubble sort
    :param size:
    :return:
    """
    try:
        a = []
        for i in range(size):
            val = int(input('enter the number: '))
            a.append(val)
        for i in range(size):
            for j in range(0, size - i - 1):
                if a[j] > a[j + 1]:
                    t = a[j]
                    a[j] = a[j + 1]
                    a[j + 1] = t
        print('sorted list is: ')
        print(a)

    except Exception as e:
        logging.exception(e)



if __name__ == '__main__':
    size = int(input('Enter the size: '))
    bubble_sort(size)