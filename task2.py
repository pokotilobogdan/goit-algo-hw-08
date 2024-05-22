import random
import heapq

def generate_sorted_list(length):
    sorted_list = []
    last_element = 0
    for _ in range(length):
        last_element += random.randint(0, 50)
        sorted_list.append(last_element)
    return sorted_list

def merge_k_sorted_lists(sorted_lists):
    print(list(heapq.merge(*sorted_lists)))
    print()


if __name__ == "__main__":
    
    k = int(input("Введіть k: "))
    print()

    sorted_lists = [generate_sorted_list(random.randint(1, 10)) for _ in range(k)]
    
    print("Отримані масиви:")
    for sorted_list in sorted_lists:
        print(sorted_list)
    
    print()

    merge_k_sorted_lists(sorted_lists)