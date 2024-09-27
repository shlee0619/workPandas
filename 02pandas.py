import pandas as pd

data = ['국어','영어','수학','과학','체육']
print(data)
print()


sr1 = pd.Series(data)
print(sr1)
print()


data = [78,90,54,39,80]
print(data)
sr2 = pd.Series(data)
print(sr2) #dtype: int64
print()

data = [3.14,6.78,'영어','수학',80]
print(data)
sr3 = pd.Series(data)
print(sr3) #dtype: object
print()


data = [3.78, 7.90, 1.54, 6.39, 5.80]
print(data)
sr4 = pd.Series(data)
print(sr4) #dtype: float64
print()