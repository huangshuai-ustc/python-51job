import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
df = pd.read_excel('result_all_normal.xlsx')
df_two = df[df['城市等级'] == '二线']
df_two_1_1 = df_two[(df_two['地点（已处理）'] == '大连') & (df_two['需求等级'] == '高需求')]
df_two_2_1 = df_two[(df_two['地点（已处理）'] == '中山') & (df_two['需求等级'] == '高需求')]
df_two_3_1 = df_two[(df_two['地点（已处理）'] == '宁波') & (df_two['需求等级'] == '高需求')]
df_two_4_1 = df_two[(df_two['地点（已处理）'] == '石家庄') & (df_two['需求等级'] == '高需求')]
df_two_5_1 = df_two[(df_two['地点（已处理）'] == '嘉兴') & (df_two['需求等级'] == '高需求')]
df_two_6_1 = df_two[(df_two['地点（已处理）'] == '南宁') & (df_two['需求等级'] == '高需求')]
df_two_7_1 = df_two[(df_two['地点（已处理）'] == '常州') & (df_two['需求等级'] == '高需求')]
df_two_8_1 = df_two[(df_two['地点（已处理）'] == '泉州') & (df_two['需求等级'] == '高需求')]
df_two_9_1 = df_two[(df_two['地点（已处理）'] == '芜湖') & (df_two['需求等级'] == '高需求')]
df_two_10_1 = df_two[(df_two['地点（已处理）'] == '桂林') & (df_two['需求等级'] == '高需求')]
df_two_11_1 = df_two[(df_two['地点（已处理）'] == '绍兴') & (df_two['需求等级'] == '高需求')]
df_two_12_1 = df_two[(df_two['地点（已处理）'] == '南昌') & (df_two['需求等级'] == '高需求')]
df_two_13_1 = df_two[(df_two['地点（已处理）'] == '南通') & (df_two['需求等级'] == '高需求')]
df_two_14_1 = df_two[(df_two['地点（已处理）'] == '烟台') & (df_two['需求等级'] == '高需求')]
df_two_15_1 = df_two[(df_two['地点（已处理）'] == '徐州') & (df_two['需求等级'] == '高需求')]
df_two_16_1 = df_two[(df_two['地点（已处理）'] == '昆明') & (df_two['需求等级'] == '高需求')]
df_two_17_1 = df_two[(df_two['地点（已处理）'] == '太原') & (df_two['需求等级'] == '高需求')]
df_two_18_1 = df_two[(df_two['地点（已处理）'] == '沈阳') & (df_two['需求等级'] == '高需求')]
df_two_19_1 = df_two[(df_two['地点（已处理）'] == '乌鲁木齐') & (df_two['需求等级'] == '高需求')]
df_two_20_1 = df_two[(df_two['地点（已处理）'] == '兰州') & (df_two['需求等级'] == '高需求')]
df_two_21_1 = df_two[(df_two['地点（已处理）'] == '宁德') & (df_two['需求等级'] == '高需求')]
df_two_22_1 = df_two[(df_two['地点（已处理）'] == '贵阳') & (df_two['需求等级'] == '高需求')]
df_two_23_1 = df_two[(df_two['地点（已处理）'] == '海口') & (df_two['需求等级'] == '高需求')]
df_two_24_1 = df_two[(df_two['地点（已处理）'] == '台州') & (df_two['需求等级'] == '高需求')]
df_two_25_1 = df_two[(df_two['地点（已处理）'] == '大庆') & (df_two['需求等级'] == '高需求')]
df_two_26_1 = df_two[(df_two['地点（已处理）'] == '盐城') & (df_two['需求等级'] == '高需求')]
df_two_27_1 = df_two[(df_two['地点（已处理）'] == '江西省') & (df_two['需求等级'] == '高需求')]
df_two_28_1 = df_two[(df_two['地点（已处理）'] == '宜昌') & (df_two['需求等级'] == '高需求')]
df_two_29_1 = df_two[(df_two['地点（已处理）'] == '廊坊') & (df_two['需求等级'] == '高需求')]
df_two_1 = [df_two_1_1.shape[0], df_two_2_1.shape[0],
              df_two_3_1.shape[0] + df_two_22_1.shape[0],
              df_two_4_1.shape[0], df_two_5_1.shape[0], df_two_6_1.shape[0],
              df_two_7_1.shape[0], df_two_8_1.shape[0] + df_two_23_1.shape[0],
              df_two_9_1.shape[0], df_two_10_1.shape[0], df_two_11_1.shape[0],
              df_two_12_1.shape[0], df_two_13_1.shape[0], df_two_14_1.shape[0],
              df_two_15_1.shape[0], df_two_16_1.shape[0] + df_two_21_1.shape[0],
              df_two_17_1.shape[0], df_two_18_1.shape[0],
              df_two_19_1.shape[0] + df_two_20_1.shape[0], df_two_27_1.shape[0],
              df_two_22_1.shape[0], df_two_23_1.shape[0], df_two_24_1.shape[0],
              df_two_25_1.shape[0], df_two_26_1.shape[0], df_two_27_1.shape[0],
              df_two_28_1.shape[0], df_two_29_1.shape[0]]

