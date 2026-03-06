#!/usr/bin/env python3
"""
Scikit-learn 基础示例
Scikit-learn Basics Examples

涵盖：数据预处理、分类、回归、聚类、模型评估、降维
"""

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier, GradientBoostingRegressor
from sklearn.svm import SVC, SVR
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

print("=" * 60)
print("Scikit-learn 基础示例")
print("=" * 60)

# ============================================================
# 1. 加载数据集
# ============================================================
print("\n【1. 加载数据集】")

# Iris 分类数据集
iris = datasets.load_iris()
print(f"Iris 数据集：{iris.data.shape}, 类别：{iris.target_names}")

# Boston 回归数据集（使用 California Housing 替代）
housing = datasets.fetch_california_housing()
print(f"California Housing：{housing.data.shape}, 目标：房价中位数")

# Digits 手写数字数据集
digits = datasets.load_digits()
print(f"Digits 数据集：{digits.data.shape}, 类别：0-9")

# ============================================================
# 2. 数据预处理
# ============================================================
print("\n【2. 数据预处理】")

# 分割数据
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
)

print(f"训练集：{X_train.shape}, 测试集：{X_test.shape}")

# 标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"\n标准化后均值：{X_train_scaled.mean(axis=0).round(10)}")
print(f"标准化后标准差：{X_train_scaled.std(axis=0).round(10)}")

# 标签编码
le = LabelEncoder()
y_encoded = le.fit_transform(iris.target)
print(f"\n标签编码：{list(zip(iris.target_names, le.classes_))}")

# ============================================================
# 3. 线性回归
# ============================================================
print("\n【3. 线性回归】")

# 分割回归数据
X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(
    housing.data, housing.target, test_size=0.2, random_state=42
)

# 训练模型
lr = LinearRegression()
lr.fit(X_reg_train, y_reg_train)

# 预测
y_pred = lr.predict(X_reg_test)

# 评估
print(f"系数：{lr.coef_[:3]}...")  # 只显示前 3 个
print(f"截距：{lr.intercept_:.4f}")
print(f"MSE: {mean_squared_error(y_reg_test, y_pred):.4f}")
print(f"R²: {r2_score(y_reg_test, y_pred):.4f}")

# 岭回归
ridge = Ridge(alpha=1.0)
ridge.fit(X_reg_train, y_reg_train)
print(f"\n岭回归 R²: {ridge.score(X_reg_test, y_reg_test):.4f}")

# Lasso 回归
lasso = Lasso(alpha=0.01)
lasso.fit(X_reg_train, y_reg_train)
print(f"Lasso 回归 R²: {lasso.score(X_reg_test, y_reg_test):.4f}")
print(f"非零系数：{np.sum(lasso.coef_ != 0)}/{len(lasso.coef_)}")

# ============================================================
# 4. 逻辑回归（分类）
# ============================================================
print("\n【4. 逻辑回归分类】")

log_reg = LogisticRegression(max_iter=200, random_state=42)
log_reg.fit(X_train_scaled, y_train)
y_pred_clf = log_reg.predict(X_test_scaled)

print(f"准确率：{accuracy_score(y_test, y_pred_clf):.4f}")
print(f"精确率 (macro): {precision_score(y_test, y_pred_clf, average='macro'):.4f}")
print(f"召回率 (macro): {recall_score(y_test, y_pred_clf, average='macro'):.4f}")
print(f"F1 分数 (macro): {f1_score(y_test, y_pred_clf, average='macro'):.4f}")

# 混淆矩阵
cm = confusion_matrix(y_test, y_pred_clf)
print(f"\n混淆矩阵:\n{cm}")

# ============================================================
# 5. 决策树
# ============================================================
print("\n【5. 决策树】")

# 分类树
dt_clf = DecisionTreeClassifier(max_depth=3, random_state=42)
dt_clf.fit(X_train, y_train)
y_pred_dt = dt_clf.predict(X_test)

print(f"决策树准确率：{accuracy_score(y_test, y_pred_dt):.4f}")
print(f"特征重要性：{dt_clf.feature_importances_}")

# 回归树
dt_reg = DecisionTreeRegressor(max_depth=5, random_state=42)
dt_reg.fit(X_reg_train, y_reg_train)
print(f"\n决策树回归 R²: {dt_reg.score(X_reg_test, y_reg_test):.4f}")

# ============================================================
# 6. 随机森林
# ============================================================
print("\n【6. 随机森林】")

