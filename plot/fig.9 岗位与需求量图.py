import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
df = pd.read_excel('result_all_normal.xlsx')
# df_three = df[df['城市等级'] == '三线']
df_three = df
df_1_1 = df_three[(df_three['职位种类'] == 'c语言') & (df_three['需求等级'] == '低需求')]
df_2_1 = df_three[(df_three['职位种类'] == 'java') & (df_three['需求等级'] == '低需求')]
df_3_1 = df_three[(df_three['职位种类'] == 'python') & (df_three['需求等级'] == '低需求')]
df_4_1 = df_three[(df_three['职位种类'] == '会计') & (df_three['需求等级'] == '低需求')]
df_5_1 = df_three[(df_three['职位种类'] == '大数据') & (df_three['需求等级'] == '低需求')]
df_6_1 = df_three[(df_three['职位种类'] == '客服') & (df_three['需求等级'] == '低需求')]
df_7_1 = df_three[(df_three['职位种类'] == '教师') & (df_three['需求等级'] == '低需求')]
df_8_1 = df_three[(df_three['职位种类'] == '数据分析') & (df_three['需求等级'] == '低需求')]
df_9_1 = df_three[(df_three['职位种类'] == '新媒体运营') & (df_three['需求等级'] == '低需求')]
df_10_1 = df_three[(df_three['职位种类'] == '销售') & (df_three['需求等级'] == '低需求')]
df_1 = [df_1_1.shape[0], df_2_1.shape[0], df_3_1.shape[0],
                df_4_1.shape[0], df_5_1.shape[0], df_6_1.shape[0],
                df_7_1.shape[0], df_8_1.shape[0], df_9_1.shape[0],
                df_10_1.shape[0]]
df_1_2 = df_three[(df_three['职位种类'] == 'c语言') & (df_three['需求等级'] == '中需求')]
df_2_2 = df_three[(df_three['职位种类'] == 'java') & (df_three['需求等级'] == '中需求')]
df_3_2 = df_three[(df_three['职位种类'] == 'python') & (df_three['需求等级'] == '中需求')]
df_4_2 = df_three[(df_three['职位种类'] == '会计') & (df_three['需求等级'] == '中需求')]
df_5_2 = df_three[(df_three['职位种类'] == '大数据') & (df_three['需求等级'] == '中需求')]
df_6_2 = df_three[(df_three['职位种类'] == '客服') & (df_three['需求等级'] == '中需求')]
df_7_2 = df_three[(df_three['职位种类'] == '教师') & (df_three['需求等级'] == '中需求')]
df_8_2 = df_three[(df_three['职位种类'] == '数据分析') & (df_three['需求等级'] == '中需求')]
df_9_2 = df_three[(df_three['职位种类'] == '新媒体运营') & (df_three['需求等级'] == '中需求')]
df_10_2 = df_three[(df_three['职位种类'] == '销售') & (df_three['需求等级'] == '中需求')]
df_2 = [df_1_2.shape[0], df_2_2.shape[0], df_3_2.shape[0],
                df_4_2.shape[0], df_5_2.shape[0], df_6_2.shape[0],
                df_7_2.shape[0], df_8_2.shape[0], df_9_2.shape[0],
                df_10_2.shape[0]]
df_1_3 = df_three[(df_three['职位种类'] == 'c语言') & (df_three['需求等级'] == '高需求')]
df_2_3 = df_three[(df_three['职位种类'] == 'java') & (df_three['需求等级'] == '高需求')]
df_3_3 = df_three[(df_three['职位种类'] == 'python') & (df_three['需求等级'] == '高需求')]
df_4_3 = df_three[(df_three['职位种类'] == '会计') & (df_three['需求等级'] == '高需求')]
df_5_3 = df_three[(df_three['职位种类'] == '大数据') & (df_three['需求等级'] == '高需求')]
df_6_3 = df_three[(df_three['职位种类'] == '客服') & (df_three['需求等级'] == '高需求')]
df_7_3 = df_three[(df_three['职位种类'] == '教师') & (df_three['需求等级'] == '高需求')]
df_8_3 = df_three[(df_three['职位种类'] == '数据分析') & (df_three['需求等级'] == '高需求')]
df_9_3 = df_three[(df_three['职位种类'] == '新媒体运营') & (df_three['需求等级'] == '高需求')]
df_10_3 = df_three[(df_three['职位种类'] == '销售') & (df_three['需求等级'] == '高需求')]
df_3 = [df_1_3.shape[0], df_2_3.shape[0], df_3_3.shape[0],
                df_4_3.shape[0], df_5_3.shape[0], df_6_3.shape[0],
                df_7_3.shape[0], df_8_3.shape[0], df_9_3.shape[0],
                df_10_3.shape[0]]
#
tick_label = ['c语言', 'python', 'java', '会计', '大数据', '客服', '教师', '数据分析', '新媒体运营', '销售']
bar_width = 0.2
data = [df_1, df_2, df_3]
x = np.arange(len(tick_label))

plt.figure(dpi=433, figsize=(12, 6))
plt.title('岗位与需求量图')
plt.bar(x, df_1, bar_width, align='center', label='高需求')
plt.bar(x + bar_width, df_2, bar_width, align='center', label='中需求')
plt.bar(x + 2 * bar_width, df_3, bar_width, align='center', label='低需求')
plt.xlabel('岗位')
plt.ylabel('数量')
plt.xticks(x + bar_width / 3, tick_label)
plt.legend()
plt.savefig('fig.9 岗位与需求量图.png')
plt.show()
