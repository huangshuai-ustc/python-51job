import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
df = pd.read_excel('result_all_normal.xlsx')
df_one = df[df['城市等级'] == '一线']
df_one_1_1 = df_one[(df_one['地点（已处理）'] == '北京') & (df_one['需求'] == '10000人以上')]
df_one_2_1 = df_one[(df_one['地点（已处理）'] == '上海') & (df_one['需求'] == '10000人以上')]
df_one_3_1 = df_one[(df_one['地点（已处理）'] == '深圳') & (df_one['需求'] == '10000人以上')]
df_one_4_1 = df_one[(df_one['地点（已处理）'] == '广州') & (df_one['需求'] == '10000人以上')]
df_one_5_1 = df_one[(df_one['地点（已处理）'] == '无锡') & (df_one['需求'] == '10000人以上')]
df_one_6_1 = df_one[(df_one['地点（已处理）'] == '苏州') & (df_one['需求'] == '10000人以上')]
df_one_7_1 = df_one[(df_one['地点（已处理）'] == '宁波') & (df_one['需求'] == '10000人以上')]
df_one_8_1 = df_one[(df_one['地点（已处理）'] == '杭州') & (df_one['需求'] == '10000人以上')]
df_one_9_1 = df_one[(df_one['地点（已处理）'] == '天津') & (df_one['需求'] == '10000人以上')]
df_one_10_1 = df_one[(df_one['地点（已处理）'] == '重庆') & (df_one['需求'] == '10000人以上')]
df_one_11_1 = df_one[(df_one['地点（已处理）'] == '青岛') & (df_one['需求'] == '10000人以上')]
df_one_12_1 = df_one[(df_one['地点（已处理）'] == '西安') & (df_one['需求'] == '10000人以上')]
df_one_13_1 = df_one[(df_one['地点（已处理）'] == '东莞') & (df_one['需求'] == '10000人以上')]
df_one_14_1 = df_one[(df_one['地点（已处理）'] == '成都') & (df_one['需求'] == '10000人以上')]
df_one_15_1 = df_one[(df_one['地点（已处理）'] == '佛山') & (df_one['需求'] == '10000人以上')]
df_one_16_1 = df_one[(df_one['地点（已处理）'] == '南京') & (df_one['需求'] == '10000人以上')]
df_one_17_1 = df_one[(df_one['地点（已处理）'] == '长沙') & (df_one['需求'] == '10000人以上')]
df_one_18_1 = df_one[(df_one['地点（已处理）'] == '哈尔滨') & (df_one['需求'] == '10000人以上')]
df_one_19_1 = df_one[(df_one['地点（已处理）'] == '武汉') & (df_one['需求'] == '10000人以上')]
df_one_20_1 = df_one[(df_one['地点（已处理）'] == '湖北省') & (df_one['需求'] == '10000人以上')]
df_one_21_1 = df_one[(df_one['地点（已处理）'] == '江苏省') & (df_one['需求'] == '10000人以上')]
df_one_22_1 = df_one[(df_one['地点（已处理）'] == '广东省') & (df_one['需求'] == '10000人以上')]
df_one_23_1 = df_one[(df_one['地点（已处理）'] == '浙江省') & (df_one['需求'] == '10000人以上')]
df_one_24_1 = df_one[(df_one['地点（已处理）'] == '珠海') & (df_one['需求'] == '10000人以上')]
df_one_25_1 = df_one[(df_one['地点（已处理）'] == '合肥') & (df_one['需求'] == '10000人以上')]
df_one_26_1 = df_one[(df_one['地点（已处理）'] == '济南') & (df_one['需求'] == '10000人以上')]
df_one_27_1 = df_one[(df_one['地点（已处理）'] == '山东省') & (df_one['需求'] == '10000人以上')]
df_one_28_1 = df_one[(df_one['地点（已处理）'] == '郑州') & (df_one['需求'] == '10000人以上')]
df_one_29_1 = df_one[(df_one['地点（已处理）'] == '河南省') & (df_one['需求'] == '10000人以上')]
df_one_1 = [df_one_1_1.shape[0], df_one_2_1.shape[0],
            df_one_3_1.shape[0] + df_one_4_1.shape[0],
            df_one_5_1.shape[0], df_one_6_1.shape[0], df_one_7_1.shape[0],
            df_one_8_1.shape[0], df_one_9_1.shape[0] + df_one_10_1.shape[0],
            df_one_11_1.shape[0], df_one_12_1.shape[0], df_one_13_1.shape[0],
            df_one_14_1.shape[0], df_one_15_1.shape[0], df_one_16_1.shape[0],
            df_one_17_1.shape[0], df_one_18_1.shape[0] + df_one_19_1.shape[0],
            df_one_20_1.shape[0], df_one_21_1.shape[0],
            df_one_22_1.shape[0] + df_one_23_1.shape[0], df_one_24_1.shape[0],
            df_one_25_1.shape[0], df_one_26_1.shape[0] + df_one_27_1.shape[0],
            df_one_28_1.shape[0] + df_one_29_1.shape[0]]

