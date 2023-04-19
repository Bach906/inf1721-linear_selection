
import math


# import heap stuff
# import bubble sort

def bubblesort(list):
    # algorithm taken from https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
    return list


def get_median(a):
    bubblesort(a)
    index = math.ceil(len(a)/2) #round up
    return a[index - 1]



def LinearSelection(A, k):
    median_list = []
    len_5_list = []

    aux = 0

    if len(A) <= 1:
        return get_median(A)
    
    for i in A:
        len_5_list.append(i)
        aux += 1
        if aux % 5 == 0 or aux == len(A):

            median_list.append(get_median(len_5_list))
            len_5_list.clear()

    m = LinearSelection(median_list, math.ceil(len(median_list)/2))
    
    R = []
    L = []

    for i in A:
        if i < m:
            L.append(i)
        elif i > m:
            R.append(i)


    if k == len(L) + 1:
        return m
    elif k <= len(L):
        return LinearSelection(L, k)
    elif k > len(L): #pode ser else
        return LinearSelection(R, k - len(L) - 1)
    
    return 1


def main():
    # cria vetor A de tamanho 100 contendo floats aleatorios
    # pega um k
    A = []
    k = 10
   
    for i in range(600):
        A.append(i)
    median_of_medians = LinearSelection(A, k)
    print(median_of_medians)

    return

main()