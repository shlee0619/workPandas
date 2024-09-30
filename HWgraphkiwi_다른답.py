# matplotlib=차트 
import matplotlib.pyplot as plt
import matplotlib 

#from matplotlib  import font_manager,rc
font_name = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)

# 음수
import matplotlib as mpl 
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus'] = False

#  한글글꼴로 변경
plt.rcParams['font.size'] = 12.0
plt.rcParams['font.family'] = 'batang'
plt.rcParams['font.family'] = 'Malgun Gothic'
##########################################################################
##########################################################################
import time
import numpy as np
import pandas as pd

fruits = ['apple', 'blue', 'kiwi', 'mango']
area =['서울','안양','수원','일산']
su1 = [21, 34, 45, 13]
su2 = [45, 19, 31, 50]
su3 = [33, 56, 27, 41]
su4 = [77, 34, 65, 29]

df = pd.DataFrame({area[0]:su1,area[1]:su2,area[2]:su3,area[3]:su4 }, index=fruits)
print(df)
print()

ax = df.plot(kind='bar', figsize=(10,6))
my = ax.patches[0] 

print('- ' * 50)
print('다른방법ax.annotate() 가장왼쪽 bar 서울 블루 정보출력')
print('다른방법ax.annotate() 값 =',my.get_height(), '  ' , my.get_width())
print('- ' * 50)

left,bottom,width,height = ax.patches[0].get_bbox().bounds
print(f'정보출력ax.patches[0]  left={left} bottom={bottom} width={width} height={height}')

for i in ax.patches:
    left,bottom,width,height = i.get_bbox().bounds
    ax.annotate('%d'%(height),(left+width/2, height*1.01), ha='center')
plt.legend(loc='upper right')
plt.show()



'''
첫번째방법 해결 위쪽껏  ax.annotate( )함수비교

ax = df.plot(kind='bar', figsize=(10,6))
my = ax.patches[0] 

print('- ' * 50)
print('점심식사후 가장왼쪽 bar 서울 블루 정보출력')
print('점심식사후 값 =',my.get_height(), '  ' , my.get_width())
print('- ' * 50)


for i in range(len(ax.patches)):
    value = ax.patches[i]
    plt.text(value.xy[0], value.get_height()+0.2, s=str(value.get_height()))
plt.legend(loc='upper right')
plt.show()

'''


'''
지역별 과일 총판매수량
과일별 지역 총판매수량
문제1] 큰제목및 범례 x축제목 y축제목
문제2] bar모양권장  scatter, pie
문제3] y축값표시
문제4] 
df=pd.DataFrame({'서울':su1,'안양':su2,'수원':su3,'일산':su4},index=fruits)

참고
# data = np.random.rand(16)  #실수 0.0000~0.99999난수
# df = pd.Series(data) #dtype: float64
# df.plot(kind='bar')#판다스를 차트matplotlib바로 연결
# plt.show() 
'''







