import random
#(a) algorithm implementation
 
def insertion_sort(n):
    for i in range(1, len(n)):
        for j in range(i,0,-1):
            if n[j] < n[j-1]:
                n[j], n[j-1] = n[j-1], n[j]
            else:
                break
    return n

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        result.extend(left[i:])
        result.extend(right[j:])
    return result 

def merge_sort(n):
    if len(n) <= 1:
        return n
    mid = len(n) // 2
    left = merge_sort(n[:mid])
    right = merge_sort(n[mid:])
    return merge(left,right)

def hybrid_sort(n,S):
    if len(n) <= S:
        insertion_sort(n)
        return 
    else:
        mid = len(n) // 2
        left = hybrid_sort(n[:mid],S)
        right = hybrid_sort(n[mid:],S)
        return merge(left,right)

#(b) Generate input data
def random_array(n,seed,maximum):
    rnd = random.Random(seed)
    arr = [rnd.randint(1,maximum) for _ in range(n)]
    print("Minumum: ", min(arr))
    print("Maximum: ", max(arr))
    print("Size: ", len(arr))
    print (arr)
    return arr
def main():
    random_array(100,1,100)

if __name__ == "__main__":
    main()