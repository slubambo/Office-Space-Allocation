def remove_list_duplicates(list_entered):

    return_list = []

    for n, list_item in enumerate(list_entered):
        if list_item not in list_entered[:n]:
            return_list.append(list_item)

    return return_list


def binary_search_if_item_in_list(list_entered, target):

    sorted_list = list_entered
    first = 0
    last = len(sorted_list) - 1
    found = False

    while first <= last and not found:
        middle = (first + last) // 2
        if sorted_list[middle].name == target:
            found = True
            return found
        else:
            if target != sorted_list[middle]:
                last = middle - 1
            else:
                first = middle + 1
    return None



