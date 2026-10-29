def list_overlap(list1, list2):
    result = []
    copy = list2[:]

    for item in list1:
        if item in copy:
            result.append(item)
            copy.remove(item)

    return result