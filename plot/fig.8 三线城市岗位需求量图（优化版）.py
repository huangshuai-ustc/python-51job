import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
df = pd.read_excel('result_all_normal.xlsx')
df_three = df[df['城市等级'] == '三线']
df_three_1_low = df_three[(df_three['地点（已处理）'] == '长春') & (df_three['需求等级'] == '低需求')]
df_three_2_low = df_three[(df_three['地点（已处理）'] == '昆山') & (df_three['需求等级'] == '低需求')]
df_three_3_low = df_three[(df_three['地点（已处理）'] == '温州') & (df_three['需求等级'] == '低需求')]
df_three_4_low = df_three[(df_three['地点（已处理）'] == '潍坊') & (df_three['需求等级'] == '低需求')]
df_three_5_low = df_three[(df_three['地点（已处理）'] == '滁州') & (df_three['需求等级'] == '低需求')]
df_three_6_low = df_three[(df_three['地点（已处理）'] == '保定') & (df_three['需求等级'] == '低需求')]
df_three_7_low = df_three[(df_three['地点（已处理）'] == '张家港') & (df_three['需求等级'] == '低需求')]
df_three_8_low = df_three[(df_three['地点（已处理）'] == '常熟') & (df_three['需求等级'] == '低需求')]
df_three_9_low = df_three[(df_three['地点（已处理）'] == '潮州') & (df_three['需求等级'] == '低需求')]
df_three_10_low = df_three[(df_three['地点（已处理）'] == '金华') & (df_three['需求等级'] == '低需求')]
df_three_11_low = df_three[(df_three['地点（已处理）'] == '江门') & (df_three['需求等级'] == '低需求')]
df_three_12_low = df_three[(df_three['地点（已处理）'] == '扬州') & (df_three['需求等级'] == '低需求')]
df_three_13_low = df_three[(df_three['地点（已处理）'] == '镇江') & (df_three['需求等级'] == '低需求')]
df_three_14_low = df_three[(df_three['地点（已处理）'] == '三亚') & (df_three['需求等级'] == '低需求')]
df_three_15_low = df_three[(df_three['地点（已处理）'] == '秦皇岛') & (df_three['需求等级'] == '低需求')]
df_three_16_low = df_three[(df_three['地点（已处理）'] == '株洲') & (df_three['需求等级'] == '低需求')]
df_three_17_low = df_three[(df_three['地点（已处理）'] == '新乡') & (df_three['需求等级'] == '低需求')]
df_three_18_low = df_three[(df_three['地点（已处理）'] == '淮安') & (df_three['需求等级'] == '低需求')]
df_three_19_low = df_three[(df_three['地点（已处理）'] == '呼和浩特') & (df_three['需求等级'] == '低需求')]
df_three_20_low = df_three[(df_three['地点（已处理）'] == '荆州') & (df_three['需求等级'] == '低需求')]
df_three_21_low = df_three[(df_three['地点（已处理）'] == '银川') & (df_three['需求等级'] == '低需求')]
df_three_22_low = df_three[(df_three['地点（已处理）'] == '邯郸') & (df_three['需求等级'] == '低需求')]
df_three_23_low = df_three[(df_three['地点（已处理）'] == '连云港') & (df_three['需求等级'] == '低需求')]
df_three_24_low = df_three[(df_three['地点（已处理）'] == '咸阳') & (df_three['需求等级'] == '低需求')]
df_three_25_low = df_three[(df_three['地点（已处理）'] == '绵阳') & (df_three['需求等级'] == '低需求')]
df_three_26_low = df_three[(df_three['地点（已处理）'] == '赣州') & (df_three['需求等级'] == '低需求')]
df_three_27_low = df_three[(df_three['地点（已处理）'] == '包头') & (df_three['需求等级'] == '低需求')]
df_three_28_low = df_three[(df_three['地点（已处理）'] == '汕头') & (df_three['需求等级'] == '低需求')]
df_three_29_low = df_three[(df_three['地点（已处理）'] == '常德') & (df_three['需求等级'] == '低需求')]
df_three_30_low = df_three[(df_three['地点（已处理）'] == '九江') & (df_three['需求等级'] == '低需求')]
df_three_31_low = df_three[(df_three['地点（已处理）'] == '宜春') & (df_three['需求等级'] == '低需求')]
df_three_32_low = df_three[(df_three['地点（已处理）'] == '清远') & (df_three['需求等级'] == '低需求')]
df_three_33_low = df_three[(df_three['地点（已处理）'] == '上饶') & (df_three['需求等级'] == '低需求')]
df_three_34_low = df_three[(df_three['地点（已处理）'] == '唐山') & (df_three['需求等级'] == '低需求')]
df_three_35_low = df_three[(df_three['地点（已处理）'] == '沧州') & (df_three['需求等级'] == '低需求')]
df_three_36_low = df_three[(df_three['地点（已处理）'] == '南充') & (df_three['需求等级'] == '低需求')]
df_three_37_low = df_three[(df_three['地点（已处理）'] == '赤峰') & (df_three['需求等级'] == '低需求')]
df_three_38_low = df_three[(df_three['地点（已处理）'] == '岳阳') & (df_three['需求等级'] == '低需求')]
df_three_39_low = df_three[(df_three['地点（已处理）'] == '肇庆') & (df_three['需求等级'] == '低需求')]
df_three_40_low = df_three[(df_three['地点（已处理）'] == '六安') & (df_three['需求等级'] == '低需求')]
df_three_41_low = df_three[(df_three['地点（已处理）'] == '漳州') & (df_three['需求等级'] == '低需求')]
df_three_42_low = df_three[(df_three['地点（已处理）'] == '鞍山') & (df_three['需求等级'] == '低需求')]
df_three_43_low = df_three[(df_three['地点（已处理）'] == '阜阳') & (df_three['需求等级'] == '低需求')]
df_three_44_low = df_three[(df_three['地点（已处理）'] == '淄博') & (df_three['需求等级'] == '低需求')]
df_three_45_low = df_three[(df_three['地点（已处理）'] == '菏泽') & (df_three['需求等级'] == '低需求')]
df_three_46_low = df_three[(df_three['地点（已处理）'] == '临沂') & (df_three['需求等级'] == '低需求')]
df_three_47_low = df_three[(df_three['地点（已处理）'] == '安庆') & (df_three['需求等级'] == '低需求')]
df_three_48_low = df_three[(df_three['地点（已处理）'] == '驻马店') & (df_three['需求等级'] == '低需求')]
df_three_49_low = df_three[(df_three['地点（已处理）'] == '宜宾') & (df_three['需求等级'] == '低需求')]
df_three_50_low = df_three[(df_three['地点（已处理）'] == '南平') & (df_three['需求等级'] == '低需求')]
df_three_51_low = df_three[(df_three['地点（已处理）'] == '衡阳') & (df_three['需求等级'] == '低需求')]
df_three_52_low = df_three[(df_three['地点（已处理）'] == '洛阳') & (df_three['需求等级'] == '低需求')]
df_three_53_low = df_three[(df_three['地点（已处理）'] == '宿迁') & (df_three['需求等级'] == '低需求')]
df_three_54_low = df_three[(df_three['地点（已处理）'] == '威海') & (df_three['需求等级'] == '低需求')]
df_three_55_low = df_three[(df_three['地点（已处理）'] == '宿州') & (df_three['需求等级'] == '低需求')]
df_three_low = [df_three_1_low.shape[0], df_three_2_low.shape[0], df_three_3_low.shape[0],
                df_three_4_low.shape[0], df_three_5_low.shape[0], df_three_6_low.shape[0],
                df_three_7_low.shape[0], df_three_8_low.shape[0], df_three_9_low.shape[0],
                df_three_10_low.shape[0], df_three_11_low.shape[0], df_three_12_low.shape[0],
                df_three_13_low.shape[0], df_three_14_low.shape[0], df_three_15_low.shape[0],
                df_three_16_low.shape[0], df_three_17_low.shape[0], df_three_18_low.shape[0],
                df_three_19_low.shape[0], df_three_20_low.shape[0], df_three_21_low.shape[0],
                df_three_22_low.shape[0], df_three_23_low.shape[0], df_three_24_low.shape[0],
                df_three_25_low.shape[0], df_three_26_low.shape[0], df_three_27_low.shape[0],
                df_three_28_low.shape[0], df_three_29_low.shape[0], df_three_30_low.shape[0],
                df_three_31_low.shape[0], df_three_32_low.shape[0], df_three_33_low.shape[0],
                df_three_34_low.shape[0], df_three_35_low.shape[0], df_three_36_low.shape[0],
                df_three_37_low.shape[0], df_three_38_low.shape[0], df_three_39_low.shape[0],
                df_three_40_low.shape[0], df_three_41_low.shape[0], df_three_42_low.shape[0],
                df_three_43_low.shape[0], df_three_44_low.shape[0], df_three_45_low.shape[0],
                df_three_46_low.shape[0], df_three_47_low.shape[0], df_three_48_low.shape[0],
                df_three_49_low.shape[0], df_three_50_low.shape[0], df_three_51_low.shape[0],
                df_three_52_low.shape[0], df_three_53_low.shape[0], df_three_54_low.shape[0],
                df_three_55_low.shape[0]]
