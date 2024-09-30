# matplotlib=차트 
import matplotlib.pyplot as plt
import matplotlib 
import time
import numpy as np
import pandas as pd


#from matplotlib  import font_manager,rc
font_name = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)

# 음수
import matplotlib as mpl 
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus'] = False

plt.rcParams['font.size']=12.0
plt.rcParams['font.family'] = 'batang'
plt.rcParams['font.family'] = 'Malgun Gothic'
##############################################################################
##############################################################################

#실습1
# data = np.random.rand(16)
# df = pd.Series(data) #dtype: float64
# df.plot(kind = 'barh') #판다스를 차트matplotlib바로 연결
# print()
# plt.show()
# print('09-30-월요일 차트연습')


# name = ['kim', '길동', '희동', '영희','lee']
# data = np.random.randint(1,10,5)
# plt.plot(name, data)
# plt.show()

y1=[10,50,43,10] #y축값 4개
y2=[50,10,70]   #y축값 3개
y3=np.random.randint(1,15,5) #y축값 5개
y4=[30,60,10,80,70]  #y축값 5개


#실습3
plt.figure(figsize=(10,4))

plt.subplot(131) #1가로행 3데이터 1열
plt.bar(['aa' , 'bb', '희동', 'dd'], y1)
plt.title('1 sub plot')


plt.subplot(132) #1가로행 3데이터 2열
plt.bar(['xx' , 'yy', 'zz'], y2)
plt.title('2 sub plot')

plt.subplot(133) #1가로행 3데이터 3열
plt.scatter(['a','b','c','d','e'], y3, c='red', marker='^')
plt.title('3 sub plot')



plt.show()

