import sys

def bubble_sort(arr):

    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


if __name__=='__main__':

    arr = [2, 1, 9, 3, 7, 5, 6, 4, 8, 0]
    print(f"The original array is give as: {arr}")
    print("The sorted array is given as: ", bubble_sort(arr))
