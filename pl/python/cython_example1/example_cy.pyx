cpdef sum_number(int num):
    cpdef int result = 0
    cpdef int i
    for i in range(num):
        result += i

    return result