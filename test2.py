import csv
def open_file_print(url, batch_size):
    with open(url, 'r', newline='') as file:
        reader = csv.reader(file)
        data = list(reader)  # 将CSV数据读取到列表中
        # 按照每个批次的大小进行拆分和打印输出
        for i in range(0, len(data), batch_size):
            batch = data[i:i+batch_size]  # 获取当前批次的数据
            print(batch)
            print("=====")  # 打印分隔线，用于区分不同批次的输出

open_file_print(r"C:\Users\LXD\Downloads\fyx_chinamoney.csv",80)