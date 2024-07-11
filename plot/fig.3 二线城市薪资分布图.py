import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
df = pd.read_excel('result_all_normal.xlsx')
df_two = df[df['城市等级'] == '二线']
df_two_1_low = df_two[(df_two['地点（已处理）'] == '大连') & (df_two['薪资水平'] == '低')]
df_two_2_low = df_two[(df_two['地点（已处理）'] == '中山') & (df_two['薪资水平'] == '低')]
df_two_3_low = df_two[(df_two['地点（已处理）'] == '宁波') & (df_two['薪资水平'] == '低')]
df_two_4_low = df_two[(df_two['地点（已处理）'] == '石家庄') & (df_two['薪资水平'] == '低')]
df_two_5_low = df_two[(df_two['地点（已处理）'] == '嘉兴') & (df_two['薪资水平'] == '低')]
df_two_6_low = df_two[(df_two['地点（已处理）'] == '南宁') & (df_two['薪资水平'] == '低')]
df_two_7_low = df_two[(df_two['地点（已处理）'] == '常州') & (df_two['薪资水平'] == '低')]
df_two_8_low = df_two[(df_two['地点（已处理）'] == '泉州') & (df_two['薪资水平'] == '低')]
df_two_9_low = df_two[(df_two['地点（已处理）'] == '芜湖') & (df_two['薪资水平'] == '低')]
df_two_10_low = df_two[(df_two['地点（已处理）'] == '桂林') & (df_two['薪资水平'] == '低')]
df_two_11_low = df_two[(df_two['地点（已处理）'] == '绍兴') & (df_two['薪资水平'] == '低')]
df_two_12_low = df_two[(df_two['地点（已处理）'] == '南昌') & (df_two['薪资水平'] == '低')]
df_two_13_low = df_two[(df_two['地点（已处理）'] == '南通') & (df_two['薪资水平'] == '低')]
df_two_14_low = df_two[(df_two['地点（已处理）'] == '烟台') & (df_two['薪资水平'] == '低')]
df_two_15_low = df_two[(df_two['地点（已处理）'] == '徐州') & (df_two['薪资水平'] == '低')]
df_two_16_low = df_two[(df_two['地点（已处理）'] == '昆明') & (df_two['薪资水平'] == '低')]
df_two_17_low = df_two[(df_two['地点（已处理）'] == '太原') & (df_two['薪资水平'] == '低')]
df_two_18_low = df_two[(df_two['地点（已处理）'] == '沈阳') & (df_two['薪资水平'] == '低')]
df_two_19_low = df_two[(df_two['地点（已处理）'] == '乌鲁木齐') & (df_two['薪资水平'] == '低')]
df_two_20_low = df_two[(df_two['地点（已处理）'] == '兰州') & (df_two['薪资水平'] == '低')]
df_two_21_low = df_two[(df_two['地点（已处理）'] == '宁德') & (df_two['薪资水平'] == '低')]
df_two_22_low = df_two[(df_two['地点（已处理）'] == '贵阳') & (df_two['薪资水平'] == '低')]
df_two_23_low = df_two[(df_two['地点（已处理）'] == '海口') & (df_two['薪资水平'] == '低')]
df_two_24_low = df_two[(df_two['地点（已处理）'] == '台州') & (df_two['薪资水平'] == '低')]
df_two_25_low = df_two[(df_two['地点（已处理）'] == '大庆') & (df_two['薪资水平'] == '低')]
df_two_26_low = df_two[(df_two['地点（已处理）'] == '盐城') & (df_two['薪资水平'] == '低')]
df_two_27_low = df_two[(df_two['地点（已处理）'] == '江西省') & (df_two['薪资水平'] == '低')]
df_two_28_low = df_two[(df_two['地点（已处理）'] == '宜昌') & (df_two['薪资水平'] == '低')]
df_two_29_low = df_two[(df_two['地点（已处理）'] == '廊坊') & (df_two['薪资水平'] == '低')]
df_two_low = [df_two_1_low.shape[0], df_two_2_low.shape[0],
              df_two_3_low.shape[0] + df_two_22_low.shape[0],
              df_two_4_low.shape[0], df_two_5_low.shape[0], df_two_6_low.shape[0],
              df_two_7_low.shape[0], df_two_8_low.shape[0] + df_two_23_low.shape[0],
              df_two_9_low.shape[0], df_two_10_low.shape[0], df_two_11_low.shape[0],
              df_two_12_low.shape[0], df_two_13_low.shape[0], df_two_14_low.shape[0],
              df_two_15_low.shape[0], df_two_16_low.shape[0] + df_two_21_low.shape[0],
              df_two_17_low.shape[0], df_two_18_low.shape[0],
              df_two_19_low.shape[0] + df_two_20_low.shape[0], df_two_27_low.shape[0],
              df_two_22_low.shape[0], df_two_23_low.shape[0], df_two_24_low.shape[0],
              df_two_25_low.shape[0], df_two_26_low.shape[0], df_two_27_low.shape[0],
              df_two_28_low.shape[0], df_two_29_low.shape[0]]
