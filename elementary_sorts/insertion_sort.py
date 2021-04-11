import random

class InsertionSort:

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


    def insertion_sort(self):
        for i in range(len(self.arr)):
            for j in range(i, 0, -1):
                if self.arr[j] < self.arr[j-1]:
                    self.swap_values(j, j-1)
                else: break
        return self.arr
            
                

 

# ====================================================
# To run from terminal: python3 insertion_sort.py 
insertion_sort_obj = InsertionSort()

p = random.randint(0, 11)
q = random.randint(0, 11)
insertion_sort_obj.init_arr(12)
insertion_sort_obj.insertion_sort()
print(f"sorted arr: {insertion_sort_obj.arr}")

