# 각 집단의 데이터
x1 = [58.7, 55.3, 61.8, 49.5, 64.5, 61, 65.7, 51.4, 53.6, 59]
x2 = [64.4, 55.8, 58.7, 54.7, 52.7, 67.8, 61.6, 58.7, 54.6, 51.5, 54.7, 61.4, 56.9]
x3 = [68, 65.9, 54.7, 53.6, 58.7, 58.7, 65.7, 66.5, 56.7, 55.4, 51.5, 54.8, 57.2]

from scipy import stats

# 정규성 검정
shapiro_x1 = stats.shapiro(x1)
shapiro_x2 = stats.shapiro(x2)
shapiro_x3 = stats.shapiro(x3)

print(f"x1: W={shapiro_x1.statistic:.4f}, p-value={shapiro_x1.pvalue:.4f}")
print(f"x2: W={shapiro_x2.statistic:.4f}, p-value={shapiro_x2.pvalue:.4f}")
print(f"x3: W={shapiro_x3.statistic:.4f}, p-value={shapiro_x3.pvalue:.4f}")

# 등분산성 검정
levene_test = stats.levene(x1, x2, x3)
print(f"Levene test: W={levene_test.statistic:.4f}, p-value={levene_test.pvalue:.4f}")
# 일원분산분석
anova_result = stats.f_oneway(x1, x2, x3)
print(f"ANOVA: F={anova_result.statistic:.4f}, p-value={anova_result.pvalue:.4f}")
import pandas as pd
import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# 데이터 준비
data = pd.DataFrame({
    'score': np.concatenate([x1, x2, x3]),
    'group': ['x1']*len(x1) + ['x2']*len(x2) + ['x3']*len(x3)
})

# Tukey HSD 사후검정
tukey_result = pairwise_tukeyhsd(endog=data['score'], groups=data['group'], alpha=0.05)
print(tukey_result)
