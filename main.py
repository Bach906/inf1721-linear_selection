
from time import time
import math
from random import randint

result_linear = 0
result_sort = 0

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
    index = math.floor(len(a)/2) #round up
    return a[index]


def LinearSelection(A, k): # precisa funcionar com floats repetidos
    median_list = []
    len_5_list = []
    aux = 0


    if k < 0 or k > len(A):
        print(F"Invalid k: k = {k}, len(A) = {len(A)}")
        quit()

    if len(A) == 1:
        return get_median(A)

    if len(A) < 1:
        quit()
        
    # separa em sublistas de 5 elementos
    for elem in A:
        len_5_list.append(elem)
        aux += 1
        if aux % 5 == 0 or aux == len(A):
            # poe medianas em uma lista median_list
            median_list.append(get_median(len_5_list))
            len_5_list.clear()


    # Particiona lista A usando a mediana da median_list 
    m = LinearSelection(median_list, len(median_list)//2)

    R = []
    L = []

    for elem in A:
        if elem < m:
            L.append(elem)
        if elem > m:
            R.append(elem)

    tamL = len(L)
    if tamL == k - 1:
        return m
    elif tamL > k - 1:
        return LinearSelection(L,k)
    else:
        return LinearSelection(R,k - tamL - 1)


def SortSelection(A, k):
    Aord = bubblesort(A)
    return Aord[k-1]


def run_n_time(A,k):

    start_linear = time()
    result_linear = LinearSelection(A, k)
    end_linear = time()
    total_time_linear = end_linear - start_linear

    start_sort = time()
    result_sort = SortSelection(A, k)
    end_sort = time()
    total_time_sort = end_sort - start_sort

    print("linear", total_time_linear, "sort", total_time_sort)

    return

def main():
    A = []
    k = 2  # <- pode modificar para achar 'k' que quiser

    f = open("n100.txt", "r")
    for line in f:
        i = int(line)
        A.append(i)

    res1 = LinearSelection(A,k)
    print(f"resultado LinearSelection: {res1}")

    

#2

    
    run_n_time(A,len(A)//2)

    if result_linear == result_sort:
        print("Resultado Correto!")
    else:
        print("Resultado Errado!")

    # print("tempo linear = ", total_time_linear)
    # print("tempo sort = ", total_time_sort)

    return

main()