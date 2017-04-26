def remove_list_duplicates(list_entered):

    return_list = []

    for n, ii in enumerate(list_entered):
        if ii not in list_entered[:n]:
            return_list.append(ii)

    return return_list