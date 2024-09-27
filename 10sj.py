import pandas as pd
import numpy as np
print()


#결측값 파일대신 Key:Value 딕트구조를 프레임화 = table화
data = {'code':range(2000,2010),
        'kor':[85,95,75,70,100,np.nan,95,85,80,85],
        'eng':[95,70,100,85,80,85,95,95,np.nan,70],
        'mat':[np.nan, np.nan, np.nan, 0,0,0,0, 95, np.nan, 75]

}
df = pd.DataFrame(data)
print(df)
print()
print()

df = df.fillna(0)
print(df)
print()


hap = df['kor'] + df['eng'] + df['mat']
df.insert(4,['hap'], hap,True)
print(df)

