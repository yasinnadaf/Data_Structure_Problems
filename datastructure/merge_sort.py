import logging


def mergesort(list1):
    """

    :param list1:
    :return:
    """
    try:
        # condition for dividing list
        if len(list1) > 1:
            mid = len(list1) // 2
            left_list = list1[:mid]
            right_list = list1[mid:]
            mergesort(left_list)
            mergesort(right_list)

            # Two iterators for traversing the two halves
            i = 0
            j = 0

            # Iterator for the main list
            k = 0

            # condition for merging
            while i < len(left_list) and j < len(right_list):
                if left_list[i] < right_list[j]:
                    list1[k] = left_list[i]
                    i += 1
                    k += 1
                else:
                    list1[k] = right_list[j]
                    j += 1
                    k += 1

            # this two conditions for any value left out or not
            # 1st while to check weather any value is left in the left sublist
            while i < len(left_list):
                list1[k] = left_list[i]
                i += 1
                k += 1

            # this while to check weather any value is left in the right sublist
            # if any value is left then ill add that to list1
            while j < len(right_list):
                list1[k] = right_list[j]
                j += 1
                k += 1
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    num = int(input("How many elements you want in list: "))
    list1 = [int(input()) for x in range(num)]
    mergesort(list1)
    print(list1)