df_one_1_2 = df_one[(df_one['地点（已处理）'] == '北京') & (df_one['需求'] == '5000-10000人')]
df_one_2_2 = df_one[(df_one['地点（已处理）'] == '上海') & (df_one['需求'] == '5000-10000人')]
df_one_3_2 = df_one[(df_one['地点（已处理）'] == '深圳') & (df_one['需求'] == '5000-10000人')]
df_one_4_2 = df_one[(df_one['地点（已处理）'] == '广州') & (df_one['需求'] == '5000-10000人')]
df_one_5_2 = df_one[(df_one['地点（已处理）'] == '无锡') & (df_one['需求'] == '5000-10000人')]
df_one_6_2 = df_one[(df_one['地点（已处理）'] == '苏州') & (df_one['需求'] == '5000-10000人')]
df_one_7_2 = df_one[(df_one['地点（已处理）'] == '宁波') & (df_one['需求'] == '5000-10000人')]
df_one_8_2 = df_one[(df_one['地点（已处理）'] == '杭州') & (df_one['需求'] == '5000-10000人')]
df_one_9_2 = df_one[(df_one['地点（已处理）'] == '天津') & (df_one['需求'] == '5000-10000人')]
df_one_10_2 = df_one[(df_one['地点（已处理）'] == '重庆') & (df_one['需求'] == '5000-10000人')]
df_one_11_2 = df_one[(df_one['地点（已处理）'] == '青岛') & (df_one['需求'] == '5000-10000人')]
df_one_12_2 = df_one[(df_one['地点（已处理）'] == '西安') & (df_one['需求'] == '5000-10000人')]
df_one_13_2 = df_one[(df_one['地点（已处理）'] == '东莞') & (df_one['需求'] == '5000-10000人')]
df_one_14_2 = df_one[(df_one['地点（已处理）'] == '成都') & (df_one['需求'] == '5000-10000人')]
df_one_15_2 = df_one[(df_one['地点（已处理）'] == '佛山') & (df_one['需求'] == '5000-10000人')]
df_one_16_2 = df_one[(df_one['地点（已处理）'] == '南京') & (df_one['需求'] == '5000-10000人')]
df_one_17_2 = df_one[(df_one['地点（已处理）'] == '长沙') & (df_one['需求'] == '5000-10000人')]
df_one_18_2 = df_one[(df_one['地点（已处理）'] == '哈尔滨') & (df_one['需求'] == '5000-10000人')]
df_one_19_2 = df_one[(df_one['地点（已处理）'] == '武汉') & (df_one['需求'] == '5000-10000人')]
df_one_20_2 = df_one[(df_one['地点（已处理）'] == '湖北省') & (df_one['需求'] == '5000-10000人')]
df_one_21_2 = df_one[(df_one['地点（已处理）'] == '江苏省') & (df_one['需求'] == '5000-10000人')]
df_one_22_2 = df_one[(df_one['地点（已处理）'] == '广东省') & (df_one['需求'] == '5000-10000人')]
df_one_23_2 = df_one[(df_one['地点（已处理）'] == '浙江省') & (df_one['需求'] == '5000-10000人')]
df_one_24_2 = df_one[(df_one['地点（已处理）'] == '珠海') & (df_one['需求'] == '5000-10000人')]
df_one_25_2 = df_one[(df_one['地点（已处理）'] == '合肥') & (df_one['需求'] == '5000-10000人')]
df_one_26_2 = df_one[(df_one['地点（已处理）'] == '济南') & (df_one['需求'] == '5000-10000人')]
df_one_27_2 = df_one[(df_one['地点（已处理）'] == '山东省') & (df_one['需求'] == '5000-10000人')]
df_one_28_2 = df_one[(df_one['地点（已处理）'] == '郑州') & (df_one['需求'] == '5000-10000人')]
df_one_29_2 = df_one[(df_one['地点（已处理）'] == '河南省') & (df_one['需求'] == '5000-10000人')]
df_one_2 = [df_one_1_2.shape[0], df_one_2_2.shape[0],
            df_one_3_2.shape[0] + df_one_4_2.shape[0],
            df_one_5_2.shape[0], df_one_6_2.shape[0], df_one_7_2.shape[0],
            df_one_8_2.shape[0], df_one_9_2.shape[0] + df_one_10_2.shape[0],
            df_one_11_2.shape[0], df_one_12_2.shape[0], df_one_13_2.shape[0],
            df_one_14_2.shape[0], df_one_15_2.shape[0], df_one_16_2.shape[0],
            df_one_17_2.shape[0], df_one_18_2.shape[0] + df_one_19_2.shape[0],
            df_one_20_2.shape[0], df_one_21_2.shape[0],
            df_one_22_2.shape[0] + df_one_23_2.shape[0], df_one_24_2.shape[0],
            df_one_25_2.shape[0], df_one_26_2.shape[0] + df_one_27_2.shape[0],
            df_one_28_2.shape[0] + df_one_29_2.shape[0]]

