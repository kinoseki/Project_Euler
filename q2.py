#/usr/bin/python3
# -*- coding: utf-8 -*-

def mul(lists, max):
    result = []    
    for candidate in lists:
        for i in range(max):
            if(max > i * candidate):
                result.append(i*candidate)
            else:
                break
    return set(result)

def fibonacci(i, lists, max):
    print("debug i:%d, lists:%s, max:%d" % (i,lists,max) )
    if lists == []:
        lists.append(i)
        return fibonacci(1, lists, max)
    if lists[-1] > max:
        return lists
    lists.append(i)
    return fibonacci(lists[-2] + i , lists, max)

if __name__ == '__main__':
    fib = fibonacci(1, [], 4000000)
#    print(fib[1:])
    sum = 0
    for i in fib[1:]:
        if i % 2 == 0:
            sum += i
    print(sum)