arr1=[4,5,7,9,10,34]
arr2=[1,3,6,8,32,33]
arr3=[]
def merge(arr1,arr2):
    if(len(arr2) != 0 and len(arr1)!=0):
        if arr1[0]>arr2[0]:
            arr3.append(arr2[0])
            arr2.remove(arr2[0])
        elif arr1[0]<arr2[0]:
            arr3.append(arr1[0])
            arr1.remove(arr1[0])
        elif arr1[0]==arr2[0]:
            arr3.append(arr1[0])
            arr1.remove(arr1[0])
            arr2.remove(arr2[0])
        merge(arr1,arr2)
    elif (len(arr1)==0):
        while (len(arr2)!=0):
            arr3.append(arr2[0])
            arr2.remove(arr2[0])
    elif (len(arr2)==0):
        while (len(arr1)!=0):
            arr3.append(arr1[0])
            arr1.remove(arr1[0])
    return arr3

print merge(arr1,arr2)
