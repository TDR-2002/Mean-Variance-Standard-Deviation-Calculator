import numpy as np
def calculate(arr):
    if len(arr)!=9:
        raise ValueError("List must contain nine numbers")
    a=np.array(arr).reshape(3,3)
    results={
        'mean': [(np.mean(a, axis=0)),(np.mean(a, axis=1)), np.mean(a)],
        'variance': [(np.var(a, axis=0)),(np.var(a, axis=1)), np.var(a)],
        'Standerd deviation': [(np.std(a, axis=0)),(np.std(a, axis=1)), np.std(a)],
        'max': [(np.max(a, axis=0)),(np.max(a, axis=1)), np.max(a)],
        'min': [(np.min(a, axis=0)),(np.min(a, axis=1)), np.min(a)],
        'sum': [(np.sum(a, axis=0)),(np.sum(a, axis=1)), np.sum(a)]


    }
    return results
print(calculate([1,2,3,4,5,6,7,8,9]))
