import numpy as np
from scipy import stats
import pandas as pd
from scipy.stats import t
# 문제2
# x1 = 재활용 전
# x2 = 재활용 후
x1 = pd.Series([20, 6, 12, 34, 55, 43, 54, 24, 33, 21, 34, 33, 54, 23, 33, 44, 65, 43, 53, 22, 34, 32, 44, 17, 28])
x2 = pd.Series([23, 8, 11, 35, 57, 76, 54, 26, 35, 26, 28, 31, 56, 22, 35, 41, 56, 34, 51, 21, 31, 33, 38, 15, 27])
df = len(x1)-1
ts, pv = stats.ttest_rel(x1, x2)

print(f't통계량: {ts:.3f}')
print(f'p값: {pv:.3f}')

cv = t.ppf(1-0.05, df);print(cv)
pv = 1-t.cdf(ts, df);print(pv)