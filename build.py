# Sort a dictionary by key

E = {1: 10, 4: 40, 2: 20, 3: 30}

def solution(dic):
    x = dic.keys()
    x.sort()
    return x

solution(E)
