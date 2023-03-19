# python3
# Kristiāns Šneiders, 11.grupa, 221RDB042
import os

def build_heap(data):
    swaps = []
    n = len(data)
    
    for i in range(n//2 - 1, -1, -1):
        sift_down(i, data, swaps)
    return swaps

def sift_down(i, data, swaps):
    n = len(data)

    left_child = 2*i + 1
    right_child = 2*i + 2
    min_child = i
    
    if left_child < n and data[left_child] < data[min_child]:
        min_child = left_child
    if right_child < n and data[right_child] < data[min_child]:
        min_child = right_child

    if i != min_child:
        swaps.append((i, min_child))
        data[i], data[min_child] = data[min_child], data[i]
        sift_down(min_child, data, swaps)

def main():

    choice = input("Enter 'F' for file or 'I' for input: ")
    choice = choice.upper()
    
    if choice == "F":
        file_name = input("Enter file name: ").strip()
        path = os.path.join("tests", file_name)
        with open(path, 'r') as file:
            n = int(file.readline().strip())
            data = list(map(int, file.readline().strip().split()))
    elif choice == "I":
        n = int(input())
        data = list(map(int, input().split()))
    else:
        print("Invalid command")
        return

    assert len(data) == n

    swaps = build_heap(data)

    assert len(swaps) <= n*4

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
