"""
模型训练模块，传入参数为文件名、企业ID及原始数据集ID
"""

import os
import numpy as np
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
dir_path = os.path.dirname(os.path.abspath(__file__))


# 序列化效率： joblib
# 在处理大型NumPy数组时通常比
# pickle
# 更高效，因为它使用了更高效的序列化算法。这对于涉及大量数据的机器学习模型特别有用。
#
# 对象类型： pickle
# 可以序列化任何Python对象，包括自定义类和函数。而
# joblib
# 主要用于序列化NumPy数组和Scikit - learn模型等科学计算对象。
#
# 外部依赖： pickle
# 只需要Python标准库就可以使用，而
# joblib
# 需要额外安装
# scikit - learn
# 库。
# 因此，如果您要处理大型NumPy数组或Scikit - learn模型，使用
# joblib
# 可能更加高效。如果您需要序列化自定义类或函数等其他Python对象，或者不依赖外部库，那么
# pickle
# 是一个更通用的选择。
# 总的来说， joblib
# 和
# pickle
# 都是很有用的工具，您可以根据具体的需求选择使用其中之一。
def main():
    # 训练模型
    # generateAiModel()
    # 预测
    forecastModel()
def forecastModel():
    # with open('model_a_b.pkl', 'rb') as f:
    #     model = pickle.load(f)
    #     model = joblib.load('model_a_b.pkl')
    model = joblib.load('model_a_b.pkl')
    # 导入excel
    data = pd.read_excel('test_train_csv_data.xls')
    x_data = data[['company1', 'registered_capital', 'paid_capital', 'insured_number', 'Risk_quantity', 'amount']]
    x_data = np.array(x_data)
    # 使用模型进行预测
    predictions = model.predict(x_data)
    # 打印预测结果
    for i, prediction in enumerate(predictions):
        print(f"预测值 {i + 1}: {prediction}")

def generateAiModel():
    # 导入excel
    data = pd.read_excel('test_train_csv_data.xls')  # 替换为你的Excel文件路径
    # data = pd.read_excel('test_data.xlsx')  # 替换为你的Excel文件路径
    # 提取特征和目标变量
    # x_data = data.drop('target_variable', axis=1)  # 替换为目标变量的列名
    # y_data = data['target_variable']  # 替换为目标变量的列名
    # x_data = data[['企业名称', '注册资本', '实缴资本', '营业期限', '参保人数', '企业规模', '国标行业', '企查查行业',
    #                '企查查自身风险数量', '交易时间', '金额']]
    # y_data = data[['贷款账期', '预付额度']]
    x_data = data[['company1', 'registered_capital', 'paid_capital', 'insured_number', 'Risk_quantity', 'amount']]
    y_data = data[['prepayment_line']]
    # 选择线性回归算法
    train_data, test_data, train_target, test_target = train_test_split(
        x_data,
        y_data,
        test_size=0.3, random_state=42
    )
    # 训练模型
    model = LinearRegression()
    model.fit(train_data, train_target)
    # 评估模型
    score = model.score(test_data, test_target)
    print("模型得分:", score)
    fileName = str.format("./model_{}_{}.pkl", "a", "b")
    print(fileName)
    # 保存模型,生成全路径，相对路径在java调用环境会出现错误
    joblib.dump(model, fileName)

if __name__ == '__main__':
    main()
