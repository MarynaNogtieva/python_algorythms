arr_len = int(input("Enter the number of elements to unite: "))
arr = list(range(arr_len))
size_arr = [1] * arr_len

print(arr)
exit = False



def get_numbers():
    first = int(input('Enter first number: ').strip())
    second = int(input('Enter second number: ').strip())

    return first, second


def connected(p_root, q_root):
    return p_root == q_root


def print_options():
    return ''

def find_root(index):
    print(f"Given num: {index}")
    while index != arr[index]:
        index = arr[index]
    print(f"Root: {index}")
    return index

def union(p, q):
    p_root_index = find_root(p)
    q_root_index = find_root(q)

    if connected(p_root_index, q_root_index):
        print(f"{p} and {q} are already connected")
        return
    
    # Make smaller tree to point to the larger
    if size_arr[p_root_index] < size_arr[q_root_index]:
        arr[p_root_index] = q_root_index
        size_arr[q_root_index] += size_arr[p_root_index]
    else:
        arr[q_root_index] = p_root_index
        size_arr[p_root_index] += size_arr[q_root_index] 

    

while not exit:
    option = int(input('Enter an option: 1 - exit, 2-union, 3-find, 4-print: ').strip())

    if option == 1:
        exit = True
        break
    elif option == 4:
        print(arr)
    elif option == 3:
        first, second = get_numbers()
        find_root(first)
        find_root(second)
    elif option == 2:
        first, second = get_numbers()
        union(first, second)
    else:
        print('Invalid input')