df_two_1_mid = df_two[(df_two['地点（已处理）'] == '大连') & (df_two['薪资水平'] == '中')]
df_two_2_mid = df_two[(df_two['地点（已处理）'] == '中山') & (df_two['薪资水平'] == '中')]
df_two_3_mid = df_two[(df_two['地点（已处理）'] == '宁波') & (df_two['薪资水平'] == '中')]
df_two_4_mid = df_two[(df_two['地点（已处理）'] == '石家庄') & (df_two['薪资水平'] == '中')]
df_two_5_mid = df_two[(df_two['地点（已处理）'] == '嘉兴') & (df_two['薪资水平'] == '中')]
df_two_6_mid = df_two[(df_two['地点（已处理）'] == '南宁') & (df_two['薪资水平'] == '中')]
df_two_7_mid = df_two[(df_two['地点（已处理）'] == '常州') & (df_two['薪资水平'] == '中')]
df_two_8_mid = df_two[(df_two['地点（已处理）'] == '泉州') & (df_two['薪资水平'] == '中')]
df_two_9_mid = df_two[(df_two['地点（已处理）'] == '芜湖') & (df_two['薪资水平'] == '中')]
df_two_10_mid = df_two[(df_two['地点（已处理）'] == '桂林') & (df_two['薪资水平'] == '中')]
df_two_11_mid = df_two[(df_two['地点（已处理）'] == '绍兴') & (df_two['薪资水平'] == '中')]
df_two_12_mid = df_two[(df_two['地点（已处理）'] == '南昌') & (df_two['薪资水平'] == '中')]
df_two_13_mid = df_two[(df_two['地点（已处理）'] == '南通') & (df_two['薪资水平'] == '中')]
df_two_14_mid = df_two[(df_two['地点（已处理）'] == '烟台') & (df_two['薪资水平'] == '中')]
df_two_15_mid = df_two[(df_two['地点（已处理）'] == '徐州') & (df_two['薪资水平'] == '中')]
df_two_16_mid = df_two[(df_two['地点（已处理）'] == '昆明') & (df_two['薪资水平'] == '中')]
df_two_17_mid = df_two[(df_two['地点（已处理）'] == '太原') & (df_two['薪资水平'] == '中')]
df_two_18_mid = df_two[(df_two['地点（已处理）'] == '沈阳') & (df_two['薪资水平'] == '中')]
df_two_19_mid = df_two[(df_two['地点（已处理）'] == '乌鲁木齐') & (df_two['薪资水平'] == '中')]
df_two_20_mid = df_two[(df_two['地点（已处理）'] == '兰州') & (df_two['薪资水平'] == '中')]
df_two_21_mid = df_two[(df_two['地点（已处理）'] == '宁德') & (df_two['薪资水平'] == '中')]
df_two_22_mid = df_two[(df_two['地点（已处理）'] == '贵阳') & (df_two['薪资水平'] == '中')]
df_two_23_mid = df_two[(df_two['地点（已处理）'] == '海口') & (df_two['薪资水平'] == '中')]
df_two_24_mid = df_two[(df_two['地点（已处理）'] == '台州') & (df_two['薪资水平'] == '中')]
df_two_25_mid = df_two[(df_two['地点（已处理）'] == '大庆') & (df_two['薪资水平'] == '中')]
df_two_26_mid = df_two[(df_two['地点（已处理）'] == '盐城') & (df_two['薪资水平'] == '中')]
df_two_27_mid = df_two[(df_two['地点（已处理）'] == '江西省') & (df_two['薪资水平'] == '中')]
df_two_28_mid = df_two[(df_two['地点（已处理）'] == '宜昌') & (df_two['薪资水平'] == '中')]
df_two_29_mid = df_two[(df_two['地点（已处理）'] == '廊坊') & (df_two['薪资水平'] == '中')]
df_two_mid = [df_two_1_mid.shape[0], df_two_2_mid.shape[0],
              df_two_3_mid.shape[0] + df_two_22_mid.shape[0],
              df_two_4_mid.shape[0], df_two_5_mid.shape[0], df_two_6_mid.shape[0],
              df_two_7_mid.shape[0], df_two_8_mid.shape[0] + df_two_23_mid.shape[0],
              df_two_9_mid.shape[0], df_two_10_mid.shape[0], df_two_11_mid.shape[0],
              df_two_12_mid.shape[0], df_two_13_mid.shape[0], df_two_14_mid.shape[0],
              df_two_15_mid.shape[0], df_two_16_mid.shape[0] + df_two_21_mid.shape[0],
              df_two_17_mid.shape[0], df_two_18_mid.shape[0],
              df_two_19_mid.shape[0] + df_two_20_mid.shape[0], df_two_27_mid.shape[0],
              df_two_22_mid.shape[0], df_two_23_mid.shape[0], df_two_24_mid.shape[0],
              df_two_25_mid.shape[0], df_two_26_mid.shape[0], df_two_27_mid.shape[0],
              df_two_28_mid.shape[0], df_two_29_mid.shape[0]]