df_one_1_3 = df_one[(df_one['地点（已处理）'] == '北京') & (df_one['需求'] == '1000-5000人')]
df_one_2_3 = df_one[(df_one['地点（已处理）'] == '上海') & (df_one['需求'] == '1000-5000人')]
df_one_3_3 = df_one[(df_one['地点（已处理）'] == '深圳') & (df_one['需求'] == '1000-5000人')]
df_one_4_3 = df_one[(df_one['地点（已处理）'] == '广州') & (df_one['需求'] == '1000-5000人')]
df_one_5_3 = df_one[(df_one['地点（已处理）'] == '无锡') & (df_one['需求'] == '1000-5000人')]
df_one_6_3 = df_one[(df_one['地点（已处理）'] == '苏州') & (df_one['需求'] == '1000-5000人')]
df_one_7_3 = df_one[(df_one['地点（已处理）'] == '宁波') & (df_one['需求'] == '1000-5000人')]
df_one_8_3 = df_one[(df_one['地点（已处理）'] == '杭州') & (df_one['需求'] == '1000-5000人')]
df_one_9_3 = df_one[(df_one['地点（已处理）'] == '天津') & (df_one['需求'] == '1000-5000人')]
df_one_10_3 = df_one[(df_one['地点（已处理）'] == '重庆') & (df_one['需求'] == '1000-5000人')]
df_one_11_3 = df_one[(df_one['地点（已处理）'] == '青岛') & (df_one['需求'] == '1000-5000人')]
df_one_12_3 = df_one[(df_one['地点（已处理）'] == '西安') & (df_one['需求'] == '1000-5000人')]
df_one_13_3 = df_one[(df_one['地点（已处理）'] == '东莞') & (df_one['需求'] == '1000-5000人')]
df_one_14_3 = df_one[(df_one['地点（已处理）'] == '成都') & (df_one['需求'] == '1000-5000人')]
df_one_15_3 = df_one[(df_one['地点（已处理）'] == '佛山') & (df_one['需求'] == '1000-5000人')]
df_one_16_3 = df_one[(df_one['地点（已处理）'] == '南京') & (df_one['需求'] == '1000-5000人')]
df_one_17_3 = df_one[(df_one['地点（已处理）'] == '长沙') & (df_one['需求'] == '1000-5000人')]
df_one_18_3 = df_one[(df_one['地点（已处理）'] == '哈尔滨') & (df_one['需求'] == '1000-5000人')]
df_one_19_3 = df_one[(df_one['地点（已处理）'] == '武汉') & (df_one['需求'] == '1000-5000人')]
df_one_20_3 = df_one[(df_one['地点（已处理）'] == '湖北省') & (df_one['需求'] == '1000-5000人')]
df_one_21_3 = df_one[(df_one['地点（已处理）'] == '江苏省') & (df_one['需求'] == '1000-5000人')]
df_one_22_3 = df_one[(df_one['地点（已处理）'] == '广东省') & (df_one['需求'] == '1000-5000人')]
df_one_23_3 = df_one[(df_one['地点（已处理）'] == '浙江省') & (df_one['需求'] == '1000-5000人')]
df_one_24_3 = df_one[(df_one['地点（已处理）'] == '珠海') & (df_one['需求'] == '1000-5000人')]
df_one_25_3 = df_one[(df_one['地点（已处理）'] == '合肥') & (df_one['需求'] == '1000-5000人')]
df_one_26_3 = df_one[(df_one['地点（已处理）'] == '济南') & (df_one['需求'] == '1000-5000人')]
df_one_27_3 = df_one[(df_one['地点（已处理）'] == '山东省') & (df_one['需求'] == '1000-5000人')]
df_one_28_3 = df_one[(df_one['地点（已处理）'] == '郑州') & (df_one['需求'] == '1000-5000人')]
df_one_29_3 = df_one[(df_one['地点（已处理）'] == '河南省') & (df_one['需求'] == '1000-5000人')]
df_one_3 = [df_one_1_3.shape[0], df_one_2_3.shape[0],
            df_one_3_3.shape[0] + df_one_4_3.shape[0],
            df_one_5_3.shape[0], df_one_6_3.shape[0], df_one_7_3.shape[0],
            df_one_8_3.shape[0], df_one_9_3.shape[0] + df_one_10_3.shape[0],
            df_one_11_3.shape[0], df_one_12_3.shape[0], df_one_13_3.shape[0],
            df_one_14_3.shape[0], df_one_15_3.shape[0], df_one_16_3.shape[0],
            df_one_17_3.shape[0], df_one_18_3.shape[0] + df_one_19_3.shape[0],
            df_one_20_3.shape[0], df_one_21_3.shape[0],
            df_one_22_3.shape[0] + df_one_23_3.shape[0], df_one_24_3.shape[0],
            df_one_25_3.shape[0], df_one_26_3.shape[0] + df_one_27_3.shape[0],
            df_one_28_3.shape[0] + df_one_29_3.shape[0]]
