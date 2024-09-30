# matplotlib = 차트

import matplotlib.font_manager
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc


font_name = matplotlib.font_manager.FontProperties(fname = 'C:/Windows/Fonts/BATANG.TTC')

import numpy as np
# c:\WINDOWS\Fonts\BATANG.TTC

x = ['2020','2021','2022','2023']
y = [300,130,270,230]
plt.bar(x,y,color='green')
plt.title('2024년 앱사용 테스트')
plt.xlabel('년도')
plt.ylabel('실적금액')
plt.show()


