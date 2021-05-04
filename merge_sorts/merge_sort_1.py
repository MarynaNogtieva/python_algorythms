def merge(arr, aux_arr, low, high, mid):
  print(low, mid, high)
  for i in range(high):
    aux_arr[i] = arr[i]

  i = low
  j = mid + 1
  for k in range(len(arr)):
    # i has a limit - mid of arr. if i exceeds it's limit
    if i >= mid:
      arr[k] = aux_arr[j]
      j += 1
    # j has a limit - end of arr - high point. if j exceeds it's limit
    elif j >= high:
      arr[k] = aux_arr[i]
      i += 1
    elif aux_arr[i] <= aux_arr[j]:
      arr[k] = aux_arr[i]
      i += 1 # move the pointer
    else:
      arr[k] = aux_arr[j]
      j += 1
  return arr

def inner_sort(arr, aux_arr, low, high):
  if high <= low:
    return [arr[0]]
  mid = (high+low) // 2
  inner_sort(arr, aux_arr, low, mid)
  inner_sort(arr, aux_arr, mid+1, high)
  merge(arr, aux_arr, low, high, mid)

  print(f"sorted_arr: {arr}")
      
def merge_sort(arr):
  aux_arr = [i for i in arr]
  low = 0
  high = len(arr)-1
  inner_sort(arr, aux_arr, low, high)
  
if __name__ == '__main__':
 
  # elements = [21, 38, 29, 17, 4, 25, 11, 32, 3]
  elements = [38, 29]
  print(f"initial array: {elements}")
  merge_sort(elements)