df_one_1_4 = df_one[(df_one['地点（已处理）'] == '北京') & (df_one['需求'] == '500-1000人')]
df_one_2_4 = df_one[(df_one['地点（已处理）'] == '上海') & (df_one['需求'] == '500-1000人')]
df_one_3_4 = df_one[(df_one['地点（已处理）'] == '深圳') & (df_one['需求'] == '500-1000人')]
df_one_4_4 = df_one[(df_one['地点（已处理）'] == '广州') & (df_one['需求'] == '500-1000人')]
df_one_5_4 = df_one[(df_one['地点（已处理）'] == '无锡') & (df_one['需求'] == '500-1000人')]
df_one_6_4 = df_one[(df_one['地点（已处理）'] == '苏州') & (df_one['需求'] == '500-1000人')]
df_one_7_4 = df_one[(df_one['地点（已处理）'] == '宁波') & (df_one['需求'] == '500-1000人')]
df_one_8_4 = df_one[(df_one['地点（已处理）'] == '杭州') & (df_one['需求'] == '500-1000人')]
df_one_9_4 = df_one[(df_one['地点（已处理）'] == '天津') & (df_one['需求'] == '500-1000人')]
df_one_10_4 = df_one[(df_one['地点（已处理）'] == '重庆') & (df_one['需求'] == '500-1000人')]
df_one_11_4 = df_one[(df_one['地点（已处理）'] == '青岛') & (df_one['需求'] == '500-1000人')]
df_one_12_4 = df_one[(df_one['地点（已处理）'] == '西安') & (df_one['需求'] == '500-1000人')]
df_one_13_4 = df_one[(df_one['地点（已处理）'] == '东莞') & (df_one['需求'] == '500-1000人')]
df_one_14_4 = df_one[(df_one['地点（已处理）'] == '成都') & (df_one['需求'] == '500-1000人')]
df_one_15_4 = df_one[(df_one['地点（已处理）'] == '佛山') & (df_one['需求'] == '500-1000人')]
df_one_16_4 = df_one[(df_one['地点（已处理）'] == '南京') & (df_one['需求'] == '500-1000人')]
df_one_17_4 = df_one[(df_one['地点（已处理）'] == '长沙') & (df_one['需求'] == '500-1000人')]
df_one_18_4 = df_one[(df_one['地点（已处理）'] == '哈尔滨') & (df_one['需求'] == '500-1000人')]
df_one_19_4 = df_one[(df_one['地点（已处理）'] == '武汉') & (df_one['需求'] == '500-1000人')]
df_one_20_4 = df_one[(df_one['地点（已处理）'] == '湖北省') & (df_one['需求'] == '500-1000人')]
df_one_21_4 = df_one[(df_one['地点（已处理）'] == '江苏省') & (df_one['需求'] == '500-1000人')]
df_one_22_4 = df_one[(df_one['地点（已处理）'] == '广东省') & (df_one['需求'] == '500-1000人')]
df_one_23_4 = df_one[(df_one['地点（已处理）'] == '浙江省') & (df_one['需求'] == '500-1000人')]
df_one_24_4 = df_one[(df_one['地点（已处理）'] == '珠海') & (df_one['需求'] == '500-1000人')]
df_one_25_4 = df_one[(df_one['地点（已处理）'] == '合肥') & (df_one['需求'] == '500-1000人')]
df_one_26_4 = df_one[(df_one['地点（已处理）'] == '济南') & (df_one['需求'] == '500-1000人')]
df_one_27_4 = df_one[(df_one['地点（已处理）'] == '山东省') & (df_one['需求'] == '500-1000人')]
df_one_28_4 = df_one[(df_one['地点（已处理）'] == '郑州') & (df_one['需求'] == '500-1000人')]
df_one_29_4 = df_one[(df_one['地点（已处理）'] == '河南省') & (df_one['需求'] == '500-1000人')]
df_one_4 = [df_one_1_4.shape[0], df_one_2_4.shape[0],
            df_one_3_4.shape[0] + df_one_4_4.shape[0],
            df_one_5_4.shape[0], df_one_6_4.shape[0], df_one_7_4.shape[0],
            df_one_8_4.shape[0], df_one_9_4.shape[0] + df_one_10_4.shape[0],
            df_one_11_4.shape[0], df_one_12_4.shape[0], df_one_13_4.shape[0],
            df_one_14_4.shape[0], df_one_15_4.shape[0], df_one_16_4.shape[0],
            df_one_17_4.shape[0], df_one_18_4.shape[0] + df_one_19_4.shape[0],
            df_one_20_4.shape[0], df_one_21_4.shape[0],
            df_one_22_4.shape[0] + df_one_23_4.shape[0], df_one_24_4.shape[0],
            df_one_25_4.shape[0], df_one_26_4.shape[0] + df_one_27_4.shape[0],
            df_one_28_4.shape[0] + df_one_29_4.shape[0]]

