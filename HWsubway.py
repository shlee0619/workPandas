import pandas as pd

df = pd.read_csv('./data/subway.csv', encoding='UTF-8', index_col=False)

# '사용일자'와 '등록일자' 컬럼을 날짜 형식으로 변환
for col in ['사용일자', '등록일자']:
    df[col] = pd.to_datetime(df[col], format='%Y%m%d').dt.strftime('%Y-%m-%d')

print(df)
print('- ' * 40)