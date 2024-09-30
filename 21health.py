import pandas as pd
import time

path = './data/health.csv'
health = pd.read_csv(path)
print(health)
print()

#HEIGHT컬럼  WEIGHT컬럼   총점, 평균, 최대, 최소 
hgroup = health.groupby(['HEIGHT'])['WEIGHT'].agg(['sum', 'mean','count'])
print(hgroup)
print()







