def shell_sort(arr):
    n = len(arr)
    gap = 1

    while (gap < n // 3):
        gap = gap * 3 + 1

    while(gap >= 1):
    # start with i=gap and compare elements going forward
    # with prev_ele = ele - gap 
        for i in range(gap, n):
            j = i
            while j >= gap and arr[j] < arr[j-gap]:
                # swap
                temp = arr[j]
                arr[j] = arr[j-gap]
                arr[j-gap] = temp

                j -= gap
                print(f"arr: {arr}")

        gap = gap // 3
    print(f"result: {arr}")







if __name__ == '__main__':
    elements = [21, 38, 29, 17, 4, 25, 11, 32, 3]
    print(f"initial array: {elements}")
    shell_sort(elements)



