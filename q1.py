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
    return result

if __name__ == '__main__':
    mul_list = mul([3, 5], 1000)
    result = sum(set(mul_list))
    print(result)
    