df_one_1_5 = df_one[(df_one['地点（已处理）'] == '北京') & (df_one['需求'] == '150-500人')]
df_one_2_5 = df_one[(df_one['地点（已处理）'] == '上海') & (df_one['需求'] == '150-500人')]
df_one_3_5 = df_one[(df_one['地点（已处理）'] == '深圳') & (df_one['需求'] == '150-500人')]
df_one_4_5 = df_one[(df_one['地点（已处理）'] == '广州') & (df_one['需求'] == '150-500人')]
df_one_5_5 = df_one[(df_one['地点（已处理）'] == '无锡') & (df_one['需求'] == '150-500人')]
df_one_6_5 = df_one[(df_one['地点（已处理）'] == '苏州') & (df_one['需求'] == '150-500人')]
df_one_7_5 = df_one[(df_one['地点（已处理）'] == '宁波') & (df_one['需求'] == '150-500人')]
df_one_8_5 = df_one[(df_one['地点（已处理）'] == '杭州') & (df_one['需求'] == '150-500人')]
df_one_9_5 = df_one[(df_one['地点（已处理）'] == '天津') & (df_one['需求'] == '150-500人')]
df_one_10_5 = df_one[(df_one['地点（已处理）'] == '重庆') & (df_one['需求'] == '150-500人')]
df_one_11_5 = df_one[(df_one['地点（已处理）'] == '青岛') & (df_one['需求'] == '150-500人')]
df_one_12_5 = df_one[(df_one['地点（已处理）'] == '西安') & (df_one['需求'] == '150-500人')]
df_one_13_5 = df_one[(df_one['地点（已处理）'] == '东莞') & (df_one['需求'] == '150-500人')]
df_one_14_5 = df_one[(df_one['地点（已处理）'] == '成都') & (df_one['需求'] == '150-500人')]
df_one_15_5 = df_one[(df_one['地点（已处理）'] == '佛山') & (df_one['需求'] == '150-500人')]
df_one_16_5 = df_one[(df_one['地点（已处理）'] == '南京') & (df_one['需求'] == '150-500人')]
df_one_17_5 = df_one[(df_one['地点（已处理）'] == '长沙') & (df_one['需求'] == '150-500人')]
df_one_18_5 = df_one[(df_one['地点（已处理）'] == '哈尔滨') & (df_one['需求'] == '150-500人')]
df_one_19_5 = df_one[(df_one['地点（已处理）'] == '武汉') & (df_one['需求'] == '150-500人')]
df_one_20_5 = df_one[(df_one['地点（已处理）'] == '湖北省') & (df_one['需求'] == '150-500人')]
df_one_21_5 = df_one[(df_one['地点（已处理）'] == '江苏省') & (df_one['需求'] == '150-500人')]
df_one_22_5 = df_one[(df_one['地点（已处理）'] == '广东省') & (df_one['需求'] == '150-500人')]
df_one_23_5 = df_one[(df_one['地点（已处理）'] == '浙江省') & (df_one['需求'] == '150-500人')]
df_one_24_5 = df_one[(df_one['地点（已处理）'] == '珠海') & (df_one['需求'] == '150-500人')]
df_one_25_5 = df_one[(df_one['地点（已处理）'] == '合肥') & (df_one['需求'] == '150-500人')]
df_one_26_5 = df_one[(df_one['地点（已处理）'] == '济南') & (df_one['需求'] == '150-500人')]
df_one_27_5 = df_one[(df_one['地点（已处理）'] == '山东省') & (df_one['需求'] == '150-500人')]
df_one_28_5 = df_one[(df_one['地点（已处理）'] == '郑州') & (df_one['需求'] == '150-500人')]
df_one_29_5 = df_one[(df_one['地点（已处理）'] == '河南省') & (df_one['需求'] == '150-500人')]
df_one_5 = [df_one_1_5.shape[0], df_one_2_5.shape[0],
            df_one_3_5.shape[0] + df_one_4_5.shape[0],
            df_one_5_5.shape[0], df_one_6_5.shape[0], df_one_7_5.shape[0],
            df_one_8_5.shape[0], df_one_9_5.shape[0] + df_one_10_5.shape[0],
            df_one_11_5.shape[0], df_one_12_5.shape[0], df_one_13_5.shape[0],
            df_one_14_5.shape[0], df_one_15_5.shape[0], df_one_16_5.shape[0],
            df_one_17_5.shape[0], df_one_18_5.shape[0] + df_one_19_5.shape[0],
            df_one_20_5.shape[0], df_one_21_5.shape[0],
            df_one_22_5.shape[0] + df_one_23_5.shape[0], df_one_24_5.shape[0],
            df_one_25_5.shape[0], df_one_26_5.shape[0] + df_one_27_5.shape[0],
            df_one_28_5.shape[0] + df_one_29_5.shape[0]]

