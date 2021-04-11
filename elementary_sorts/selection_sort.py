import random

class SelectionSort:

    def __init__(self):
        self.arr = []
        
    def init_arr(self, n):
        for i in range(n):
            self.arr.append(i)

        return self.arr
    
    def swap_values(self, a,b):
        temp = a
        self.arr[a] = self.arr[b]
        self.arr[b] = temp
        return self.arr


    def selection_sort(self):
        for i in range(len(self.arr)):
            min_val = i
            for j in range(i+1, len(self.arr)):
                if self.arr[j] < self.arr[min_val]:
                    min_val = j
            self.swap_values(i, min_val)
        return self.arr
            
                

 

# ====================================================
# To run from terminal: python3 selection_sort.py 
selection_sort_obj = SelectionSort()

p = random.randint(0, 11)
q = random.randint(0, 11)
selection_sort_obj.init_arr(12)
selection_sort_obj.selection_sort()
print(f"sorted arr: {selection_sort_obj.arr}")

