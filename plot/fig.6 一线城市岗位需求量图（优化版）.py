import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
df = pd.read_excel('result_all_normal.xlsx')
df_one = df[df['城市等级'] == '一线']
df_one_1_1 = df_one[(df_one['地点（已处理）'] == '北京') & (df_one['需求等级'] == '高需求')]
df_one_2_1 = df_one[(df_one['地点（已处理）'] == '上海') & (df_one['需求等级'] == '高需求')]
df_one_3_1 = df_one[(df_one['地点（已处理）'] == '深圳') & (df_one['需求等级'] == '高需求')]
df_one_4_1 = df_one[(df_one['地点（已处理）'] == '广州') & (df_one['需求等级'] == '高需求')]
df_one_5_1 = df_one[(df_one['地点（已处理）'] == '无锡') & (df_one['需求等级'] == '高需求')]
df_one_6_1 = df_one[(df_one['地点（已处理）'] == '苏州') & (df_one['需求等级'] == '高需求')]
df_one_7_1 = df_one[(df_one['地点（已处理）'] == '宁波') & (df_one['需求等级'] == '高需求')]
df_one_8_1 = df_one[(df_one['地点（已处理）'] == '杭州') & (df_one['需求等级'] == '高需求')]
df_one_9_1 = df_one[(df_one['地点（已处理）'] == '天津') & (df_one['需求等级'] == '高需求')]
df_one_10_1 = df_one[(df_one['地点（已处理）'] == '重庆') & (df_one['需求等级'] == '高需求')]
df_one_11_1 = df_one[(df_one['地点（已处理）'] == '青岛') & (df_one['需求等级'] == '高需求')]
df_one_12_1 = df_one[(df_one['地点（已处理）'] == '西安') & (df_one['需求等级'] == '高需求')]
df_one_13_1 = df_one[(df_one['地点（已处理）'] == '东莞') & (df_one['需求等级'] == '高需求')]
df_one_14_1 = df_one[(df_one['地点（已处理）'] == '成都') & (df_one['需求等级'] == '高需求')]
df_one_15_1 = df_one[(df_one['地点（已处理）'] == '佛山') & (df_one['需求等级'] == '高需求')]
df_one_16_1 = df_one[(df_one['地点（已处理）'] == '南京') & (df_one['需求等级'] == '高需求')]
df_one_17_1 = df_one[(df_one['地点（已处理）'] == '长沙') & (df_one['需求等级'] == '高需求')]
df_one_18_1 = df_one[(df_one['地点（已处理）'] == '哈尔滨') & (df_one['需求等级'] == '高需求')]
df_one_19_1 = df_one[(df_one['地点（已处理）'] == '武汉') & (df_one['需求等级'] == '高需求')]
df_one_20_1 = df_one[(df_one['地点（已处理）'] == '湖北省') & (df_one['需求等级'] == '高需求')]
df_one_21_1 = df_one[(df_one['地点（已处理）'] == '江苏省') & (df_one['需求等级'] == '高需求')]
df_one_22_1 = df_one[(df_one['地点（已处理）'] == '广东省') & (df_one['需求等级'] == '高需求')]
df_one_23_1 = df_one[(df_one['地点（已处理）'] == '浙江省') & (df_one['需求等级'] == '高需求')]
df_one_24_1 = df_one[(df_one['地点（已处理）'] == '珠海') & (df_one['需求等级'] == '高需求')]
df_one_25_1 = df_one[(df_one['地点（已处理）'] == '合肥') & (df_one['需求等级'] == '高需求')]
df_one_26_1 = df_one[(df_one['地点（已处理）'] == '济南') & (df_one['需求等级'] == '高需求')]
df_one_27_1 = df_one[(df_one['地点（已处理）'] == '山东省') & (df_one['需求等级'] == '高需求')]
df_one_28_1 = df_one[(df_one['地点（已处理）'] == '郑州') & (df_one['需求等级'] == '高需求')]
df_one_29_1 = df_one[(df_one['地点（已处理）'] == '河南省') & (df_one['需求等级'] == '高需求')]
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

