import pandas as pd
import numpy as np
print()

data = {'학번':range(2000,2010),
        '국어성적':[85,95,75,70,100,np.nan,95,85,80,85],
        '영어성적':[95,70,100,85,80,85,95,95,np.nan,70],
        '수학성적':[np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,95,np.nan,70]

}

df = pd.DataFrame(data)
print(df)
print(df.isna())
df.fillna(0)
print(df)
df.dropna()
print(df)

