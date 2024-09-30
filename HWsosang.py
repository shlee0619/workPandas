import pandas as pd
import numpy as np

path = './0927금요일소상공인데이터/소상공인시장진흥공단_상가(상권)정보_서울_202112.csv'
df = pd.read_csv(path, encoding='utf-8', index_col=False)
print(df)
print()


# 스타벅스 or 스타 벅스 혹은 starbucks
# 이디야 or 이디아 혹은 ediya Ediya
# 요거프레소도 가능

print(df[df['스타벅스','경도','위도']])