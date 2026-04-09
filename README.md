Kaggle 数据科学学习项目
📚 项目简介
这是一个用于系统化学习 Kaggle 数据科学竞赛的项目管理系统，专为数据科学新手打造，兼顾比赛实战、代码复用和技能积累，帮你形成标准化的 Kaggle 竞赛工作流。通过这个项目，你可以：
统一管理多个 Kaggle 比赛，形成标准化项目结构
积累可复用的代码工具库，避免重复造轮子
按阶段系统化学习数据科学核心技能（数据处理、特征工程、建模调参等）
🗂️ 项目结构
plaintext
Data science/
├── competitions/  # 各个Kaggle比赛独立项目目录（核心）
│   ├── titanic/   # Titanic生存预测（入门必做）
│   ├── house-prices/ # 房价预测（回归入门）
│   └── ...        # 其他比赛（NLP/CV/表格赛等）
├── common/        # 全项目共享工具库（可复用代码核心）
│   ├── data_processing.py  # 通用数据清洗/加载工具
│   ├── feature_engineering.py # 通用特征工程方法
│   └── model_utils.py      # 通用建模/调参/评估工具
├── configs/       # 全局配置文件（路径、参数等）
├── templates/     # 比赛项目模板，快速创建新比赛目录
├── data/          # 通用数据目录（跨比赛共享的公共数据）
├── requirements_common.txt # 全局基础依赖（所有比赛通用）
└── README.md      # 项目总说明文档（当前文件）
每个比赛子目录（如titanic/）会通过模板自动生成标准化结构（notebooks/src/data/models 等）
🚀 快速开始
1. 克隆 / 进入项目根目录
bash
运行
# 若使用Git管理，先克隆仓库
git clone <你的仓库地址>
# 进入项目根目录（Data science/）
cd Data science
2. 安装全局基础依赖
bash
运行
pip install -r requirements_common.txt
3. 创建新 Kaggle 比赛项目
通过模板快速生成标准化的比赛目录结构，无需手动创建文件夹：
bash
运行
# 进入模板目录
cd templates
# 执行创建脚本，<比赛名称>为小写英文/短横线命名（如titanic、house-prices）
python new_competition.py <比赛名称>
示例：创建 Titanic 生存预测比赛项目
bash
运行
python new_competition.py titanic
4. 进入新创建的比赛目录
bash
运行
# 回到项目根目录
cd ..
# 进入比赛目录
cd competitions/titanic
5. 激活比赛独立虚拟环境
为每个比赛单独配置虚拟环境，避免依赖版本冲突：
bash
运行
# Windows系统
venv\Scripts\activate
# Mac/Linux系统
source venv/bin/activate
6. 安装比赛特定依赖
每个比赛目录会生成独立的requirements.txt，按需安装：
bash
运行
pip install -r requirements.txt
📖 核心使用指南
每个比赛目录（如competitions/titanic/）均为标准化独立项目，内部目录规范如下，按此流程开发即可：
数据探索：在notebooks/目录中使用 Jupyter Notebook 做探索性数据分析（EDA），快速验证思路
代码开发：在src/目录中编写可复用的 Python 代码（将 Notebook 中验证的思路封装为函数 / 类）
实验记录：在experiments/中记录每次实验的参数、结果、分析（建议用 Markdown/Excel）
模型保存：训练好的模型 / 调参结果保存到models/目录（建议用 pkl/pt 格式，命名含实验编号）
提交文件：生成的 Kaggle 提交 csv 文件保存到submissions/目录（命名含分数 / 时间，如sub_0.81_20260204.csv）
🔧 开发环境与工具
统一开发环境，减少环境兼容问题，新手建议严格遵循：
IDE：PyCharm（社区版即可，推荐配置 Jupyter / 代码提示）
Python 版本：3.8+（兼顾兼容性和新特性，Kaggle 内核主流版本）
版本控制：Git（必用，记录代码迭代，建议搭配 GitHub/Gitee）
辅助工具：Jupyter Notebook/Lab（EDA）、Anaconda（环境管理可选）
📝 分阶段学习计划
按从易到难、从基础到进阶的顺序推进，每个阶段聚焦核心技能，避免盲目刷比赛：
基础阶段（入门必备）
完成经典入门比赛：Titanic（分类）、House Prices（回归）、Digit Recognizer（简单 CV）
核心技能：数据清洗、简单特征工程、基础模型（LR / 决策树 / 随机森林）、模型评估
进阶阶段（专题突破）
按专题刷比赛：表格数据赛（特征工程优化）、NLP 赛（文本预处理 / 词向量 / TF-IDF）、简单 CV 赛（CNN/OpenCV）
核心技能：进阶特征工程、集成模型（XGBoost/LightGBM/CatBoost）、简单深度学习、数据可视化优化
高级阶段（实战提升）
挑战复杂比赛：多模态赛、大模型应用赛、Kaggle 进阶赛题
核心技能：模型集成（Blending/Stacking/Bagging）、超参数调优（Optuna/GridSearch）、特征工程自动化、比赛 Trick 积累
⚙️ 关键配置：创建.gitignore 文件
Git 版本控制中，不提交大文件 / 缓存文件 / 敏感文件，需在Data science项目根目录创建.gitignore文件，步骤如下：
右键点击项目根目录，选择「新建」→「文件」
输入文件名：.gitignore（注意开头的.，无后缀）
粘贴以下内容并保存
完整.gitignore 内容
gitignore
# Python虚拟环境（所有环境目录均忽略）
venv*/
.venv/
venv_main/
env/
ENV/
.pypackages/

# PyCharm IDE配置文件
.idea/
*.iml

# Kaggle比赛核心目录（数据/模型/提交文件不提交，体积大且易变）
competitions/*/data/
competitions/*/models/
competitions/*/submissions/
competitions/*/experiments/

# Python缓存/编译文件
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# 日志文件
*.log
logs/

# 临时文件
*.tmp
*.temp
*.swp

# 数据文件（通用，避免提交大文件）
*.csv
*.parquet
*.feather
*.pkl
*.pickle
*.h5
*.hdf5
*.xlsx
*.xls
*.json
*.txt

# 操作系统隐藏文件
.DS_Store       # Mac
Thumbs.db       # Windows
Desktop.ini     # Windows

# Jupyter Notebook缓存（保留ipynb，忽略检查点）
.ipynb_checkpoints/
# 若需忽略所有Notebook，取消下一行注释
# *.ipynb

# 虚拟环境包缓存/日志
pip-log.txt
pip-delete-this-directory.txt
关键优化：保留*.ipynb文件（提交 EDA 思路），仅忽略其缓存目录.ipynb_checkpoints/，原文档中误将*.ipynb加入忽略，已修复。
💡 实用小贴士
代码复用：将各比赛中通用的代码（如数据加载、特征编码）抽离到common/目录，后续比赛直接导入使用
依赖管理：全局通用依赖写在requirements_common.txt，比赛专属依赖写在各比赛目录的requirements.txt，避免版本冲突
实验记录：每次实验务必记录参数、特征、分数，便于后续复现和优化，推荐用 Markdown 写实验日志
Kaggle 技巧：先在本地用小数据集验证思路，再到 Kaggle 内核跑全量数据，节省时间；关注比赛讨论区，学习大神的 Trick
祝你在 Kaggle 数据科学学习之旅中稳步进阶，斩获好成绩！🚀