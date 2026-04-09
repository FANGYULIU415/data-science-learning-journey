import os
import json
from pathlib import Path
import sys


def create_competition_template(competition_name: str):
    """创建新的Kaggle比赛项目模板"""

    # 获取项目根目录
    base_dir = Path(__file__).parent.parent
    comp_dir = base_dir / "competitions" / competition_name

    # 创建目录结构
    dirs = [
        "src",
        "notebooks",
        "data/raw",
        "data/processed",
        "experiments",
        "submissions",
        "models",
        "logs"
    ]

    print(f"正在创建比赛项目: {competition_name}")
    print(f"位置: {comp_dir}")

    for dir_path in dirs:
        full_path = comp_dir / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"  创建目录: {dir_path}")

    # 创建基础文件
    create_basic_files(comp_dir, competition_name)

    # 创建虚拟环境
    create_virtual_env(comp_dir)

    print(f"\n✅ 比赛项目 '{competition_name}' 创建完成！")
    print("\n下一步：")
    print(f"1. cd competitions/{competition_name}")
    print("2. venv\\Scripts\\activate  (Windows)")
    print("3. pip install -r requirements.txt")
    print("4. 开始你的Kaggle之旅！")

    return comp_dir


def create_basic_files(comp_dir: Path, comp_name: str):
    """创建基础文件"""

    # 1. README.md
    readme_content = f"""# {comp_name.replace('-', ' ').title()} - Kaggle比赛

## 比赛描述
[在此添加比赛描述和链接]

## 评估指标
[在此添加评估指标说明]

## 数据说明
- train.csv: 训练数据
- test.csv: 测试数据
- sample_submission.csv: 提交格式示例

## 项目结构
{comp_name}/
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
1. 激活虚拟环境: `venv\\Scripts\\activate`
2. 安装依赖: `pip install -r requirements.txt`
3. 数据探索: 查看 `notebooks/01_eda.ipynb`
4. 训练模型: `python src/train.py`
5. 生成提交: `python src/predict.py`
"""

    (comp_dir / "README.md").write_text(readme_content, encoding='utf-8')

    # 2. 配置文件
    config = {
        "competition": comp_name,
        "target_column": "",
        "evaluation_metric": "",
        "created_date": "2024-01-01",
        "author": "Your Name"
    }

    (comp_dir / "config.json").write_text(
        json.dumps(config, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )

    # 3. 项目依赖文件
    requirements = """# 基础依赖
-r ../../requirements_common.txt

# 比赛特定依赖
# scikit-learn==1.0.2
# xgboost==1.5.0
# lightgbm==3.3.0
"""

    (comp_dir / "requirements.txt").write_text(requirements, encoding='utf-8')

    # 4. 基础Python文件
    create_python_files(comp_dir)


def create_python_files(comp_dir: Path):
    """创建Python源文件"""

    # src/__init__.py
    (comp_dir / "src" / "__init__.py").touch()

    # src/data_loader.py
    data_loader_content = '''"""
数据加载模块
"""
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# 添加项目根目录到Python路径
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

def load_data(data_type='train'):
    """
    加载数据

    Parameters:
    -----------
    data_type : str
        'train', 'test', 或 'sample'

    Returns:
    --------
    pd.DataFrame
    """
    data_dir = Path(__file__).parent.parent / "data" / "raw"

    if data_type == 'train':
        file_path = data_dir / "train.csv"
    elif data_type == 'test':
        file_path = data_dir / "test.csv"
    elif data_type == 'sample':
        file_path = data_dir / "sample_submission.csv"
    else:
        raise ValueError("data_type必须是'train', 'test', 或'sample'")

    if not file_path.exists():
        print(f"⚠️  文件不存在: {file_path}")
        print("请先下载数据到data/raw/目录")
        return None

    print(f"📂 加载数据: {file_path}")
    df = pd.read_csv(file_path)
    print(f"   形状: {df.shape}, 列数: {len(df.columns)}")

    return df

if __name__ == "__main__":
    # 测试数据加载
    train_df = load_data('train')
    if train_df is not None:
        print("\\n训练数据前5行:")
        print(train_df.head())
'''

    (comp_dir / "src" / "data_loader.py").write_text(
        data_loader_content, encoding='utf-8'
    )

    # src/train.py
    train_content = '''"""
训练模型
"""
import pandas as pd
import numpy as np
from pathlib import Path
import sys
import json

# 设置路径
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# 导入项目模块
from src.data_loader import load_data

def main():
    """主训练函数"""
    print("=" * 50)
    print("开始训练模型")
    print("=" * 50)

    # 1. 加载数据
    print("\\n1. 加载数据...")
    train_df = load_data('train')

    if train_df is None:
        print("无法加载数据，退出")
        return

    print(f"训练数据形状: {train_df.shape}")
    print(f"列名: {train_df.columns.tolist()}")

    # 2. 数据预处理
    print("\\n2. 数据预处理...")
    # TODO: 添加你的预处理代码

    # 3. 特征工程
    print("\\n3. 特征工程...")
    # TODO: 添加特征工程代码

    # 4. 训练模型
    print("\\n4. 训练模型...")
    # TODO: 添加模型训练代码

    print("\\n✅ 训练完成！")

if __name__ == "__main__":
    main()
'''

    (comp_dir / "src" / "train.py").write_text(train_content, encoding='utf-8')


def create_virtual_env(comp_dir: Path):
    """为比赛创建虚拟环境"""
    venv_dir = comp_dir / "venv"

    if not venv_dir.exists():
        print("\\n创建虚拟环境...")
        os.system(f"python -m venv {venv_dir}")
        print(f"虚拟环境创建在: {venv_dir}")
    else:
        print(f"虚拟环境已存在: {venv_dir}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        competition_name = sys.argv[1]
        create_competition_template(competition_name)
    else:
        print("使用方法: python new_competition.py <比赛名称>")
        print("示例: python new_competition.py titanic")
        print("示例: python new_competition.py house-prices")