df_one_1_6 = df_one[(df_one['地点（已处理）'] == '北京') & (df_one['需求'] == '50-150人')]
df_one_2_6 = df_one[(df_one['地点（已处理）'] == '上海') & (df_one['需求'] == '50-150人')]
df_one_3_6 = df_one[(df_one['地点（已处理）'] == '深圳') & (df_one['需求'] == '50-150人')]
df_one_4_6 = df_one[(df_one['地点（已处理）'] == '广州') & (df_one['需求'] == '50-150人')]
df_one_5_6 = df_one[(df_one['地点（已处理）'] == '无锡') & (df_one['需求'] == '50-150人')]
df_one_6_6 = df_one[(df_one['地点（已处理）'] == '苏州') & (df_one['需求'] == '50-150人')]
df_one_7_6 = df_one[(df_one['地点（已处理）'] == '宁波') & (df_one['需求'] == '50-150人')]
df_one_8_6 = df_one[(df_one['地点（已处理）'] == '杭州') & (df_one['需求'] == '50-150人')]
df_one_9_6 = df_one[(df_one['地点（已处理）'] == '天津') & (df_one['需求'] == '50-150人')]
df_one_10_6 = df_one[(df_one['地点（已处理）'] == '重庆') & (df_one['需求'] == '50-150人')]
df_one_11_6 = df_one[(df_one['地点（已处理）'] == '青岛') & (df_one['需求'] == '50-150人')]
df_one_12_6 = df_one[(df_one['地点（已处理）'] == '西安') & (df_one['需求'] == '50-150人')]
df_one_13_6 = df_one[(df_one['地点（已处理）'] == '东莞') & (df_one['需求'] == '50-150人')]
df_one_14_6 = df_one[(df_one['地点（已处理）'] == '成都') & (df_one['需求'] == '50-150人')]
df_one_15_6 = df_one[(df_one['地点（已处理）'] == '佛山') & (df_one['需求'] == '50-150人')]
df_one_16_6 = df_one[(df_one['地点（已处理）'] == '南京') & (df_one['需求'] == '50-150人')]
df_one_17_6 = df_one[(df_one['地点（已处理）'] == '长沙') & (df_one['需求'] == '50-150人')]
df_one_18_6 = df_one[(df_one['地点（已处理）'] == '哈尔滨') & (df_one['需求'] == '50-150人')]
df_one_19_6 = df_one[(df_one['地点（已处理）'] == '武汉') & (df_one['需求'] == '50-150人')]
df_one_20_6 = df_one[(df_one['地点（已处理）'] == '湖北省') & (df_one['需求'] == '50-150人')]
df_one_21_6 = df_one[(df_one['地点（已处理）'] == '江苏省') & (df_one['需求'] == '50-150人')]
df_one_22_6 = df_one[(df_one['地点（已处理）'] == '广东省') & (df_one['需求'] == '50-150人')]
df_one_23_6 = df_one[(df_one['地点（已处理）'] == '浙江省') & (df_one['需求'] == '50-150人')]
df_one_24_6 = df_one[(df_one['地点（已处理）'] == '珠海') & (df_one['需求'] == '50-150人')]
df_one_25_6 = df_one[(df_one['地点（已处理）'] == '合肥') & (df_one['需求'] == '50-150人')]
df_one_26_6 = df_one[(df_one['地点（已处理）'] == '济南') & (df_one['需求'] == '50-150人')]
df_one_27_6 = df_one[(df_one['地点（已处理）'] == '山东省') & (df_one['需求'] == '50-150人')]
df_one_28_6 = df_one[(df_one['地点（已处理）'] == '郑州') & (df_one['需求'] == '50-150人')]
df_one_29_6 = df_one[(df_one['地点（已处理）'] == '河南省') & (df_one['需求'] == '50-150人')]
df_one_6 = [df_one_1_6.shape[0], df_one_2_6.shape[0],
            df_one_3_6.shape[0] + df_one_4_6.shape[0],
            df_one_5_6.shape[0], df_one_6_6.shape[0], df_one_7_6.shape[0],
            df_one_8_6.shape[0], df_one_9_6.shape[0] + df_one_10_6.shape[0],
            df_one_11_6.shape[0], df_one_12_6.shape[0], df_one_13_6.shape[0],
            df_one_14_6.shape[0], df_one_15_6.shape[0], df_one_16_6.shape[0],
            df_one_17_6.shape[0], df_one_18_6.shape[0] + df_one_19_6.shape[0],
            df_one_20_6.shape[0], df_one_21_6.shape[0],
            df_one_22_6.shape[0] + df_one_23_6.shape[0], df_one_24_6.shape[0],
            df_one_25_6.shape[0], df_one_26_6.shape[0] + df_one_27_6.shape[0],
            df_one_28_6.shape[0] + df_one_29_6.shape[0]]
