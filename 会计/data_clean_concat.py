import os
import pandas as pd
from collections import Counter

files = os.listdir('./')
data = pd.DataFrame()
d = {'营口': '四线', '潮州': '三线', '咸阳': '三线', '自贡': '四线', '湘潭': '四线', '钦州': '四线', '北海': '四线',
     '鄂尔多斯': '四线', '南充': '三线', '抚顺': '四线', '抚州': '四线', '赣州': '三线', '威海': '三线', '运城': '四线',
     '鞍山': '三线', '长沙': '一线', '开平': '四线', '和田': '四线', '九江': '三线', '大同': '四线', '泰州': '四线',
     '潜江': '四线', '丽水': '四线', '雅安': '四线', '河源': '四线', '义乌': '四线', '温州': '三线', '通辽': '四线',
     '海口': '二线', '珠海': '一线', '潍坊': '三线', '德阳': '四线', '成都': '一线', '襄阳': '四线', '桂林': '二线',
     '邢台': '四线', '丹东': '四线', '遂宁': '四线', '无': '无', '广东省': '一线', '河南省': '一线', '文山': '四线',
     '宜昌': '二线', '贵港': '四线', '哈尔滨': '一线', '佛山': '一线', '海东': '四线', '湖州': '四线', '金华': '三线',
     '宣城': '四线', '衢州': '四线', '喀什地区': '四线', '焦作': '四线', '东莞': '一线', '保定': '三线', '湛江': '四线',
     '济宁': '四线', '达州': '四线', '甘孜': '四线', '苏州': '一线', '枣庄': '四线', '浙江省': '一线', '巴中': '四线',
     '广州': '一线', '大连': '二线', '西安': '一线', '舟山': '四线', '太仓': '四线', '澄迈': '四线', '玉林': '四线',
     '韶关': '四线', '辽阳': '四线', '信阳': '四线', '景德镇': '四线', '邵阳': '四线', '昆明': '二线', '芜湖': '二线',
     '齐齐哈尔': '四线', '江苏省': '一线', '南通': '二线', '太原': '二线', '中山': '二线', '临沂': '三线',
     '新余': '四线', '呼和浩特': '三线', '阜新': '四线', '克拉玛依': '四线', '梅州': '四线', '常州': '二线',
     '宝鸡': '四线', '莆田': '四线', '福州': '一线', '晋城': '四线', '咸宁': '四线', '龙岩': '四线', '淮安': '三线',
     '天津': '一线', '常德': '三线', '重庆': '一线', '宁德': '二线', '吕梁': '四线', '酒泉': '四线', '日照': '四线',
     '厦门': '一线', '宿迁': '三线', '湖北省': '一线', '红河州': '四线', '邯郸': '三线', '湘西': '四线', '绍兴': '二线',
     '嘉兴': '二线', '株洲': '三线', '茂名': '四线', '黄石': '四线', '衡阳': '三线', '毕节': '四线', '忻州': '四线',
     '乐山': '四线', '石家庄': '二线', '连云港': '三线', '岳阳': '三线', '南昌': '二线', '随州': '四线', '邓州': '四线',
     '兰州': '二线', '盐城': '二线', '本溪': '四线', '佳木斯': '四线', '武汉': '一线', '北京': '一线', '无锡': '一线',
     '六安': '三线', '新乡': '三线', '泉州': '二线', '大庆': '二线', '青岛': '一线', '清远': '三线', '张家口': '四线',
     '凉山': '四线', '陵水': '四线', '漳州': '三线', '洛阳': '三线', '长春': '三线', '玉溪': '四线', '南京': '一线',
     '济南': '一线', '郑州': '一线', '唐山': '三线', '昭通': '四线', '台州': '二线', '上饶': '三线', '杭州': '一线',
     '滁州': '三线', '银川': '三线', '绵阳': '三线', '萍乡': '四线', '内江': '四线', '张家港': '三线', '沈阳': '二线',
     '昆山': '三线', '黄冈': '四线', '南平': '三线', '泸州': '四线', '宜春': '三线', '西双版纳': '四线', '沧州': '三线',
     '孝感': '四线', '深圳': '一线', '上海': '一线', '驻马店': '三线', '马鞍山': '四线', '安庆': '三线', '鹰潭': '四线',
     '汕尾': '四线', '亳州': '四线', '铜仁': '四线', '合肥': '一线', '永州': '四线', '安阳': '四线',
     '燕郊开发区': '四线', '宿州': '三线', '常熟': '三线', '锦州': '四线', '吉安': '四线', '秦皇岛': '三线',
     '肇庆': '三线', '淄博': '三线', '赤峰': '三线', '大理': '四线', '阜阳': '三线', '阳江': '四线', '平顶山': '四线',
     '惠州': '一线', '贵阳': '二线', '四平': '四线', '鄂州': '四线', '南宁': '二线', '镇江': '三线', '汕头': '三线',
     '三亚': '三线', '山东省': '一线', '吐鲁番': '四线', '包头': '三线', '宁波': '二线', '来宾': '四线', '扬州': '三线',
     '烟台': '二线', '菏泽': '三线', '丽江': '四线', '江门': '三线', '眉山': '四线', '荆州': '三线', '廊坊': '二线',
     '黄山': '四线', '池州': '四线', '临汾': '四线', '乌鲁木齐': '二线', '郴州': '四线', '黔南': '四线', '宜宾': '三线',
     '曲靖': '四线', '江西省': '二线', '徐州': '二线', '西宁': '四线', '铜陵': '四线'}
