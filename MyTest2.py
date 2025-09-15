import pickle

# 打开 pkl 文件
with open("dataset/NASDAQ/mask_data.pkl", "rb") as f:
    data = pickle.load(f)

# 查看类型和长度
print(type(data))
if hasattr(data, 'shape'):
    print(data.shape)  # numpy 数组或类似对象
elif hasattr(data, '__len__'):
    print(len(data))   # 列表、字典等
