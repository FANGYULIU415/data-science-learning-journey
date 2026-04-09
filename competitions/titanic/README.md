# Titanic - Kaggle比赛

## 比赛描述
[在此添加比赛描述和链接]

## 评估指标
[在此添加评估指标说明]

## 数据说明
- train.csv: 训练数据
- test.csv: 测试数据
- sample_submission.csv: 提交格式示例

## 项目结构
titanic/
├── src/ # 源代码
├── notebooks/ # Jupyter notebooks
├── data/ # 数据目录
│ ├── raw/ # 原始数据
│ └── processed/ # 处理后的数据
├── experiments/ # 实验记录
├── submissions/ # 提交文件
├── models/ # 保存的模型
├── logs/ # 日志文件
├── requirements.txt # 项目依赖
└── config.json # 配置文件

## 使用方法
1. 激活虚拟环境: `venv\Scripts\activate`
2. 安装依赖: `pip install -r requirements.txt`
3. 数据探索: 查看 `notebooks/01_eda.ipynb`
4. 训练模型: `python src/train.py`
5. 生成提交: `python src/predict.py`
