import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


def prime_check(lower, upper):
    """
    :param lower: int
    :param upper: int
    :return: none
    """
    try:
        for number in range(lower, upper):
            if number > 1:
                for i in range(2, number):
                    if (number % i) == 0:
                        break
                else:
                    print(number)
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    prime_check(0, 1000)

