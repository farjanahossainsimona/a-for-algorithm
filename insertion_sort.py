def insertion_sort(list):
    index_length = range(1, len(list))
    for i in index_length:
        to_sort = list[i]

        while list[i-1] > to_sort and i>0:
            list[i] , list[i-1] = list[i-1], list[i]
            i= i-1
    return list        

print(insertion_sort([1,2,7,8,9,2,8,2,4,5,2,7,8,9,2,8,2,4,5]))    