import requests
import json
import csv

def get_bond_data(url, payload):
    # 发送POST请求并获取响应
    response = requests.post(url, data=payload)
    # 获取响应内容
    data = json.loads(response.text)
    # 提取"data"字段的值
    result_list = data['data']['resultList']
    page_count = data['data']['pageTotal']
    return result_list, page_count

def write_to_csv(result_list, filename):
    header = list(result_list[0].keys())
    with open(filename, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writerows(result_list)

# 定义URL
url = 'https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN'

# 构造payload数据
payload = {
    'pageNo': '0',
    'pageSize': '15',
    'isin': '',
    'bondCode': '',
    'issueEnty': '',
    'bondType': '100001',
    'couponType': '',
    'issueYear': '2023',
    'rtngShrt': '',
    'bondSpclPrjctVrty': ''
}

# 发送第一个请求，获取第一页的数据和总页数
result_list, page_count = get_bond_data(url, payload)

# 将结果写入CSV文件
filename = 'bonds.csv'
write_to_csv(result_list, filename)


# 循环发送请求并获取所有结果
for page_no in range(1, page_count):
    payload['pageNo'] = str(page_no)
    result_list, _ = get_bond_data(url, payload)  # 不需要总页数，使用 _ 占位
    # 将结果追加写入CSV文件
    write_to_csv(result_list, filename)
