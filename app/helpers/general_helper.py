def remove_list_duplicates(list_entered):

    return_list = []

    for n, ii in enumerate(list_entered):
        if ii not in list_entered[:n]:
            return_list.append(ii)

    return return_list


def binary_search_if_item_in_list(list_entered, target):
    lower = 0
    upper = len(list_entered)
    count = 0

    while lower < upper:

        x = lower + (upper - lower) // 2

        val = list_entered[x]

        count += 1

        if target == val:

            return True

        elif target > val:
            if lower == x:
                break

            lower = x

        elif target < val:
            upper = x

        else:
            return False
