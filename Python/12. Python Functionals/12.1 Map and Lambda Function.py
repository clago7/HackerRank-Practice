# Problem: https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: x ** 3# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib = []
    for num in range(n):
        if num == 0:
            fib.append(0)
        elif num == 1:
            fib.append(1)
        else: fib.append(fib[num-2]+fib[num-1])
    return fib
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))