df_two_1_2 = df_two[(df_two['地点（已处理）'] == '大连') & (df_two['需求等级'] == '中需求')]
df_two_2_2 = df_two[(df_two['地点（已处理）'] == '中山') & (df_two['需求等级'] == '中需求')]
df_two_3_2 = df_two[(df_two['地点（已处理）'] == '宁波') & (df_two['需求等级'] == '中需求')]
df_two_4_2 = df_two[(df_two['地点（已处理）'] == '石家庄') & (df_two['需求等级'] == '中需求')]
df_two_5_2 = df_two[(df_two['地点（已处理）'] == '嘉兴') & (df_two['需求等级'] == '中需求')]
df_two_6_2 = df_two[(df_two['地点（已处理）'] == '南宁') & (df_two['需求等级'] == '中需求')]
df_two_7_2 = df_two[(df_two['地点（已处理）'] == '常州') & (df_two['需求等级'] == '中需求')]
df_two_8_2 = df_two[(df_two['地点（已处理）'] == '泉州') & (df_two['需求等级'] == '中需求')]
df_two_9_2 = df_two[(df_two['地点（已处理）'] == '芜湖') & (df_two['需求等级'] == '中需求')]
df_two_10_2 = df_two[(df_two['地点（已处理）'] == '桂林') & (df_two['需求等级'] == '中需求')]
df_two_11_2 = df_two[(df_two['地点（已处理）'] == '绍兴') & (df_two['需求等级'] == '中需求')]
df_two_12_2 = df_two[(df_two['地点（已处理）'] == '南昌') & (df_two['需求等级'] == '中需求')]
df_two_13_2 = df_two[(df_two['地点（已处理）'] == '南通') & (df_two['需求等级'] == '中需求')]
df_two_14_2 = df_two[(df_two['地点（已处理）'] == '烟台') & (df_two['需求等级'] == '中需求')]
df_two_15_2 = df_two[(df_two['地点（已处理）'] == '徐州') & (df_two['需求等级'] == '中需求')]
df_two_16_2 = df_two[(df_two['地点（已处理）'] == '昆明') & (df_two['需求等级'] == '中需求')]
df_two_17_2 = df_two[(df_two['地点（已处理）'] == '太原') & (df_two['需求等级'] == '中需求')]
df_two_18_2 = df_two[(df_two['地点（已处理）'] == '沈阳') & (df_two['需求等级'] == '中需求')]
df_two_19_2 = df_two[(df_two['地点（已处理）'] == '乌鲁木齐') & (df_two['需求等级'] == '中需求')]
df_two_20_2 = df_two[(df_two['地点（已处理）'] == '兰州') & (df_two['需求等级'] == '中需求')]
df_two_21_2 = df_two[(df_two['地点（已处理）'] == '宁德') & (df_two['需求等级'] == '中需求')]
df_two_22_2 = df_two[(df_two['地点（已处理）'] == '贵阳') & (df_two['需求等级'] == '中需求')]
df_two_23_2 = df_two[(df_two['地点（已处理）'] == '海口') & (df_two['需求等级'] == '中需求')]
df_two_24_2 = df_two[(df_two['地点（已处理）'] == '台州') & (df_two['需求等级'] == '中需求')]
df_two_25_2 = df_two[(df_two['地点（已处理）'] == '大庆') & (df_two['需求等级'] == '中需求')]
df_two_26_2 = df_two[(df_two['地点（已处理）'] == '盐城') & (df_two['需求等级'] == '中需求')]
df_two_27_2 = df_two[(df_two['地点（已处理）'] == '江西省') & (df_two['需求等级'] == '中需求')]
df_two_28_2 = df_two[(df_two['地点（已处理）'] == '宜昌') & (df_two['需求等级'] == '中需求')]
df_two_29_2 = df_two[(df_two['地点（已处理）'] == '廊坊') & (df_two['需求等级'] == '中需求')]
df_two_2 = [df_two_1_2.shape[0], df_two_2_2.shape[0],
              df_two_3_2.shape[0] + df_two_22_2.shape[0],
              df_two_4_2.shape[0], df_two_5_2.shape[0], df_two_6_2.shape[0],
              df_two_7_2.shape[0], df_two_8_2.shape[0] + df_two_23_2.shape[0],
              df_two_9_2.shape[0], df_two_10_2.shape[0], df_two_11_2.shape[0],
              df_two_12_2.shape[0], df_two_13_2.shape[0], df_two_14_2.shape[0],
              df_two_15_2.shape[0], df_two_16_2.shape[0] + df_two_21_2.shape[0],
              df_two_17_2.shape[0], df_two_18_2.shape[0],
              df_two_19_2.shape[0] + df_two_20_2.shape[0], df_two_27_2.shape[0],
              df_two_22_2.shape[0], df_two_23_2.shape[0], df_two_24_2.shape[0],
              df_two_25_2.shape[0], df_two_26_2.shape[0], df_two_27_2.shape[0],
              df_two_28_2.shape[0], df_two_29_2.shape[0]]

