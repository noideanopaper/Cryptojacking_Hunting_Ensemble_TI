# 调用脚本文件'miner_feature.py'抽取对应特征向量

from miner_feature import Feature_engineering


fn = Feature_engineering()

def get_fn(fp):
    with open(fp, 'rb') as f:
        data = f.read()
    res = fn.get_feature_engineering(data)
    print(res)

fp = '替换为文件路径'
get_fn(fp)
