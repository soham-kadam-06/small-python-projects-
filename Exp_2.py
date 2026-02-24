# Merge sort logic 
def Mergesort(A, low, high,):
    if low < high:
        mid = (low + high) // 2
        Mergesort(A, low, mid)
        Mergesort(A, mid + 1, high)
        Merge(A, low, mid, high)


def Merge(A, low, mid, high):
    h = low
    i = low
    j = mid + 1
    unsorted_arr = []

    while h <= mid and j <= high:
        if A[h] <= A[j]:
            unsorted_arr.append(A[h])
            h = h + 1
        else:
            unsorted_arr.append(A[j])
            j = j + 1
        i = i + 1

    if h > mid:
        for k in range(j, high + 1):
            unsorted_arr.append(A[k])
    else:
        for k in range(h, mid + 1):
            unsorted_arr.append(A[k])

    for k in range(low, high + 1):
        A[k] = unsorted_arr[k - low]


  


  

def main():
    unsorted_arr=list(map(int,input("Enter numbers to be sorted: ").split()))
  
    while True:
        print("----sorting program---")
        print("1.Merge sort")
        print("2.Quick sort ")
        print("3.End")
        choice=int(input("enter choice :"))

        match choice:
            case 1:
                print("\nunsorted arr:",unsorted_arr)
                arr=unsorted_arr.copy()
                Mergesort(arr,0,len(unsorted_arr)-1)
                print("\n sorted arry:",arr)
                break
            case 2:
                Quicksort(unsorted_arr.copy())
            
            case 3:
                break
            case _:
                print("invalid option")

if __name__=="__main__":
    main()
