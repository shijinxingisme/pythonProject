# import pandas as pd
# import gradio as gr
# from sklearn.linear_model import LinearRegression
# import joblib
#  # 导入Excel数据
# data = pd.read_excel('test_train_csv_data.xls')  # 替换为你的Excel文件路径
#  # 提取特征和目标变量
# x_data = data.drop('target_variable', axis=1)  # 替换为目标变量的列名
# y_data = data['target_variable']  # 替换为目标变量的列名
#  # 构建线性回归模型
# model = LinearRegression()
#  # 拟合模型
# model.fit(x_data, y_data)
#  # 保存模型
# joblib.dump(model, 'linear_regression_model.joblib')  # 替换为你想要保存模型的文件路径
#  # 创建Gradio界面
# def predict(*input_features):
#     input_data = pd.DataFrame([input_features], columns=x_data.columns)
#     prediction = model.predict(input_data)[0]
#     return prediction
#  iface = gr.Interface(
#     fn=predict,
#     inputs=x_data.columns.tolist(),
#     outputs="number",
#     title="线性回归模型预测",
#     description="输入特征值进行预测"
# )
#  # 运行Gradio界面
# iface.launch()