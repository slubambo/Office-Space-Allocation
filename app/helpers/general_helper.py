def remove_list_duplicates(list_entered):

    return_list = []

    for n, ii in enumerate(list_entered):
        if ii not in list_entered[:n]:
            return_list.append(ii)

    return return_list


def binary_search_if_item_in_list(list_entered, target):

    sorted_list = sorted(list_entered)
    first = 0
    last = len(sorted_list) - 1
    found = False

    print(len(list_entered))

    while first <= last and not found:
        middle = (first + last) // 2
        if sorted_list[middle].name == target:
            found = True
        else:
            if target != sorted_list[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return found

