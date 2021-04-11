import random

class QuickFind:

    def __init__(self):
        self.id_arr = []
        
    def init_id_arr(self, n):
        for i in range(n):
            self.id_arr.append(i)

        return self.id_arr

    def find(self, num):
        return self.id_arr[num]

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)

        if p_id == q_id:
            print(f'{p} and {q} are connected')
            return 

        # change all p_id to be q_id
        for i in range(len(self.id_arr)):
            if self.id_arr[i] == p_id:
                self.id_arr[i] = q_id


# ====================================================
# To run from terminal: python3 quick_find.py 
quick_find_obj1 = QuickFind()
for i in range(12):
    p = random.randint(0, 11)
    q = random.randint(0, 11)
    quick_find_obj1.init_id_arr(12)
    quick_find_obj1.union(p,q)