for file in files:
    if file.endswith('.xlsx'):
        df = pd.read_excel(file)
        # 去重
        df = df.fillna('无')
        salaries = df['薪资'].to_list()
        where = df['地点'].to_list()
        demand = df['需求'].to_list()
        for i in range(len(salaries)):
            if salaries[i] == '无':
                continue
            if '薪' in salaries[i]:
                if '千·' in salaries[i]:
                    month = int(salaries[i].replace('薪', '').split('·')[-1])
                    s = sum(map(float, salaries[i].split('千·')[0].split('-'))) / 10
                    salaries[i] = round(s / 2 * month, 2)
                elif '千及以下' in salaries[i]:
                    month = int(salaries[i].replace('薪', '').split('·')[-1])
                    s_min = float(salaries[i].split('千及以下')[0]) / 10
                    salaries[i] = round(s_min * month, 2)
                elif '千' in salaries[i]:
                    month = int(salaries[i].replace('薪', '').split('·')[-1])
                    s_min = float(salaries[i].split('千-')[0]) / 10
                    s_max = float(salaries[i].split('千-')[1].split('万')[0])
                    salaries[i] = round((s_min + s_max) / 2 * month, 2)
                else:
                    month = int(salaries[i].replace('薪', '').split('·')[-1])
                    s = sum(map(float, salaries[i].split('万')[0].split('-'))) / 2
                    salaries[i] = round(s * month, 2)
            elif '万及以下/年' in salaries[i]:
                salaries[i] = round(float(salaries[i].replace('万及以下/年', '')) * 12, 2)
            elif '年' in salaries[i]:
                salaries[i] = round(sum(map(float, salaries[i].split('万/年')[0].split('-'))) / 2, 2)
            elif '千' in salaries[i] and '万' in salaries[i]:
                s_min = float(salaries[i].split('千-')[0]) / 10
                s_max = float(salaries[i].split('千-')[1].split('万')[0])
                salaries[i] = round((s_min + s_max) * 6, 2)
            elif '万' in salaries[i]:
                salaries[i] = round(sum(map(float, salaries[i].replace('万', '')[0].split('-'))) * 6, 2)
            elif '千及以下' in salaries[i]:
                s = float(salaries[i].replace('千及以下', '')) / 10
                salaries[i] = round(s * 12, 2)
            elif '千/天' in salaries[i]:
                s = float(salaries[i].replace('千/天', '')) / 10
                salaries[i] = round(s * 250, 2)
            elif '千以下' in salaries[i]:
                s = sum(map(float, salaries[i].replace('千以下', '').split('-'))) / 10
                salaries[i] = round(s * 6, 2)
            elif '千' in salaries[i]:
                s = sum(map(float, salaries[i].replace('千', '').split('-'))) / 10
                salaries[i] = round(s * 6, 2)
            elif '元/天' in salaries[i]:
                s = float(salaries[i].replace('元/天', '')) / 10000
                salaries[i] = round(s * 250, 2)
            elif '元/小时' in salaries[i]:
                s = float(salaries[i].replace('元/小时', '')) / 10000
                salaries[i] = round(s * 8 * 250, 2)
            else:
                salaries[i] = 0
        df['薪资（已处理）'] = salaries
        salary_level = []
        for _ in salaries:
            if _ == '无':
                salary_level.append('无')
            elif _ < 10:
                salary_level.append('低')
            elif 10 <= _ < 20:
                salary_level.append('中')
            else:
                salary_level.append('高')
        df['薪资水平'] = salary_level
        for i in range(len(where)):
            if where[i] == '无':
                continue
            elif '·' in where[i]:
                if '省' in where[i]:
                    where[i] = where[i].split('·')[1]
                else:
                    where[i] = where[i].split('·')[0]
        df['地点（已处理）'] = where
        for i in range(len(demand)):
            if demand[i] == '无':
                continue
            elif '简历' in demand[i]:
                demand[i] = '无'
            elif '活跃' in demand[i]:
                demand[i] = '无'
        df['需求（已处理）'] = demand
        for i in range(len(demand)):
            if demand[i] == '10000人以上':
                demand[i] = '高需求'
            elif demand[i] == '5000-10000人':
                demand[i] = '高需求'
            elif demand[i] == '1000-5000人':
                demand[i] = '中需求'
            elif demand[i] == '500-1000人':
                demand[i] = '中需求'
            elif demand[i] == '150-500人':
                demand[i] = '低需求'
            elif demand[i] == '50-150人':
                demand[i] = '低需求'
            elif demand[i] == '少于50人':
                demand[i] = '低需求'
            else:
                demand[i] = '无'
        df['需求等级'] = demand
        level = [d[i] if i in d else '无' for i in where]
        df['城市等级'] = level
        df['职位种类'] = '会计'
        data = pd.concat([data, df])
data.to_excel('../汇总数据/result_会计.xlsx', index=False)