df_one_1_7 = df_one[(df_one['地点（已处理）'] == '北京') & (df_one['需求'] == '少于50人')]
df_one_2_7 = df_one[(df_one['地点（已处理）'] == '上海') & (df_one['需求'] == '少于50人')]
df_one_3_7 = df_one[(df_one['地点（已处理）'] == '深圳') & (df_one['需求'] == '少于50人')]
df_one_4_7 = df_one[(df_one['地点（已处理）'] == '广州') & (df_one['需求'] == '少于50人')]
df_one_5_7 = df_one[(df_one['地点（已处理）'] == '无锡') & (df_one['需求'] == '少于50人')]
df_one_6_7 = df_one[(df_one['地点（已处理）'] == '苏州') & (df_one['需求'] == '少于50人')]
df_one_7_7 = df_one[(df_one['地点（已处理）'] == '宁波') & (df_one['需求'] == '少于50人')]
df_one_8_7 = df_one[(df_one['地点（已处理）'] == '杭州') & (df_one['需求'] == '少于50人')]
df_one_9_7 = df_one[(df_one['地点（已处理）'] == '天津') & (df_one['需求'] == '少于50人')]
df_one_10_7 = df_one[(df_one['地点（已处理）'] == '重庆') & (df_one['需求'] == '少于50人')]
df_one_11_7 = df_one[(df_one['地点（已处理）'] == '青岛') & (df_one['需求'] == '少于50人')]
df_one_12_7 = df_one[(df_one['地点（已处理）'] == '西安') & (df_one['需求'] == '少于50人')]
df_one_13_7 = df_one[(df_one['地点（已处理）'] == '东莞') & (df_one['需求'] == '少于50人')]
df_one_14_7 = df_one[(df_one['地点（已处理）'] == '成都') & (df_one['需求'] == '少于50人')]
df_one_15_7 = df_one[(df_one['地点（已处理）'] == '佛山') & (df_one['需求'] == '少于50人')]
df_one_16_7 = df_one[(df_one['地点（已处理）'] == '南京') & (df_one['需求'] == '少于50人')]
df_one_17_7 = df_one[(df_one['地点（已处理）'] == '长沙') & (df_one['需求'] == '少于50人')]
df_one_18_7 = df_one[(df_one['地点（已处理）'] == '哈尔滨') & (df_one['需求'] == '少于50人')]
df_one_19_7 = df_one[(df_one['地点（已处理）'] == '武汉') & (df_one['需求'] == '少于50人')]
df_one_20_7 = df_one[(df_one['地点（已处理）'] == '湖北省') & (df_one['需求'] == '少于50人')]
df_one_21_7 = df_one[(df_one['地点（已处理）'] == '江苏省') & (df_one['需求'] == '少于50人')]
df_one_22_7 = df_one[(df_one['地点（已处理）'] == '广东省') & (df_one['需求'] == '少于50人')]
df_one_23_7 = df_one[(df_one['地点（已处理）'] == '浙江省') & (df_one['需求'] == '少于50人')]
df_one_24_7 = df_one[(df_one['地点（已处理）'] == '珠海') & (df_one['需求'] == '少于50人')]
df_one_25_7 = df_one[(df_one['地点（已处理）'] == '合肥') & (df_one['需求'] == '少于50人')]
df_one_26_7 = df_one[(df_one['地点（已处理）'] == '济南') & (df_one['需求'] == '少于50人')]
df_one_27_7 = df_one[(df_one['地点（已处理）'] == '山东省') & (df_one['需求'] == '少于50人')]
df_one_28_7 = df_one[(df_one['地点（已处理）'] == '郑州') & (df_one['需求'] == '少于50人')]
df_one_29_7 = df_one[(df_one['地点（已处理）'] == '河南省') & (df_one['需求'] == '少于50人')]
df_one_7 = [df_one_1_7.shape[0], df_one_2_7.shape[0],
            df_one_3_7.shape[0] + df_one_4_7.shape[0],
            df_one_5_7.shape[0], df_one_6_7.shape[0], df_one_7_7.shape[0],
            df_one_8_7.shape[0], df_one_9_7.shape[0] + df_one_10_7.shape[0],
            df_one_11_7.shape[0], df_one_12_7.shape[0], df_one_13_7.shape[0],
            df_one_14_7.shape[0], df_one_15_7.shape[0], df_one_16_7.shape[0],
            df_one_17_7.shape[0], df_one_18_7.shape[0] + df_one_19_7.shape[0],
            df_one_20_7.shape[0], df_one_21_7.shape[0],
            df_one_22_7.shape[0] + df_one_23_7.shape[0], df_one_24_7.shape[0],
            df_one_25_7.shape[0], df_one_26_7.shape[0] + df_one_27_7.shape[0],
            df_one_28_7.shape[0] + df_one_29_7.shape[0]]