df_one_1_2 = df_one[(df_one['地点（已处理）'] == '北京') & (df_one['需求等级'] == '中需求')]
df_one_2_2 = df_one[(df_one['地点（已处理）'] == '上海') & (df_one['需求等级'] == '中需求')]
df_one_3_2 = df_one[(df_one['地点（已处理）'] == '深圳') & (df_one['需求等级'] == '中需求')]
df_one_4_2 = df_one[(df_one['地点（已处理）'] == '广州') & (df_one['需求等级'] == '中需求')]
df_one_5_2 = df_one[(df_one['地点（已处理）'] == '无锡') & (df_one['需求等级'] == '中需求')]
df_one_6_2 = df_one[(df_one['地点（已处理）'] == '苏州') & (df_one['需求等级'] == '中需求')]
df_one_7_2 = df_one[(df_one['地点（已处理）'] == '宁波') & (df_one['需求等级'] == '中需求')]
df_one_8_2 = df_one[(df_one['地点（已处理）'] == '杭州') & (df_one['需求等级'] == '中需求')]
df_one_9_2 = df_one[(df_one['地点（已处理）'] == '天津') & (df_one['需求等级'] == '中需求')]
df_one_10_2 = df_one[(df_one['地点（已处理）'] == '重庆') & (df_one['需求等级'] == '中需求')]
df_one_11_2 = df_one[(df_one['地点（已处理）'] == '青岛') & (df_one['需求等级'] == '中需求')]
df_one_12_2 = df_one[(df_one['地点（已处理）'] == '西安') & (df_one['需求等级'] == '中需求')]
df_one_13_2 = df_one[(df_one['地点（已处理）'] == '东莞') & (df_one['需求等级'] == '中需求')]
df_one_14_2 = df_one[(df_one['地点（已处理）'] == '成都') & (df_one['需求等级'] == '中需求')]
df_one_15_2 = df_one[(df_one['地点（已处理）'] == '佛山') & (df_one['需求等级'] == '中需求')]
df_one_16_2 = df_one[(df_one['地点（已处理）'] == '南京') & (df_one['需求等级'] == '中需求')]
df_one_17_2 = df_one[(df_one['地点（已处理）'] == '长沙') & (df_one['需求等级'] == '中需求')]
df_one_18_2 = df_one[(df_one['地点（已处理）'] == '哈尔滨') & (df_one['需求等级'] == '中需求')]
df_one_19_2 = df_one[(df_one['地点（已处理）'] == '武汉') & (df_one['需求等级'] == '中需求')]
df_one_20_2 = df_one[(df_one['地点（已处理）'] == '湖北省') & (df_one['需求等级'] == '中需求')]
df_one_21_2 = df_one[(df_one['地点（已处理）'] == '江苏省') & (df_one['需求等级'] == '中需求')]
df_one_22_2 = df_one[(df_one['地点（已处理）'] == '广东省') & (df_one['需求等级'] == '中需求')]
df_one_23_2 = df_one[(df_one['地点（已处理）'] == '浙江省') & (df_one['需求等级'] == '中需求')]
df_one_24_2 = df_one[(df_one['地点（已处理）'] == '珠海') & (df_one['需求等级'] == '中需求')]
df_one_25_2 = df_one[(df_one['地点（已处理）'] == '合肥') & (df_one['需求等级'] == '中需求')]
df_one_26_2 = df_one[(df_one['地点（已处理）'] == '济南') & (df_one['需求等级'] == '中需求')]
df_one_27_2 = df_one[(df_one['地点（已处理）'] == '山东省') & (df_one['需求等级'] == '中需求')]
df_one_28_2 = df_one[(df_one['地点（已处理）'] == '郑州') & (df_one['需求等级'] == '中需求')]
df_one_29_2 = df_one[(df_one['地点（已处理）'] == '河南省') & (df_one['需求等级'] == '中需求')]
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

