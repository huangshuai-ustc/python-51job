import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
df = pd.read_excel('result_all_normal.xlsx')
df_one = df[df['城市等级'] == '一线']
df_one_1_low = df_one[(df_one['地点（已处理）'] == '北京') & (df_one['薪资水平'] == '低')]
df_one_2_low = df_one[(df_one['地点（已处理）'] == '上海') & (df_one['薪资水平'] == '低')]
df_one_3_low = df_one[(df_one['地点（已处理）'] == '深圳') & (df_one['薪资水平'] == '低')]
df_one_4_low = df_one[(df_one['地点（已处理）'] == '广州') & (df_one['薪资水平'] == '低')]
df_one_5_low = df_one[(df_one['地点（已处理）'] == '无锡') & (df_one['薪资水平'] == '低')]
df_one_6_low = df_one[(df_one['地点（已处理）'] == '苏州') & (df_one['薪资水平'] == '低')]
df_one_7_low = df_one[(df_one['地点（已处理）'] == '宁波') & (df_one['薪资水平'] == '低')]
df_one_8_low = df_one[(df_one['地点（已处理）'] == '杭州') & (df_one['薪资水平'] == '低')]
df_one_9_low = df_one[(df_one['地点（已处理）'] == '天津') & (df_one['薪资水平'] == '低')]
df_one_10_low = df_one[(df_one['地点（已处理）'] == '重庆') & (df_one['薪资水平'] == '低')]
df_one_11_low = df_one[(df_one['地点（已处理）'] == '青岛') & (df_one['薪资水平'] == '低')]
df_one_12_low = df_one[(df_one['地点（已处理）'] == '西安') & (df_one['薪资水平'] == '低')]
df_one_13_low = df_one[(df_one['地点（已处理）'] == '东莞') & (df_one['薪资水平'] == '低')]
df_one_14_low = df_one[(df_one['地点（已处理）'] == '成都') & (df_one['薪资水平'] == '低')]
df_one_15_low = df_one[(df_one['地点（已处理）'] == '佛山') & (df_one['薪资水平'] == '低')]
df_one_16_low = df_one[(df_one['地点（已处理）'] == '南京') & (df_one['薪资水平'] == '低')]
df_one_17_low = df_one[(df_one['地点（已处理）'] == '长沙') & (df_one['薪资水平'] == '低')]
df_one_18_low = df_one[(df_one['地点（已处理）'] == '哈尔滨') & (df_one['薪资水平'] == '低')]
df_one_19_low = df_one[(df_one['地点（已处理）'] == '武汉') & (df_one['薪资水平'] == '低')]
df_one_20_low = df_one[(df_one['地点（已处理）'] == '湖北省') & (df_one['薪资水平'] == '低')]
df_one_21_low = df_one[(df_one['地点（已处理）'] == '江苏省') & (df_one['薪资水平'] == '低')]
df_one_22_low = df_one[(df_one['地点（已处理）'] == '广东省') & (df_one['薪资水平'] == '低')]
df_one_23_low = df_one[(df_one['地点（已处理）'] == '浙江省') & (df_one['薪资水平'] == '低')]
df_one_24_low = df_one[(df_one['地点（已处理）'] == '珠海') & (df_one['薪资水平'] == '低')]
df_one_25_low = df_one[(df_one['地点（已处理）'] == '合肥') & (df_one['薪资水平'] == '低')]
df_one_26_low = df_one[(df_one['地点（已处理）'] == '济南') & (df_one['薪资水平'] == '低')]
df_one_27_low = df_one[(df_one['地点（已处理）'] == '山东省') & (df_one['薪资水平'] == '低')]
df_one_28_low = df_one[(df_one['地点（已处理）'] == '郑州') & (df_one['薪资水平'] == '低')]
df_one_henan_low = df_one[(df_one['地点（已处理）'] == '河南省') & (df_one['薪资水平'] == '低')]
df_one_low = [df_one_1_low.shape[0], df_one_2_low.shape[0],
              df_one_3_low.shape[0] + df_one_22_low.shape[0],
              df_one_4_low.shape[0], df_one_5_low.shape[0], df_one_6_low.shape[0],
              df_one_7_low.shape[0], df_one_8_low.shape[0] + df_one_23_low.shape[0],
              df_one_9_low.shape[0], df_one_10_low.shape[0], df_one_11_low.shape[0],
              df_one_12_low.shape[0], df_one_13_low.shape[0], df_one_14_low.shape[0],
              df_one_15_low.shape[0], df_one_16_low.shape[0] + df_one_21_low.shape[0],
              df_one_17_low.shape[0], df_one_18_low.shape[0],
              df_one_19_low.shape[0] + df_one_20_low.shape[0], df_one_24_low.shape[0],
              df_one_25_low.shape[0], df_one_26_low.shape[0] + df_one_27_low.shape[0],
              df_one_28_low.shape[0] + df_one_henan_low.shape[0]]
