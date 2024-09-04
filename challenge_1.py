
def fibonancci(arr):
    if len(arr)==0:
        arr.append(0)
    else:
        last_index=arr[-1]
        b_last_index=arr[-2]
        arr.append(last_index+b_last_index)
    return arr

arr=[0,1,1,2,3,5,8,13]
arr=fibonancci(arr)
print(arr)