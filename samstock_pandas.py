import pandas as pd
import numpy as np
import time


# sam_kospi.xlsx엑셀파일
path = './data/sam_kospi.xlsx'
sam = pd.read_csv(path, encoding='utf-8')
print(sam)
print()
# 오픈열기처리
# Date거래일자,Open,High,Low,Volume
print(sam[['Date', 'Open', 'High', 'Low', 'Volume']])


