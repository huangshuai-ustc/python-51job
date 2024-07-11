import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_excel('result_all_normal.xlsx')
df_one = df[df['城市等级'] == '一线']
df_two = df[df['城市等级'] == '二线']
df_three = df[df['城市等级'] == '三线']
df_four = df[df['城市等级'] == '四线']
df_one_cyuyan = df_one[df_one['职位种类'] == 'c语言']
df_one_java = df_one[df_one['职位种类'] == 'java']
df_one_python = df_one[df_one['职位种类'] == 'python']
df_one_kuaiji = df_one[df_one['职位种类'] == '会计']
df_one_big_data = df_one[df_one['职位种类'] == '大数据']
df_one_kefu = df_one[df_one['职位种类'] == '客服']
df_one_teacher = df_one[df_one['职位种类'] == '教师']
df_one_data_r = df_one[df_one['职位种类'] == '数据分析']
df_one_xinmeiti = df_one[df_one['职位种类'] == '新媒体运营']
df_one_xiaoshhou = df_one[df_one['职位种类'] == '销售']
df_two_cyuyan = df_two[df_two['职位种类'] == 'c语言']
df_two_java = df_two[df_two['职位种类'] == 'java']
df_two_python = df_two[df_two['职位种类'] == 'python']
df_two_kuaiji = df_two[df_two['职位种类'] == '会计']
df_two_big_data = df_two[df_two['职位种类'] == '大数据']
df_two_kefu = df_two[df_two['职位种类'] == '客服']
df_two_teacher = df_two[df_two['职位种类'] == '教师']
df_two_data_r = df_two[df_two['职位种类'] == '数据分析']
df_two_xinmeiti = df_two[df_two['职位种类'] == '新媒体运营']
df_two_xiaoshhou = df_two[df_two['职位种类'] == '销售']
df_three_cyuyan = df_three[df_three['职位种类'] == 'c语言']
df_three_java = df_three[df_three['职位种类'] == 'java']
df_three_python = df_three[df_three['职位种类'] == 'python']
df_three_kuaiji = df_three[df_three['职位种类'] == '会计']
df_three_big_data = df_three[df_three['职位种类'] == '大数据']
df_three_kefu = df_three[df_three['职位种类'] == '客服']
df_three_teacher = df_three[df_three['职位种类'] == '教师']
df_three_data_r = df_three[df_three['职位种类'] == '数据分析']
df_three_xinmeiti = df_three[df_three['职位种类'] == '新媒体运营']
df_three_xiaoshhou = df_three[df_three['职位种类'] == '销售']
# df_four_cyuyan = df_four[df_four['职位种类'] == 'c语言']
# df_four_java = df_four[df_four['职位种类'] == 'java']
# df_four_python = df_four[df_four['职位种类'] == 'python']
# df_four_kuaiji = df_four[df_four['职位种类'] == '会计']
# df_four_big_data = df_four[df_four['职位种类'] == '大数据']
# df_four_kefu = df_four[df_four['职位种类'] == '客服']
# df_four_teacher = df_four[df_four['职位种类'] == '教师']
# df_four_data_r = df_four[df_four['职位种类'] == '数据分析']
# df_four_xinmeiti = df_four[df_four['职位种类'] == '新媒体运营']
# df_four_xiaoshhou = df_four[df_four['职位种类'] == '销售']
one = [df_one_cyuyan.shape[0], df_one_java.shape[0], df_one_python.shape[0], df_one_kuaiji.shape[0],
       df_one_big_data.shape[0], df_one_kefu.shape[0], df_one_teacher.shape[0], df_one_data_r.shape[0],
       df_one_xinmeiti.shape[0], df_one_xiaoshhou.shape[0]]
two = [df_two_cyuyan.shape[0], df_two_java.shape[0], df_two_python.shape[0], df_two_kuaiji.shape[0],
       df_two_big_data.shape[0], df_two_kefu.shape[0], df_two_teacher.shape[0], df_two_data_r.shape[0],
       df_two_xinmeiti.shape[0], df_two_xiaoshhou.shape[0]]
three = [df_three_cyuyan.shape[0], df_three_java.shape[0], df_three_python.shape[0], df_three_kuaiji.shape[0],
         df_three_big_data.shape[0], df_three_kefu.shape[0], df_three_teacher.shape[0], df_three_data_r.shape[0],
         df_three_xinmeiti.shape[0], df_three_xiaoshhou.shape[0]]
# four = [df_four_cyuyan.shape[0], df_four_java.shape[0], df_four_python.shape[0], df_four_kuaiji.shape[0],
#         df_four_big_data.shape[0], df_four_kefu.shape[0], df_four_teacher.shape[0], df_four_data_r.shape[0],
#         df_four_xinmeiti.shape[0], df_four_xiaoshhou.shape[0]]
x = ['c语言', 'java', 'python', '会计', '大数据', '客服', '教师', '数据分析', '新媒体运营', '销售']

plt.figure(dpi=433)
plt.title('职位分布图')  # 折线图标题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
plt.xlabel('职业')  # x轴标题
plt.ylabel('数量')  # y轴标题
plt.plot(x, one, marker='o', markersize=3)  # 绘制折线图，添加数据点，设置点的大小
plt.plot(x, two, marker='o', markersize=3)
plt.plot(x, three, marker='o', markersize=3)
# plt.plot(x, four, marker='o', markersize=3)
for a, b in zip(x, one):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)  # 设置数据标签位置及大小
for a, b in zip(x, two):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, three):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
# for a, b in zip(x, four):
#     plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.legend(['一线城市', '二线城市', '三线城市'])  # 设置折线名称
plt.savefig('fig.1 职位分布图.png')
plt.show()





