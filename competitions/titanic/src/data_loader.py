"""
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
        print("\n训练数据前5行:")
        print(train_df.head())