df_one_1_mid = df_one[(df_one['地点（已处理）'] == '北京') & (df_one['薪资水平'] == '中')]
df_one_2_mid = df_one[(df_one['地点（已处理）'] == '上海') & (df_one['薪资水平'] == '中')]
df_one_3_mid = df_one[(df_one['地点（已处理）'] == '深圳') & (df_one['薪资水平'] == '中')]
df_one_4_mid = df_one[(df_one['地点（已处理）'] == '广州') & (df_one['薪资水平'] == '中')]
df_one_5_mid = df_one[(df_one['地点（已处理）'] == '无锡') & (df_one['薪资水平'] == '中')]
df_one_6_mid = df_one[(df_one['地点（已处理）'] == '苏州') & (df_one['薪资水平'] == '中')]
df_one_7_mid = df_one[(df_one['地点（已处理）'] == '宁波') & (df_one['薪资水平'] == '中')]
df_one_8_mid = df_one[(df_one['地点（已处理）'] == '杭州') & (df_one['薪资水平'] == '中')]
df_one_9_mid = df_one[(df_one['地点（已处理）'] == '天津') & (df_one['薪资水平'] == '中')]
df_one_10_mid = df_one[(df_one['地点（已处理）'] == '重庆') & (df_one['薪资水平'] == '中')]
df_one_11_mid = df_one[(df_one['地点（已处理）'] == '青岛') & (df_one['薪资水平'] == '中')]
df_one_12_mid = df_one[(df_one['地点（已处理）'] == '西安') & (df_one['薪资水平'] == '中')]
df_one_13_mid = df_one[(df_one['地点（已处理）'] == '东莞') & (df_one['薪资水平'] == '中')]
df_one_14_mid = df_one[(df_one['地点（已处理）'] == '成都') & (df_one['薪资水平'] == '中')]
df_one_15_mid = df_one[(df_one['地点（已处理）'] == '佛山') & (df_one['薪资水平'] == '中')]
df_one_16_mid = df_one[(df_one['地点（已处理）'] == '南京') & (df_one['薪资水平'] == '中')]
df_one_17_mid = df_one[(df_one['地点（已处理）'] == '长沙') & (df_one['薪资水平'] == '中')]
df_one_18_mid = df_one[(df_one['地点（已处理）'] == '哈尔滨') & (df_one['薪资水平'] == '中')]
df_one_19_mid = df_one[(df_one['地点（已处理）'] == '武汉') & (df_one['薪资水平'] == '中')]
df_one_20_mid = df_one[(df_one['地点（已处理）'] == '湖北省') & (df_one['薪资水平'] == '中')]
df_one_21_mid = df_one[(df_one['地点（已处理）'] == '江苏省') & (df_one['薪资水平'] == '中')]
df_one_22_mid = df_one[(df_one['地点（已处理）'] == '广东省') & (df_one['薪资水平'] == '中')]
df_one_23_mid = df_one[(df_one['地点（已处理）'] == '浙江省') & (df_one['薪资水平'] == '中')]
df_one_24_mid = df_one[(df_one['地点（已处理）'] == '珠海') & (df_one['薪资水平'] == '中')]
df_one_25_mid = df_one[(df_one['地点（已处理）'] == '合肥') & (df_one['薪资水平'] == '中')]
df_one_26_mid = df_one[(df_one['地点（已处理）'] == '济南') & (df_one['薪资水平'] == '中')]
df_one_27_mid = df_one[(df_one['地点（已处理）'] == '山东省') & (df_one['薪资水平'] == '中')]
df_one_28_mid = df_one[(df_one['地点（已处理）'] == '郑州') & (df_one['薪资水平'] == '中')]
df_one_henan_mid = df_one[(df_one['地点（已处理）'] == '河南省') & (df_one['薪资水平'] == '中')]
df_one_mid = [df_one_1_mid.shape[0], df_one_2_mid.shape[0],
              df_one_3_mid.shape[0] + df_one_22_mid.shape[0],
              df_one_4_mid.shape[0], df_one_5_mid.shape[0], df_one_6_mid.shape[0],
              df_one_7_mid.shape[0], df_one_8_mid.shape[0] + df_one_23_mid.shape[0],
              df_one_9_mid.shape[0], df_one_10_mid.shape[0], df_one_11_mid.shape[0],
              df_one_12_mid.shape[0], df_one_13_mid.shape[0], df_one_14_mid.shape[0],
              df_one_15_mid.shape[0], df_one_16_mid.shape[0] + df_one_21_mid.shape[0],
              df_one_17_mid.shape[0], df_one_18_mid.shape[0],
              df_one_19_mid.shape[0] + df_one_20_mid.shape[0], df_one_24_mid.shape[0],
              df_one_25_mid.shape[0], df_one_26_mid.shape[0] + df_one_27_mid.shape[0],
              df_one_28_mid.shape[0] + df_one_henan_mid.shape[0]]
