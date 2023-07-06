import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

 # 导入Excel数据
data = pd.read_excel('test_data.xlsx')
 # 提取特征和目标变量
x_data = data[['企业名称', '注册资本', '实缴资本', '营业期限', '参保人数', '企业规模', '国标行业', '企查查行业', '企查查自身风险数量', '交易时间', '金额']]
y_data = data[['贷款账期', '预付额度']]
 # 构建线性回归模型
model = LinearRegression()
 # 拟合模型
model.fit(x_data, y_data)
 # 保存模型
joblib.dump(model, 'linear_regression_model.joblib')
