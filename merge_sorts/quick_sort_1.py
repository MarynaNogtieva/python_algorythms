# creating additional arrays     
def quick_sort(arr):
  # print(arr)
  arr_len = len(arr)
  if arr_len <= 1:
      return arr
  # pivot will be the last ele
  pivot = arr.pop()

  items_greater = []
  items_lower = []

  for num in arr:
      if num <= pivot:
          items_lower.append(num)
      else:
          items_greater.append(num)
  res_lower = quick_sort(items_lower)
  res_greater = quick_sort(items_greater)
  return res_lower + [pivot] + res_greater
  

  
if __name__ == '__main__':
 
  elements = [21, 38, 29, 17, 4, 25, 11, 32, 3,17]
  # elements = [38, 29]
  print(f"initial array: {elements}")
  print(f"sorted array: {quick_sort(elements)}")