df_two_1_3 = df_two[(df_two['地点（已处理）'] == '大连') & (df_two['需求等级'] == '低需求')]
df_two_2_3 = df_two[(df_two['地点（已处理）'] == '中山') & (df_two['需求等级'] == '低需求')]
df_two_3_3 = df_two[(df_two['地点（已处理）'] == '宁波') & (df_two['需求等级'] == '低需求')]
df_two_4_3 = df_two[(df_two['地点（已处理）'] == '石家庄') & (df_two['需求等级'] == '低需求')]
df_two_5_3 = df_two[(df_two['地点（已处理）'] == '嘉兴') & (df_two['需求等级'] == '低需求')]
df_two_6_3 = df_two[(df_two['地点（已处理）'] == '南宁') & (df_two['需求等级'] == '低需求')]
df_two_7_3 = df_two[(df_two['地点（已处理）'] == '常州') & (df_two['需求等级'] == '低需求')]
df_two_8_3 = df_two[(df_two['地点（已处理）'] == '泉州') & (df_two['需求等级'] == '低需求')]
df_two_9_3 = df_two[(df_two['地点（已处理）'] == '芜湖') & (df_two['需求等级'] == '低需求')]
df_two_10_3 = df_two[(df_two['地点（已处理）'] == '桂林') & (df_two['需求等级'] == '低需求')]
df_two_11_3 = df_two[(df_two['地点（已处理）'] == '绍兴') & (df_two['需求等级'] == '低需求')]
df_two_12_3 = df_two[(df_two['地点（已处理）'] == '南昌') & (df_two['需求等级'] == '低需求')]
df_two_13_3 = df_two[(df_two['地点（已处理）'] == '南通') & (df_two['需求等级'] == '低需求')]
df_two_14_3 = df_two[(df_two['地点（已处理）'] == '烟台') & (df_two['需求等级'] == '低需求')]
df_two_15_3 = df_two[(df_two['地点（已处理）'] == '徐州') & (df_two['需求等级'] == '低需求')]
df_two_16_3 = df_two[(df_two['地点（已处理）'] == '昆明') & (df_two['需求等级'] == '低需求')]
df_two_17_3 = df_two[(df_two['地点（已处理）'] == '太原') & (df_two['需求等级'] == '低需求')]
df_two_18_3 = df_two[(df_two['地点（已处理）'] == '沈阳') & (df_two['需求等级'] == '低需求')]
df_two_19_3 = df_two[(df_two['地点（已处理）'] == '乌鲁木齐') & (df_two['需求等级'] == '低需求')]
df_two_20_3 = df_two[(df_two['地点（已处理）'] == '兰州') & (df_two['需求等级'] == '低需求')]
df_two_21_3 = df_two[(df_two['地点（已处理）'] == '宁德') & (df_two['需求等级'] == '低需求')]
df_two_22_3 = df_two[(df_two['地点（已处理）'] == '贵阳') & (df_two['需求等级'] == '低需求')]
df_two_23_3 = df_two[(df_two['地点（已处理）'] == '海口') & (df_two['需求等级'] == '低需求')]
df_two_24_3 = df_two[(df_two['地点（已处理）'] == '台州') & (df_two['需求等级'] == '低需求')]
df_two_25_3 = df_two[(df_two['地点（已处理）'] == '大庆') & (df_two['需求等级'] == '低需求')]
df_two_26_3 = df_two[(df_two['地点（已处理）'] == '盐城') & (df_two['需求等级'] == '低需求')]
df_two_27_3 = df_two[(df_two['地点（已处理）'] == '江西省') & (df_two['需求等级'] == '低需求')]
df_two_28_3 = df_two[(df_two['地点（已处理）'] == '宜昌') & (df_two['需求等级'] == '低需求')]
df_two_29_3 = df_two[(df_two['地点（已处理）'] == '廊坊') & (df_two['需求等级'] == '低需求')]
df_two_3 = [df_two_1_3.shape[0], df_two_2_3.shape[0],
              df_two_3_3.shape[0] + df_two_22_3.shape[0],
              df_two_4_3.shape[0], df_two_5_3.shape[0], df_two_6_3.shape[0],
              df_two_7_3.shape[0], df_two_8_3.shape[0] + df_two_23_3.shape[0],
              df_two_9_3.shape[0], df_two_10_3.shape[0], df_two_11_3.shape[0],
              df_two_12_3.shape[0], df_two_13_3.shape[0], df_two_14_3.shape[0],
              df_two_15_3.shape[0], df_two_16_3.shape[0] + df_two_21_3.shape[0],
              df_two_17_3.shape[0], df_two_18_3.shape[0],
              df_two_19_3.shape[0] + df_two_20_3.shape[0], df_two_27_3.shape[0],
              df_two_22_3.shape[0], df_two_23_3.shape[0], df_two_24_3.shape[0],
              df_two_25_3.shape[0], df_two_26_3.shape[0], df_two_27_3.shape[0],
              df_two_28_3.shape[0], df_two_29_3.shape[0]]


tick_label = ['大\n连', '中\n山', '宁\n波', '石\n家\n庄', '嘉\n兴', '南\n宁', '常\n州', '泉\n州', '芜\n湖', '桂\n林', '绍\n兴',
              '南\n昌', '南\n通', '烟\n台', '徐\n州', '昆\n明', '太\n原', '沈\n阳', '乌\n鲁\n木\n齐', '兰\n州', '宁\n德', '贵\n阳',
              '海\n口', '台\n州', '大\n庆', '盐\n城', '宜\n昌', '廊\n坊']
bar_width = 0.3
x = np.arange(len(tick_label))

plt.figure(dpi=433, figsize=(12, 6))
plt.title('二线城市岗位需求量图')
plt.bar(x, df_two_1, bar_width, align='center', label='高需求')
plt.bar(x + bar_width, df_two_2, bar_width, align='center', label='中需求')
plt.bar(x + 2 * bar_width, df_two_3, bar_width, align='center', label='低需求')
plt.xlabel('城市')
plt.ylabel('数量')
plt.xticks(x + bar_width / 3, tick_label)
plt.legend()
plt.savefig('fig.7 二线城市岗位需求量图（优化版）.png')
plt.show()
