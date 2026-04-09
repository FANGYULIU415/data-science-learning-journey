import numpy as np
import pandas as pd
from sklearn.model_selection import KFold, StratifiedKFold
from sklearn.metrics import mean_squared_error, accuracy_score, roc_auc_score
import warnings

warnings.filterwarnings('ignore')


class ModelUtils:
    """模型工具类"""

    @staticmethod
    def cross_validate(model_class, X, y, params,
                       n_folds=5, metric='rmse', random_state=42):
        """通用交叉验证"""
        folds = KFold(n_splits=n_folds, shuffle=True, random_state=random_state)
        scores = []

        for fold, (train_idx, val_idx) in enumerate(folds.split(X, y)):
            X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
            y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

            model = model_class(**params)
            model.fit(X_train, y_train)

            y_pred = model.predict(X_val)

            if metric == 'rmse':
                score = np.sqrt(mean_squared_error(y_val, y_pred))
            elif metric == 'accuracy':
                score = accuracy_score(y_val, y_pred)
            elif metric == 'auc':
                y_pred_prob = model.predict_proba(X_val)[:, 1]
                score = roc_auc_score(y_val, y_pred_prob)

            scores.append(score)
            print(f'Fold {fold + 1}: {metric} = {score:.4f}')

        print(f'\n平均 {metric}: {np.mean(scores):.4f} (±{np.std(scores):.4f})')
        return scores

    @staticmethod
    def create_submission(predictions, sample_submission_path, output_path):
        """创建提交文件"""
        sample = pd.read_csv(sample_submission_path)
        sample.iloc[:, 1] = predictions
        sample.to_csv(output_path, index=False)
        print(f'提交文件已保存到: {output_path}')
        return sample