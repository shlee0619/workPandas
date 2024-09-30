# matplotlib=차트 
import matplotlib.pyplot as plt
import matplotlib 
import time
import numpy as np

#from matplotlib  import font_manager,rc
font_name = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)

# 음수
import matplotlib as mpl 
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus'] = False


name = [ '가나','길동','희동','영희']
data = [ 40, 60, 86, 35 ]
fig , ax = plt.subplots()
ax.bar(name,data, color='g')
plt.show()


plt.scatter(name, data, s=90, c='red', marker='d') #흩어진 정도
plt.title('scatter test 그래프')
plt.show() 


name = [ '가나','길동','희동','영희']
data = [ 40, 60, 86, 35 ]
ep= [0.05, 0.1, 0.15, 0.05] #슬라이싱되는 값
#explode슬라이싱, shadow=True그림자효과  시작각도startangle
fig,plt.pie(data, explode=ep, labels=name, autopct='%0.1f%%' ,shadow=True )
#plt.pie(data, labels=name, autopct='%0.1f%%' ,shadow=True, startangle=180 )
# plt.pie(data, labels=name, autopct='%0.1f%%' ,shadow=True)
plt.show()


name = [ '가나','길동','희동','영희']
data =[ 40, 90,  55, 85]
#라인 plt.plot(name, data) 
plt.pie(data, labels=name)

plt.title('pie 그래픽 연습')
plt.legend(name, loc='upper right')
plt.show()


z = np.random.randn(10000) 
print(z)
plt.hist(z, bins=20, color='hotpink')
plt.show()