import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


def check_anagram(str1, str2):
    """
    This function is to check strings are anagram or not.
    param str1:int
    :param str2:int
    :return:none
    """
    try:
        sorted_str1 = sorted(str1)
        sorted_str2 = sorted(str2)
        if sorted_str1 == sorted_str2:
            print("strings are anagrams")
        else:
            print("strings are not anagrams")
    except Exception as e:
        logging.exception(e)


if __name__ == '__main__':
    str1 = str(input("Enter a string1: "))
    str2 = str(input("Enter a string2: "))
    check_anagram(str1, str2)