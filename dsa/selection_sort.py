#! python3

def sel_sort(my_list):
    for i in range(len(my_list)-1):
        min_i=i
        for j in range(i+1,len(my_list)):
            if my_list[min_i]>my_list[j]:
                min_i=j
        my_list[i],my_list[min_i]=my_list[min_i],my_list[i]
    
    return print(my_list)



my_list=[64,25,75,37,44,56,22]
sel_sort(my_list)