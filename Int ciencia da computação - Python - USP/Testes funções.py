def even_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
        return lst


print(even_lst(11))

def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list


foo = [1, 2, 3, 4, 5]
print(list_updater(foo))