df_one_1_hig = df_one[(df_one['地点（已处理）'] == '北京') & (df_one['薪资水平'] == '高')]
df_one_2_hig = df_one[(df_one['地点（已处理）'] == '上海') & (df_one['薪资水平'] == '高')]
df_one_3_hig = df_one[(df_one['地点（已处理）'] == '深圳') & (df_one['薪资水平'] == '高')]
df_one_4_hig = df_one[(df_one['地点（已处理）'] == '广州') & (df_one['薪资水平'] == '高')]
df_one_5_hig = df_one[(df_one['地点（已处理）'] == '无锡') & (df_one['薪资水平'] == '高')]
df_one_6_hig = df_one[(df_one['地点（已处理）'] == '苏州') & (df_one['薪资水平'] == '高')]
df_one_7_hig = df_one[(df_one['地点（已处理）'] == '宁波') & (df_one['薪资水平'] == '高')]
df_one_8_hig = df_one[(df_one['地点（已处理）'] == '杭州') & (df_one['薪资水平'] == '高')]
df_one_9_hig = df_one[(df_one['地点（已处理）'] == '天津') & (df_one['薪资水平'] == '高')]
df_one_10_hig = df_one[(df_one['地点（已处理）'] == '重庆') & (df_one['薪资水平'] == '高')]
df_one_11_hig = df_one[(df_one['地点（已处理）'] == '青岛') & (df_one['薪资水平'] == '高')]
df_one_12_hig = df_one[(df_one['地点（已处理）'] == '西安') & (df_one['薪资水平'] == '高')]
df_one_13_hig = df_one[(df_one['地点（已处理）'] == '东莞') & (df_one['薪资水平'] == '高')]
df_one_14_hig = df_one[(df_one['地点（已处理）'] == '成都') & (df_one['薪资水平'] == '高')]
df_one_15_hig = df_one[(df_one['地点（已处理）'] == '佛山') & (df_one['薪资水平'] == '高')]
df_one_16_hig = df_one[(df_one['地点（已处理）'] == '南京') & (df_one['薪资水平'] == '高')]
df_one_17_hig = df_one[(df_one['地点（已处理）'] == '长沙') & (df_one['薪资水平'] == '高')]
df_one_18_hig = df_one[(df_one['地点（已处理）'] == '哈尔滨') & (df_one['薪资水平'] == '高')]
df_one_19_hig = df_one[(df_one['地点（已处理）'] == '武汉') & (df_one['薪资水平'] == '高')]
df_one_20_hig = df_one[(df_one['地点（已处理）'] == '湖北省') & (df_one['薪资水平'] == '高')]
df_one_21_hig = df_one[(df_one['地点（已处理）'] == '江苏省') & (df_one['薪资水平'] == '高')]
df_one_22_hig = df_one[(df_one['地点（已处理）'] == '广东省') & (df_one['薪资水平'] == '高')]
df_one_23_hig = df_one[(df_one['地点（已处理）'] == '浙江省') & (df_one['薪资水平'] == '高')]
df_one_24_hig = df_one[(df_one['地点（已处理）'] == '珠海') & (df_one['薪资水平'] == '高')]
df_one_25_hig = df_one[(df_one['地点（已处理）'] == '合肥') & (df_one['薪资水平'] == '高')]
df_one_26_hig = df_one[(df_one['地点（已处理）'] == '济南') & (df_one['薪资水平'] == '高')]
df_one_27_hig = df_one[(df_one['地点（已处理）'] == '山东省') & (df_one['薪资水平'] == '高')]
df_one_28_hig = df_one[(df_one['地点（已处理）'] == '郑州') & (df_one['薪资水平'] == '高')]
df_one_henan_hig = df_one[(df_one['地点（已处理）'] == '河南省') & (df_one['薪资水平'] == '高')]
df_one_hig = [df_one_1_hig.shape[0], df_one_2_hig.shape[0],
              df_one_3_hig.shape[0] + df_one_22_hig.shape[0],
              df_one_4_hig.shape[0], df_one_5_hig.shape[0], df_one_6_hig.shape[0],
              df_one_7_hig.shape[0], df_one_8_hig.shape[0] + df_one_23_hig.shape[0],
              df_one_9_hig.shape[0], df_one_10_hig.shape[0], df_one_11_hig.shape[0],
              df_one_12_hig.shape[0], df_one_13_hig.shape[0], df_one_14_hig.shape[0],
              df_one_15_hig.shape[0], df_one_16_hig.shape[0] + df_one_21_hig.shape[0],
              df_one_17_hig.shape[0], df_one_18_hig.shape[0],
              df_one_19_hig.shape[0] + df_one_20_hig.shape[0], df_one_24_hig.shape[0],
              df_one_25_hig.shape[0], df_one_26_hig.shape[0] + df_one_27_hig.shape[0],
              df_one_28_hig.shape[0] + df_one_henan_hig.shape[0]]
tick_label = ['北京', '上海', '深圳', '广州', '无锡', '苏州', '宁波', '杭州', '天津', '重庆', '青岛', '西安', '东莞',
              '成都', '佛山', '南京', '长沙', '哈尔滨', '武汉', '珠海', '合肥', '济南', '郑州']
bar_width = 0.3
x = np.arange(len(tick_label))
plt.figure(dpi=433, figsize=(10, 6))
plt.title('一线城市薪资分布图')
plt.bar(x, df_one_low, bar_width, align='center', label='低薪资')
plt.bar(x + bar_width, df_one_mid, bar_width, align='center', label='中薪资')
plt.bar(x + 2 * bar_width, df_one_hig, bar_width, align='center', label='高薪资')
plt.xlabel('城市')
plt.ylabel('数量')
plt.xticks(x + bar_width / 3, tick_label)
plt.legend()
plt.savefig('fig.2 一线城市薪资分布图.png')
plt.show()