tick_label = ['北京', '上海', '深圳', '广州', '无锡', '苏州', '宁波', '杭州', '天津', '重庆', '青岛', '西安', '东莞',
              '成都', '佛山', '南京', '长沙', '哈尔滨', '武汉', '珠海', '合肥', '济南', '郑州']
data = [df_one_1, df_one_2, df_one_3, df_one_4, df_one_5, df_one_6, df_one_7]
plt.figure(dpi=433, figsize=(12, 6))
x = range(len(tick_label))
width = 0.5
bottom_y = [0] * len(tick_label)
plt.bar(x, data[0], width, bottom=bottom_y, label='10000人以上')
bottom_y = [a+b for a, b in zip(data[0], bottom_y)]
plt.bar(x, data[1], width, bottom=bottom_y, label='5000-10000人')
bottom_y = [a+b for a, b in zip(data[1], bottom_y)]
plt.bar(x, data[2], width, bottom=bottom_y, label='1000-5000人')
bottom_y = [a+b for a, b in zip(data[2], bottom_y)]
plt.bar(x, data[3], width, bottom=bottom_y, label='500-1000人')
bottom_y = [a+b for a, b in zip(data[3], bottom_y)]
plt.bar(x, data[4], width, bottom=bottom_y, label='150-500人')
bottom_y = [a+b for a, b in zip(data[4], bottom_y)]
plt.bar(x, data[5], width, bottom=bottom_y, label='50-150人')
bottom_y = [a+b for a, b in zip(data[5], bottom_y)]
plt.bar(x, data[6], width, bottom=bottom_y, label='少于50人')
plt.xticks(x, tick_label, rotation=0)
plt.title('一线城市岗位需求量图')
plt.xlabel('城市')
plt.ylabel('岗位数量')
plt.legend()
plt.savefig('fig.5 一线城市岗位需求量图.png')
plt.show()
