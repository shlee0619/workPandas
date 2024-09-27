import pandas as pd
import numpy as np
print()


#결측값 파일대신 Key:Value 딕트구조를 프레임화 = table화
data = {'code':range(2000,2010),
        'kor':[85,95,np.nan,70,100,np.nan,95,np.nan,80,85],
        'eng':[95,70,100,85,80,85,95,95,np.nan,70],
        'mat':[np.nan, np.nan, np.nan, 0,0,0,0, 95, np.nan, 75]

}
df = pd.DataFrame(data)
print(df)
print()

#문제 0번째 삭제
# df=df.drop(0)
# df=df.drop(1)
# df=df.drop(7)
# print(df)
# print()

#문제 code, kor출력
print(df.loc[:,['code','kor']])
print()
df = df.fillna(1)
print(df['kor']*2)