df_three_1_mid = df_three[(df_three['地点（已处理）'] == '长春') & (df_three['需求等级'] == '中需求')]
df_three_2_mid = df_three[(df_three['地点（已处理）'] == '昆山') & (df_three['需求等级'] == '中需求')]
df_three_3_mid = df_three[(df_three['地点（已处理）'] == '温州') & (df_three['需求等级'] == '中需求')]
df_three_4_mid = df_three[(df_three['地点（已处理）'] == '潍坊') & (df_three['需求等级'] == '中需求')]
df_three_5_mid = df_three[(df_three['地点（已处理）'] == '滁州') & (df_three['需求等级'] == '中需求')]
df_three_6_mid = df_three[(df_three['地点（已处理）'] == '保定') & (df_three['需求等级'] == '中需求')]
df_three_7_mid = df_three[(df_three['地点（已处理）'] == '张家港') & (df_three['需求等级'] == '中需求')]
df_three_8_mid = df_three[(df_three['地点（已处理）'] == '常熟') & (df_three['需求等级'] == '中需求')]
df_three_9_mid = df_three[(df_three['地点（已处理）'] == '潮州') & (df_three['需求等级'] == '中需求')]
df_three_10_mid = df_three[(df_three['地点（已处理）'] == '金华') & (df_three['需求等级'] == '中需求')]
df_three_11_mid = df_three[(df_three['地点（已处理）'] == '江门') & (df_three['需求等级'] == '中需求')]
df_three_12_mid = df_three[(df_three['地点（已处理）'] == '扬州') & (df_three['需求等级'] == '中需求')]
df_three_13_mid = df_three[(df_three['地点（已处理）'] == '镇江') & (df_three['需求等级'] == '中需求')]
df_three_14_mid = df_three[(df_three['地点（已处理）'] == '三亚') & (df_three['需求等级'] == '中需求')]
df_three_15_mid = df_three[(df_three['地点（已处理）'] == '秦皇岛') & (df_three['需求等级'] == '中需求')]
df_three_16_mid = df_three[(df_three['地点（已处理）'] == '株洲') & (df_three['需求等级'] == '中需求')]
df_three_17_mid = df_three[(df_three['地点（已处理）'] == '新乡') & (df_three['需求等级'] == '中需求')]
df_three_18_mid = df_three[(df_three['地点（已处理）'] == '淮安') & (df_three['需求等级'] == '中需求')]
df_three_19_mid = df_three[(df_three['地点（已处理）'] == '呼和浩特') & (df_three['需求等级'] == '中需求')]
df_three_20_mid = df_three[(df_three['地点（已处理）'] == '荆州') & (df_three['需求等级'] == '中需求')]
df_three_21_mid = df_three[(df_three['地点（已处理）'] == '银川') & (df_three['需求等级'] == '中需求')]
df_three_22_mid = df_three[(df_three['地点（已处理）'] == '邯郸') & (df_three['需求等级'] == '中需求')]
df_three_23_mid = df_three[(df_three['地点（已处理）'] == '连云港') & (df_three['需求等级'] == '中需求')]
df_three_24_mid = df_three[(df_three['地点（已处理）'] == '咸阳') & (df_three['需求等级'] == '中需求')]
df_three_25_mid = df_three[(df_three['地点（已处理）'] == '绵阳') & (df_three['需求等级'] == '中需求')]
df_three_26_mid = df_three[(df_three['地点（已处理）'] == '赣州') & (df_three['需求等级'] == '中需求')]
df_three_27_mid = df_three[(df_three['地点（已处理）'] == '包头') & (df_three['需求等级'] == '中需求')]
df_three_28_mid = df_three[(df_three['地点（已处理）'] == '汕头') & (df_three['需求等级'] == '中需求')]
df_three_29_mid = df_three[(df_three['地点（已处理）'] == '常德') & (df_three['需求等级'] == '中需求')]
df_three_30_mid = df_three[(df_three['地点（已处理）'] == '九江') & (df_three['需求等级'] == '中需求')]
df_three_31_mid = df_three[(df_three['地点（已处理）'] == '宜春') & (df_three['需求等级'] == '中需求')]
df_three_32_mid = df_three[(df_three['地点（已处理）'] == '清远') & (df_three['需求等级'] == '中需求')]
df_three_33_mid = df_three[(df_three['地点（已处理）'] == '上饶') & (df_three['需求等级'] == '中需求')]
df_three_34_mid = df_three[(df_three['地点（已处理）'] == '唐山') & (df_three['需求等级'] == '中需求')]
df_three_35_mid = df_three[(df_three['地点（已处理）'] == '沧州') & (df_three['需求等级'] == '中需求')]
df_three_36_mid = df_three[(df_three['地点（已处理）'] == '南充') & (df_three['需求等级'] == '中需求')]
df_three_37_mid = df_three[(df_three['地点（已处理）'] == '赤峰') & (df_three['需求等级'] == '中需求')]
df_three_38_mid = df_three[(df_three['地点（已处理）'] == '岳阳') & (df_three['需求等级'] == '中需求')]
df_three_39_mid = df_three[(df_three['地点（已处理）'] == '肇庆') & (df_three['需求等级'] == '中需求')]
df_three_40_mid = df_three[(df_three['地点（已处理）'] == '六安') & (df_three['需求等级'] == '中需求')]
df_three_41_mid = df_three[(df_three['地点（已处理）'] == '漳州') & (df_three['需求等级'] == '中需求')]
df_three_42_mid = df_three[(df_three['地点（已处理）'] == '鞍山') & (df_three['需求等级'] == '中需求')]
df_three_43_mid = df_three[(df_three['地点（已处理）'] == '阜阳') & (df_three['需求等级'] == '中需求')]
df_three_44_mid = df_three[(df_three['地点（已处理）'] == '淄博') & (df_three['需求等级'] == '中需求')]
df_three_45_mid = df_three[(df_three['地点（已处理）'] == '菏泽') & (df_three['需求等级'] == '中需求')]
df_three_46_mid = df_three[(df_three['地点（已处理）'] == '临沂') & (df_three['需求等级'] == '中需求')]
df_three_47_mid = df_three[(df_three['地点（已处理）'] == '安庆') & (df_three['需求等级'] == '中需求')]
df_three_48_mid = df_three[(df_three['地点（已处理）'] == '驻马店') & (df_three['需求等级'] == '中需求')]
df_three_49_mid = df_three[(df_three['地点（已处理）'] == '宜宾') & (df_three['需求等级'] == '中需求')]
df_three_50_mid = df_three[(df_three['地点（已处理）'] == '南平') & (df_three['需求等级'] == '中需求')]
df_three_51_mid = df_three[(df_three['地点（已处理）'] == '衡阳') & (df_three['需求等级'] == '中需求')]
df_three_52_mid = df_three[(df_three['地点（已处理）'] == '洛阳') & (df_three['需求等级'] == '中需求')]
df_three_53_mid = df_three[(df_three['地点（已处理）'] == '宿迁') & (df_three['需求等级'] == '中需求')]
df_three_54_mid = df_three[(df_three['地点（已处理）'] == '威海') & (df_three['需求等级'] == '中需求')]
df_three_55_mid = df_three[(df_three['地点（已处理）'] == '宿州') & (df_three['需求等级'] == '中需求')]
df_three_mid = [df_three_1_mid.shape[0], df_three_2_mid.shape[0], df_three_3_mid.shape[0],
                df_three_4_mid.shape[0], df_three_5_mid.shape[0], df_three_6_mid.shape[0],
                df_three_7_mid.shape[0], df_three_8_mid.shape[0], df_three_9_mid.shape[0],
                df_three_10_mid.shape[0], df_three_11_mid.shape[0], df_three_12_mid.shape[0],
                df_three_13_mid.shape[0], df_three_14_mid.shape[0], df_three_15_mid.shape[0],
                df_three_16_mid.shape[0], df_three_17_mid.shape[0], df_three_18_mid.shape[0],
                df_three_19_mid.shape[0], df_three_20_mid.shape[0], df_three_21_mid.shape[0],
                df_three_22_mid.shape[0], df_three_23_mid.shape[0], df_three_24_mid.shape[0],
                df_three_25_mid.shape[0], df_three_26_mid.shape[0], df_three_27_mid.shape[0],
                df_three_28_mid.shape[0], df_three_29_mid.shape[0], df_three_30_mid.shape[0],
                df_three_31_mid.shape[0], df_three_32_mid.shape[0], df_three_33_mid.shape[0],
                df_three_34_mid.shape[0], df_three_35_mid.shape[0], df_three_36_mid.shape[0],
                df_three_37_mid.shape[0], df_three_38_mid.shape[0], df_three_39_mid.shape[0],
                df_three_40_mid.shape[0], df_three_41_mid.shape[0], df_three_42_mid.shape[0],
                df_three_43_mid.shape[0], df_three_44_mid.shape[0], df_three_45_mid.shape[0],
                df_three_46_mid.shape[0], df_three_47_mid.shape[0], df_three_48_mid.shape[0],
                df_three_49_mid.shape[0], df_three_50_mid.shape[0], df_three_51_mid.shape[0],
                df_three_52_mid.shape[0], df_three_53_mid.shape[0], df_three_54_mid.shape[0],
                df_three_55_mid.shape[0]]
