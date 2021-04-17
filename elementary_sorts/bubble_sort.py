def bubble_sort(arr):
    n = len(arr)
    max_num = 0
    for i in range(n):
        # compare every 2 items of array, ele with the next ele: arr[j] vs arr[j+1] each iteration,
        # the max value will bubble up towards the end of array
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            print(f"arr: {arr}")
    print(f"result: {arr}")

if __name__ == '__main__':
    elements = [8, 1, 4, 3, 7]
    print(f"initial array: {elements}")
    bubble_sort(elements)