df_two_1_hig = df_two[(df_two['地点（已处理）'] == '大连') & (df_two['薪资水平'] == '高')]
df_two_2_hig = df_two[(df_two['地点（已处理）'] == '中山') & (df_two['薪资水平'] == '高')]
df_two_3_hig = df_two[(df_two['地点（已处理）'] == '宁波') & (df_two['薪资水平'] == '高')]
df_two_4_hig = df_two[(df_two['地点（已处理）'] == '石家庄') & (df_two['薪资水平'] == '高')]
df_two_5_hig = df_two[(df_two['地点（已处理）'] == '嘉兴') & (df_two['薪资水平'] == '高')]
df_two_6_hig = df_two[(df_two['地点（已处理）'] == '南宁') & (df_two['薪资水平'] == '高')]
df_two_7_hig = df_two[(df_two['地点（已处理）'] == '常州') & (df_two['薪资水平'] == '高')]
df_two_8_hig = df_two[(df_two['地点（已处理）'] == '泉州') & (df_two['薪资水平'] == '高')]
df_two_9_hig = df_two[(df_two['地点（已处理）'] == '芜湖') & (df_two['薪资水平'] == '高')]
df_two_10_hig = df_two[(df_two['地点（已处理）'] == '桂林') & (df_two['薪资水平'] == '高')]
df_two_11_hig = df_two[(df_two['地点（已处理）'] == '绍兴') & (df_two['薪资水平'] == '高')]
df_two_12_hig = df_two[(df_two['地点（已处理）'] == '南昌') & (df_two['薪资水平'] == '高')]
df_two_13_hig = df_two[(df_two['地点（已处理）'] == '南通') & (df_two['薪资水平'] == '高')]
df_two_14_hig = df_two[(df_two['地点（已处理）'] == '烟台') & (df_two['薪资水平'] == '高')]
df_two_15_hig = df_two[(df_two['地点（已处理）'] == '徐州') & (df_two['薪资水平'] == '高')]
df_two_16_hig = df_two[(df_two['地点（已处理）'] == '昆明') & (df_two['薪资水平'] == '高')]
df_two_17_hig = df_two[(df_two['地点（已处理）'] == '太原') & (df_two['薪资水平'] == '高')]
df_two_18_hig = df_two[(df_two['地点（已处理）'] == '沈阳') & (df_two['薪资水平'] == '高')]
df_two_19_hig = df_two[(df_two['地点（已处理）'] == '乌鲁木齐') & (df_two['薪资水平'] == '高')]
df_two_20_hig = df_two[(df_two['地点（已处理）'] == '兰州') & (df_two['薪资水平'] == '高')]
df_two_21_hig = df_two[(df_two['地点（已处理）'] == '宁德') & (df_two['薪资水平'] == '高')]
df_two_22_hig = df_two[(df_two['地点（已处理）'] == '贵阳') & (df_two['薪资水平'] == '高')]
df_two_23_hig = df_two[(df_two['地点（已处理）'] == '海口') & (df_two['薪资水平'] == '高')]
df_two_24_hig = df_two[(df_two['地点（已处理）'] == '台州') & (df_two['薪资水平'] == '高')]
df_two_25_hig = df_two[(df_two['地点（已处理）'] == '大庆') & (df_two['薪资水平'] == '高')]
df_two_26_hig = df_two[(df_two['地点（已处理）'] == '盐城') & (df_two['薪资水平'] == '高')]
df_two_27_hig = df_two[(df_two['地点（已处理）'] == '江西省') & (df_two['薪资水平'] == '高')]
df_two_28_hig = df_two[(df_two['地点（已处理）'] == '宜昌') & (df_two['薪资水平'] == '高')]
df_two_29_hig = df_two[(df_two['地点（已处理）'] == '廊坊') & (df_two['薪资水平'] == '高')]
df_two_hig = [df_two_1_hig.shape[0], df_two_2_hig.shape[0],
              df_two_3_hig.shape[0] + df_two_22_hig.shape[0],
              df_two_4_hig.shape[0], df_two_5_hig.shape[0], df_two_6_hig.shape[0],
              df_two_7_hig.shape[0], df_two_8_hig.shape[0] + df_two_23_hig.shape[0],
              df_two_9_hig.shape[0], df_two_10_hig.shape[0], df_two_11_hig.shape[0],
              df_two_12_hig.shape[0], df_two_13_hig.shape[0], df_two_14_hig.shape[0],
              df_two_15_hig.shape[0], df_two_16_hig.shape[0] + df_two_21_hig.shape[0],
              df_two_17_hig.shape[0], df_two_18_hig.shape[0],
              df_two_19_hig.shape[0] + df_two_20_hig.shape[0], df_two_27_hig.shape[0],
              df_two_22_hig.shape[0], df_two_23_hig.shape[0], df_two_24_hig.shape[0],
              df_two_25_hig.shape[0], df_two_26_hig.shape[0], df_two_27_hig.shape[0],
              df_two_28_hig.shape[0], df_two_29_hig.shape[0]]

tick_label = ['大\n连', '中\n山', '宁\n波', '石\n家\n庄', '嘉\n兴', '南\n宁', '常\n州', '泉\n州', '芜\n湖', '桂\n林', '绍\n兴',
              '南\n昌', '南\n通', '烟\n台', '徐\n州', '昆\n明', '太\n原', '沈\n阳', '乌\n鲁\n木\n齐', '兰\n州', '宁\n德', '贵\n阳',
              '海\n口', '台\n州', '大\n庆', '盐\n城', '宜\n昌', '廊\n坊']
bar_width = 0.3
x = np.arange(len(tick_label))
plt.figure(dpi=433, figsize=(12, 6))
plt.title('二线城市薪资分布图')
plt.bar(x, df_two_low, bar_width, align='center', label='低薪资')
plt.bar(x + bar_width, df_two_mid, bar_width, align='center', label='中薪资')
plt.bar(x + 2 * bar_width, df_two_hig, bar_width, align='center', label='高薪资')
plt.xlabel('城市')
plt.ylabel('数量')
plt.xticks(x + bar_width / 3, tick_label)
plt.legend()
plt.savefig('fig.3 二线城市薪资分布图.png')
plt.show()
