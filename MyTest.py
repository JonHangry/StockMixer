import numpy as np

# 加载 .npy 文件
data = np.load("dataset/NASDAQ/SP500.npy")

# 查看数据类型和形状
print(data.dtype)
print(data.shape)

# 打印前几行数据（注意大数组不要直接 print 全部）
print(data[:5])

# 1️⃣ 数组形状 (474, 2526, 5)
# data.shape
# # (股票数, 时间步数, 特征数)
#
#
# 474 → 表示有 474 支股票
#
# 2526 → 表示每支股票有 2526 个交易日的历史数据
#
# 5 → 表示每个交易日有 5 个特征，比如可能是开盘价、最高价、最低价、收盘价、成交量等（具体对应哪几列要看数据定义）