df_one_1_3 = df_one[(df_one['地点（已处理）'] == '北京') & (df_one['需求等级'] == '低需求')]
df_one_2_3 = df_one[(df_one['地点（已处理）'] == '上海') & (df_one['需求等级'] == '低需求')]
df_one_3_3 = df_one[(df_one['地点（已处理）'] == '深圳') & (df_one['需求等级'] == '低需求')]
df_one_4_3 = df_one[(df_one['地点（已处理）'] == '广州') & (df_one['需求等级'] == '低需求')]
df_one_5_3 = df_one[(df_one['地点（已处理）'] == '无锡') & (df_one['需求等级'] == '低需求')]
df_one_6_3 = df_one[(df_one['地点（已处理）'] == '苏州') & (df_one['需求等级'] == '低需求')]
df_one_7_3 = df_one[(df_one['地点（已处理）'] == '宁波') & (df_one['需求等级'] == '低需求')]
df_one_8_3 = df_one[(df_one['地点（已处理）'] == '杭州') & (df_one['需求等级'] == '低需求')]
df_one_9_3 = df_one[(df_one['地点（已处理）'] == '天津') & (df_one['需求等级'] == '低需求')]
df_one_10_3 = df_one[(df_one['地点（已处理）'] == '重庆') & (df_one['需求等级'] == '低需求')]
df_one_11_3 = df_one[(df_one['地点（已处理）'] == '青岛') & (df_one['需求等级'] == '低需求')]
df_one_12_3 = df_one[(df_one['地点（已处理）'] == '西安') & (df_one['需求等级'] == '低需求')]
df_one_13_3 = df_one[(df_one['地点（已处理）'] == '东莞') & (df_one['需求等级'] == '低需求')]
df_one_14_3 = df_one[(df_one['地点（已处理）'] == '成都') & (df_one['需求等级'] == '低需求')]
df_one_15_3 = df_one[(df_one['地点（已处理）'] == '佛山') & (df_one['需求等级'] == '低需求')]
df_one_16_3 = df_one[(df_one['地点（已处理）'] == '南京') & (df_one['需求等级'] == '低需求')]
df_one_17_3 = df_one[(df_one['地点（已处理）'] == '长沙') & (df_one['需求等级'] == '低需求')]
df_one_18_3 = df_one[(df_one['地点（已处理）'] == '哈尔滨') & (df_one['需求等级'] == '低需求')]
df_one_19_3 = df_one[(df_one['地点（已处理）'] == '武汉') & (df_one['需求等级'] == '低需求')]
df_one_20_3 = df_one[(df_one['地点（已处理）'] == '湖北省') & (df_one['需求等级'] == '低需求')]
df_one_21_3 = df_one[(df_one['地点（已处理）'] == '江苏省') & (df_one['需求等级'] == '低需求')]
df_one_22_3 = df_one[(df_one['地点（已处理）'] == '广东省') & (df_one['需求等级'] == '低需求')]
df_one_23_3 = df_one[(df_one['地点（已处理）'] == '浙江省') & (df_one['需求等级'] == '低需求')]
df_one_24_3 = df_one[(df_one['地点（已处理）'] == '珠海') & (df_one['需求等级'] == '低需求')]
df_one_25_3 = df_one[(df_one['地点（已处理）'] == '合肥') & (df_one['需求等级'] == '低需求')]
df_one_26_3 = df_one[(df_one['地点（已处理）'] == '济南') & (df_one['需求等级'] == '低需求')]
df_one_27_3 = df_one[(df_one['地点（已处理）'] == '山东省') & (df_one['需求等级'] == '低需求')]
df_one_28_3 = df_one[(df_one['地点（已处理）'] == '郑州') & (df_one['需求等级'] == '低需求')]
df_one_29_3 = df_one[(df_one['地点（已处理）'] == '河南省') & (df_one['需求等级'] == '低需求')]
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

tick_label = ['北京', '上海', '深圳', '广州', '无锡', '苏州', '宁波', '杭州', '天津', '重庆', '青岛', '西安', '东莞',
              '成都', '佛山', '南京', '长沙', '哈尔滨', '武汉', '珠海', '合肥', '济南', '郑州']
data = [df_one_1, df_one_2, df_one_3]
bar_width = 0.3
x = np.arange(len(tick_label))
plt.figure(dpi=433, figsize=(12, 6))
plt.title('一线城市岗位需求量图')
plt.bar(x, df_one_1, bar_width, align='center', label='高需求')
plt.bar(x + bar_width, df_one_2, bar_width, align='center', label='中需求')
plt.bar(x + 2 * bar_width, df_one_3, bar_width, align='center', label='低需求')
plt.xlabel('城市')
plt.ylabel('数量')
plt.xticks(x + bar_width / 3, tick_label)
plt.legend()
plt.savefig('fig.6 一线城市岗位需求量图（优化版）.png')
plt.show()
