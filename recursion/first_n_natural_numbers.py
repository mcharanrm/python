# My notes on how to slove this problem using recursion

# I could see Recursion is not a appropriate method to print first N natural numbers
# because technique is designed for designed purpose

# Problems like What is the sum of first N natural numbers ?
#               What is the N'th term in the given arithmetic/geometrics Progression ?
#               Etc...


def print_nat_numbers(N):
    # Algorithm 
    # An = An-1 + 1
    # Assume A1 = 1
    ''' Program to print first N natural numbers using Recursion '''
    if N == 1:
        print(N)
        return N
    else:
        tmp = 1 + print_nat_numbers(N - 1)
        print(tmp)
        return tmp

def print_sum_of_n_numbers(N):
    ''' Print the sum of first N natural numbers using Recursion '''
    # Mathematical Formula = n (n + 1) / 2
    # Otherwise we can use simple for loop
    # tmp_aggr_sum = 0; for item in range(1, N+1): tmp_aggr_sum += item ; print(tmp_aggr_sum)

    #Using recursion method
    if N == 1:
        return N
    else:
        return N + print_sum_of_n_numbers(N - 1)



if globals()['__name__'] == '__main__':
    N = int(input('Please Enter a Number: ').strip())
    print_nat_numbers(N)
    print('{}'.format(print_sum_of_n_numbers(N)))

