
import math
from random import randint

#global var
distr_flag = 0

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


def simple_LinearSelection(A, k): #visto em sala
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

    m = simple_LinearSelection(median_list, math.ceil(len(median_list)/2))
    A.remove(m)

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
        return simple_LinearSelection(L, k)
    else: #elif k > len(L):
        return simple_LinearSelection(R, k - len(L) - 1)


def LinearSelection(A, k): # precisa funcionar com floats repetidos
    median_list = []
    len_5_list = []
    global distr_flag
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
    A.remove(m)

    R = []
    L = []

    for i in A:
        if (i < m) or (i == m and distr_flag == 0):
            L.append(i)
            distr_flag = 1
        elif (i > m) or (i == m and distr_flag == 1):
            R.append(i)
            distr_flag = 0

    if k == len(L) + 1:
        return m
    elif k <= len(L):
        return LinearSelection(L, k)
    else: #elif k > len(L):
        return LinearSelection(R, k - len(L) - 1)


def main():
    A = []
    k = 20

    while(len(A) < 100):
        i = randint(1, 100)
        A.append(i)

    result = LinearSelection(A, k)

    A.sort()
    for i in range(len(A) - 1):
        print(A[i], end = ",")
    
    print()
    print("k'esimo menor valor =", A[k-1], "\nresultado da funcao =", result)

    return

main()