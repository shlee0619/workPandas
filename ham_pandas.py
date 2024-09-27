import pandas as pd
import numpy as np
import time
import re


path = './data/spam_data.csv'
spam_data = pd.read_csv(path, encoding='cp949')
print(spam_data)

# 파이썬 기본정규화 처리
# 특수문자, 숫자, 공백제거 
# 대문자를 소문자화


def normalize_text(text):
    #소문자화
    text = text.lower()
    #특수문자,숫자 제거
    text = re.sub(r'[^가-힣a-zA-Z\s]', '', text)  
    #공백제거
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

spam_data.iloc[:,1] = spam_data.iloc[:,1].apply(normalize_text)
print(spam_data)