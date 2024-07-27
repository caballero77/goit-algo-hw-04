def merge_k_lists(lists):
    result = []
    while True:
        empty = 0
        min_i, min_val = 0, float('inf')
        for i in range(len(lists)):
            if len(lists[i]) == 0:
                empty += 1
            elif lists[i][0] < min_val:
                min_i = i
                min_val = lists[i][0]

        if empty == len(lists):
            break

        result.append(min_val)
        lists[min_i].pop(0)

    return result


merged_list = merge_k_lists([[1, 4, 5], [1, 3, 4], [2, 6]])
print("Sorted array:", merged_list)