df_three_1_hig = df_three[(df_three['地点（已处理）'] == '长春') & (df_three['需求等级'] == '高需求')]
df_three_2_hig = df_three[(df_three['地点（已处理）'] == '昆山') & (df_three['需求等级'] == '高需求')]
df_three_3_hig = df_three[(df_three['地点（已处理）'] == '温州') & (df_three['需求等级'] == '高需求')]
df_three_4_hig = df_three[(df_three['地点（已处理）'] == '潍坊') & (df_three['需求等级'] == '高需求')]
df_three_5_hig = df_three[(df_three['地点（已处理）'] == '滁州') & (df_three['需求等级'] == '高需求')]
df_three_6_hig = df_three[(df_three['地点（已处理）'] == '保定') & (df_three['需求等级'] == '高需求')]
df_three_7_hig = df_three[(df_three['地点（已处理）'] == '张家港') & (df_three['需求等级'] == '高需求')]
df_three_8_hig = df_three[(df_three['地点（已处理）'] == '常熟') & (df_three['需求等级'] == '高需求')]
df_three_9_hig = df_three[(df_three['地点（已处理）'] == '潮州') & (df_three['需求等级'] == '高需求')]
df_three_10_hig = df_three[(df_three['地点（已处理）'] == '金华') & (df_three['需求等级'] == '高需求')]
df_three_11_hig = df_three[(df_three['地点（已处理）'] == '江门') & (df_three['需求等级'] == '高需求')]
df_three_12_hig = df_three[(df_three['地点（已处理）'] == '扬州') & (df_three['需求等级'] == '高需求')]
df_three_13_hig = df_three[(df_three['地点（已处理）'] == '镇江') & (df_three['需求等级'] == '高需求')]
df_three_14_hig = df_three[(df_three['地点（已处理）'] == '三亚') & (df_three['需求等级'] == '高需求')]
df_three_15_hig = df_three[(df_three['地点（已处理）'] == '秦皇岛') & (df_three['需求等级'] == '高需求')]
df_three_16_hig = df_three[(df_three['地点（已处理）'] == '株洲') & (df_three['需求等级'] == '高需求')]
df_three_17_hig = df_three[(df_three['地点（已处理）'] == '新乡') & (df_three['需求等级'] == '高需求')]
df_three_18_hig = df_three[(df_three['地点（已处理）'] == '淮安') & (df_three['需求等级'] == '高需求')]
df_three_19_hig = df_three[(df_three['地点（已处理）'] == '呼和浩特') & (df_three['需求等级'] == '高需求')]
df_three_20_hig = df_three[(df_three['地点（已处理）'] == '荆州') & (df_three['需求等级'] == '高需求')]
df_three_21_hig = df_three[(df_three['地点（已处理）'] == '银川') & (df_three['需求等级'] == '高需求')]
df_three_22_hig = df_three[(df_three['地点（已处理）'] == '邯郸') & (df_three['需求等级'] == '高需求')]
df_three_23_hig = df_three[(df_three['地点（已处理）'] == '连云港') & (df_three['需求等级'] == '高需求')]
df_three_24_hig = df_three[(df_three['地点（已处理）'] == '咸阳') & (df_three['需求等级'] == '高需求')]
df_three_25_hig = df_three[(df_three['地点（已处理）'] == '绵阳') & (df_three['需求等级'] == '高需求')]
df_three_26_hig = df_three[(df_three['地点（已处理）'] == '赣州') & (df_three['需求等级'] == '高需求')]
df_three_27_hig = df_three[(df_three['地点（已处理）'] == '包头') & (df_three['需求等级'] == '高需求')]
df_three_28_hig = df_three[(df_three['地点（已处理）'] == '汕头') & (df_three['需求等级'] == '高需求')]
df_three_29_hig = df_three[(df_three['地点（已处理）'] == '常德') & (df_three['需求等级'] == '高需求')]
df_three_30_hig = df_three[(df_three['地点（已处理）'] == '九江') & (df_three['需求等级'] == '高需求')]
df_three_31_hig = df_three[(df_three['地点（已处理）'] == '宜春') & (df_three['需求等级'] == '高需求')]
df_three_32_hig = df_three[(df_three['地点（已处理）'] == '清远') & (df_three['需求等级'] == '高需求')]
df_three_33_hig = df_three[(df_three['地点（已处理）'] == '上饶') & (df_three['需求等级'] == '高需求')]
df_three_34_hig = df_three[(df_three['地点（已处理）'] == '唐山') & (df_three['需求等级'] == '高需求')]
df_three_35_hig = df_three[(df_three['地点（已处理）'] == '沧州') & (df_three['需求等级'] == '高需求')]
df_three_36_hig = df_three[(df_three['地点（已处理）'] == '南充') & (df_three['需求等级'] == '高需求')]
df_three_37_hig = df_three[(df_three['地点（已处理）'] == '赤峰') & (df_three['需求等级'] == '高需求')]
df_three_38_hig = df_three[(df_three['地点（已处理）'] == '岳阳') & (df_three['需求等级'] == '高需求')]
df_three_39_hig = df_three[(df_three['地点（已处理）'] == '肇庆') & (df_three['需求等级'] == '高需求')]
df_three_40_hig = df_three[(df_three['地点（已处理）'] == '六安') & (df_three['需求等级'] == '高需求')]
df_three_41_hig = df_three[(df_three['地点（已处理）'] == '漳州') & (df_three['需求等级'] == '高需求')]
df_three_42_hig = df_three[(df_three['地点（已处理）'] == '鞍山') & (df_three['需求等级'] == '高需求')]
df_three_43_hig = df_three[(df_three['地点（已处理）'] == '阜阳') & (df_three['需求等级'] == '高需求')]
df_three_44_hig = df_three[(df_three['地点（已处理）'] == '淄博') & (df_three['需求等级'] == '高需求')]
df_three_45_hig = df_three[(df_three['地点（已处理）'] == '菏泽') & (df_three['需求等级'] == '高需求')]
df_three_46_hig = df_three[(df_three['地点（已处理）'] == '临沂') & (df_three['需求等级'] == '高需求')]
df_three_47_hig = df_three[(df_three['地点（已处理）'] == '安庆') & (df_three['需求等级'] == '高需求')]
df_three_48_hig = df_three[(df_three['地点（已处理）'] == '驻马店') & (df_three['需求等级'] == '高需求')]
df_three_49_hig = df_three[(df_three['地点（已处理）'] == '宜宾') & (df_three['需求等级'] == '高需求')]
df_three_50_hig = df_three[(df_three['地点（已处理）'] == '南平') & (df_three['需求等级'] == '高需求')]
df_three_51_hig = df_three[(df_three['地点（已处理）'] == '衡阳') & (df_three['需求等级'] == '高需求')]
df_three_52_hig = df_three[(df_three['地点（已处理）'] == '洛阳') & (df_three['需求等级'] == '高需求')]
df_three_53_hig = df_three[(df_three['地点（已处理）'] == '宿迁') & (df_three['需求等级'] == '高需求')]
df_three_54_hig = df_three[(df_three['地点（已处理）'] == '威海') & (df_three['需求等级'] == '高需求')]
df_three_55_hig = df_three[(df_three['地点（已处理）'] == '宿州') & (df_three['需求等级'] == '高需求')]
df_three_hig = [df_three_1_hig.shape[0], df_three_2_hig.shape[0], df_three_3_hig.shape[0],
                df_three_4_hig.shape[0], df_three_5_hig.shape[0], df_three_6_hig.shape[0],
                df_three_7_hig.shape[0], df_three_8_hig.shape[0], df_three_9_hig.shape[0],
                df_three_10_hig.shape[0], df_three_11_hig.shape[0], df_three_12_hig.shape[0],
                df_three_13_hig.shape[0], df_three_14_hig.shape[0], df_three_15_hig.shape[0],
                df_three_16_hig.shape[0], df_three_17_hig.shape[0], df_three_18_hig.shape[0],
                df_three_19_hig.shape[0], df_three_20_hig.shape[0], df_three_21_hig.shape[0],
                df_three_22_hig.shape[0], df_three_23_hig.shape[0], df_three_24_hig.shape[0],
                df_three_25_hig.shape[0], df_three_26_hig.shape[0], df_three_27_hig.shape[0],
                df_three_28_hig.shape[0], df_three_29_hig.shape[0], df_three_30_hig.shape[0],
                df_three_31_hig.shape[0], df_three_32_hig.shape[0], df_three_33_hig.shape[0],
                df_three_34_hig.shape[0], df_three_35_hig.shape[0], df_three_36_hig.shape[0],
                df_three_37_hig.shape[0], df_three_38_hig.shape[0], df_three_39_hig.shape[0],
                df_three_40_hig.shape[0], df_three_41_hig.shape[0], df_three_42_hig.shape[0],
                df_three_43_hig.shape[0], df_three_44_hig.shape[0], df_three_45_hig.shape[0],
                df_three_46_hig.shape[0], df_three_47_hig.shape[0], df_three_48_hig.shape[0],
                df_three_49_hig.shape[0], df_three_50_hig.shape[0], df_three_51_hig.shape[0],
                df_three_52_hig.shape[0], df_three_53_hig.shape[0], df_three_54_hig.shape[0],
                df_three_55_hig.shape[0]]

