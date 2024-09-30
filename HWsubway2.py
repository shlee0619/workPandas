import pandas as pd
import numpy as np
import time

path = './data/subway.csv'
df = pd.read_csv(path, encoding='utf-8', index_col=False)
print(df)
print()

time.sleep(2)

# 함수생성구현후 필드에 적용할때 apply()사용
def subwayDate(data):
    data = str(data)
    year = data[0:4]
    month = data[4:6]
    day = data[6:8]
    return year+'-'+month+'-'+day


print('~ ' * 50)  
df['사용일자'] = df['사용일자'].apply(subwayDate)
print(df )




