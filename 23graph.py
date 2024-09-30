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


name = [ '가나','길동','희동','영희', 'aa', 'bb', 'cc']
data = [ 40, 60, 86, 35, 54,12, 70 ]
fig , ax = plt.subplots()
ax.bar(name,data, color='g')
plt.show()


plt.scatter(name, data, s=90, c='blue', marker='p') #흩어진 정도
plt.title('scatter test 그래프')
plt.show() 


