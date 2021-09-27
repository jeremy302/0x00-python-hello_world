def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        r = 0
        try:
            v1 = my_list_1[i]
            v2 = my_list_2[i]
            try:
                r = v1 / v2
            except TypeError as err:
                print('wrong type')
            except ZeroDivisionError as err:
                print('division by 0')
        except:
            print('out of range')
        finally:
            res.append(r)

    return res