#
tick_label = ['长\n春', '昆\n山', '温\n州', '潍\n坊', '滁\n州', '保\n定', '张\n家\n港', '常\n熟', '潮\n州', '金\n华', '江\n门',
              '扬\n州', '镇\n江', '三\n亚',
              '秦\n皇\n岛', '株\n洲', '新\n乡', '淮\n安', '呼\n和\n浩\n特', '荆\n州', '银\n川', '邯\n郸', '连\n云\n港', '咸\n阳',
              '绵\n阳', '赣\n州', '包\n头', '汕\n头',
              '常\n德', '九\n江', '宜\n春', '清\n远', '上\n饶', '唐\n山', '沧\n州', '南\n充', '赤\n峰', '岳\n阳', '肇\n庆',
              '六\n安', '漳\n州', '鞍\n山',
              '阜\n阳', '淄\n博', '菏\n泽', '临\n沂', '安\n庆', '驻\n马\n店', '宜\n宾', '南\n平', '衡\n阳', '洛\n阳', '宿\n迁',
              '威\n海', '宿\n州']
bar_width = 0.2
data = [df_three_low, df_three_mid, df_three_hig]
plt.figure(dpi=433, figsize=(12, 6))
x = range(len(tick_label))
width = 0.5
bottom_y = [0] * len(tick_label)
plt.bar(x, data[0], width, bottom=bottom_y, label='低需求')
bottom_y = [a+b for a, b in zip(data[0], bottom_y)]
plt.bar(x, data[1], width, bottom=bottom_y, label='中需求')
bottom_y = [a+b for a, b in zip(data[1], bottom_y)]
plt.bar(x, data[2], width, bottom=bottom_y, label='高需求')
plt.xticks(x, tick_label, rotation=0)
plt.title('三线城市岗位需求量图')
plt.xlabel('城市')
plt.ylabel('数量')
plt.legend()
plt.savefig('fig.8 三线城市岗位需求量图（优化版）.png')
plt.show()