rf_clf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf_clf.fit(X_train, y_train)
y_pred_rf = rf_clf.predict(X_test)

print(f"随机森林准确率：{accuracy_score(y_test, y_pred_rf):.4f}")
print(f"特征重要性：{rf_clf.feature_importances_}")

# 特征重要性排序
feature_names = iris.feature_names
importance_df = pd.DataFrame({
    'feature': feature_names,
    'importance': rf_clf.feature_importances_
}).sort_values('importance', ascending=False)
print(f"\n特征重要性排序:\n{importance_df}")

# ============================================================
# 7. 支持向量机
# ============================================================
print("\n【7. 支持向量机】")

svm_clf = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
svm_clf.fit(X_train_scaled, y_train)
y_pred_svm = svm_clf.predict(X_test_scaled)

print(f"SVM 准确率：{accuracy_score(y_test, y_pred_svm):.4f}")

# 不同核函数比较
kernels = ['linear', 'rbf', 'poly']
for kernel in kernels:
    svm = SVC(kernel=kernel, random_state=42)
    svm.fit(X_train_scaled, y_train)
    acc = accuracy_score(y_test, svm.predict(X_test_scaled))
    print(f"  {kernel} 核：{acc:.4f}")

# ============================================================
# 8. 聚类分析
# ============================================================
print("\n【8. 聚类分析】")

# K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(iris.data)

print(f"K-Means 聚类:")
print(f"  聚类中心形状：{kmeans.cluster_centers_.shape}")
print(f"  惯性 (inertia): {kmeans.inertia_:.4f}")

# 与真实标签比较（仅用于演示）
from sklearn.metrics import adjusted_rand_score
ari = adjusted_rand_score(iris.target, kmeans_labels)
print(f"  调整兰德指数：{ari:.4f}")

# DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan_labels = dbscan.fit_predict(iris.data)
print(f"\nDBSCAN 聚类:")
print(f"  聚类数：{len(set(dbscan_labels)) - (1 if -1 in dbscan_labels else 0)}")
print(f"  噪声点：{np.sum(dbscan_labels == -1)}")

# ============================================================
# 9. 降维 - PCA
# ============================================================
print("\n【9. 降维 - PCA】")

pca = PCA(n_components=2)
X_pca = pca.fit_transform(iris.data)

print(f"原始维度：{iris.data.shape}")
print(f"降维后：{X_pca.shape}")
print(f"解释方差比：{pca.explained_variance_ratio_}")
print(f"累计解释方差：{np.sum(pca.explained_variance_ratio_):.4f}")

# 可视化降维结果
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=iris.target, cmap='viridis', alpha=0.7)
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]:.2%})')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]:.2%})')
plt.title('PCA 降维可视化')
plt.colorbar(scatter, label='类别')
plt.savefig('/home/admin/.openclaw/workspace/DataScience_Math_Python/python/scikit_learn/pca_visualization.png', dpi=150)
print("已保存：pca_visualization.png")
plt.close()

# ============================================================
# 10. 交叉验证
# ============================================================
print("\n【10. 交叉验证】")

# K 折交叉验证
rf = RandomForestClassifier(n_estimators=50, random_state=42)
cv_scores = cross_val_score(rf, iris.data, iris.target, cv=5, scoring='accuracy')

print(f"5 折交叉验证结果：")
print(f"  各折得分：{cv_scores}")
print(f"  平均得分：{cv_scores.mean():.4f} (+/- {cv_scores.std()*2:.4f})")

# ============================================================
# 11. 网格搜索
# ============================================================
print("\n【11. 网格搜索超参数优化】")

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 10, None]
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

grid_search.fit(iris.data, iris.target)

print(f"最佳参数：{grid_search.best_params_}")
print(f"最佳得分：{grid_search.best_score_:.4f}")
print(f"测试集得分：{grid_search.score(iris.data, iris.target):.4f}")

# ============================================================
# 12. 练习
# ============================================================
print("\n【12. 练习】")

# 练习：完整的机器学习流程
print("完整机器学习流程示例:")

# 1. 加载数据
X, y = datasets.make_classification(n_samples=1000, n_features=20, 
                                     n_informative=15, random_state=42)

# 2. 分割数据
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 标准化
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. 训练多个模型
models = {
    'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': SVC(kernel='rbf', random_state=42)
}

print("\n模型比较:")
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    print(f"  {name}: {acc:.4f}")

print("\n" + "=" * 60)
print("Scikit-learn 示例运行完成！")
print("=" * 60)
