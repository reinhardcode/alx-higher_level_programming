#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []

    for n in range(list_length):
        try:
            new.append(my_list_1[n] / my_list_2[n])
        except (ValueError, TypeError):
            new.append(0)
            print("wrong type")
        except ZeroDivisionError:
            new.append(0)
            print("division by 0")
        except IndexError:
            new.append(0)
            print("out of range")
    return new
