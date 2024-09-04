
def game(arr):
    arr.sort()
    missed_numbers=[]
    for i in range(len(arr)):
        if i!=(len(arr)-1):
            current_val=arr[i]
            next_val=arr[i+1]
            difference=next_val-current_val
            if (difference) !=1:
                for j in range(1,difference):
                    missed_numbers.append(current_val+j)
    return missed_numbers

test=[2,1,5,4,6,9,7,8,10]
missing=game(test)
print(missing)
