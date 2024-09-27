
import pandas as pd

'''
08emp.py

loc[행,열]
iloc[행,열]

data/emp.cvs파일 

emp = pd.read_csv(파일이름.csv)
'''

# 문제1 판다스 이용해서 emp.csv파일읽기 
path = './data/emp.csv'
emp = pd.read_csv(path , encoding='cp949')
print(emp) 
print()

# 문제2 emp정보에서 No, Name컬럼 출력 /Pay출력 안해요
print(emp[['No','Name']])
print(emp['Name'])


# 문제3 2 103 강감찬 500
print(emp.loc[2])
print()

# 문제4 2행~4행
print(emp.loc[2:4])
print()
# 문제5 모든행 Name, Pay필드
print(emp.loc[:, 'Name':'Pay'])
print()
# 문제6 모든행 Name,No,Pay필드
print('loc 속성 열순서변경 Name,No,Pay')
print(emp.loc[:, ['Name','No','Pay']])
print()




print()
