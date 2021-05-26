def pivot(arr, low, high):
    i = low - 1

    # pivot is the last number in arr
    pivot = arr[high] 
    for j in range(low, high):
        if arr[j] < pivot:
            # i becomes a bigger number
            i += 1
            # swap smaller j with bigger i
            arr[j], arr[i] = arr[i], arr[j]
    i += 1
    pivot_idx = i
    # swap high(pivot) idx with i and put it in the correct spot 
    arr[i], arr[high] = arr[high], arr[i]
    return pivot_idx

def quick_sort(arr, low, high):
    if low >= high:
        return 
    sorted_p_idx = pivot(arr, low, high)
    quick_sort(arr, low, sorted_p_idx - 1)
    quick_sort(arr, sorted_p_idx + 1, high)

    return arr

if __name__ == '__main__':
    elements = [21, 38, 29, 17, 4, 25, 11, 32, 3,17]
    # elements = [38, 29]
    low = 0
    high = len(elements) - 1
    print(f"initial array: {elements}")
    print(f"sorted array: {quick_sort(elements, low, high)}")