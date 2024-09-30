import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc

# 한글 폰트 설정 (맑은 고딕)
font_path = 'C:/Windows/Fonts/malgun.ttf' 
font_name = fm.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

# 데이터
x = ['2020', '2021', '2022', '2023']
y = [300, 130, 270, 230]

# 그래프 그리기
plt.bar(x, y, color='green')
plt.title('2024년 앱사용 테스트')  # 한글 제목
plt.xlabel('년도')  # 한글 x축 라벨
plt.ylabel('실적금액')  # 한글 y축 라벨
plt.show()

