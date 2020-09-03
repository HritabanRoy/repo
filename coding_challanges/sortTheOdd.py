def sort_array(arr1):
    arr2 = arr1.copy()
    arr2.sort()
    for i in range(len(arr1)):
        if arr1[i]%2 == 1:
            for j in range(len(arr1)):
                if arr2[j]%2==1:
                    arr1[i]=arr2[j]
                    arr2[j]=0
                    break
    return arr1

print(sort_array([5, 3, 2, 8, 1, 4]))