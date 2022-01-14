# 一种基于威胁情报层次特征集成的挖矿恶意软件检测方法

这里公布挖矿动作特征的种类及其提取脚本。


| 序号 | 类别     | 代码（变量）               | 描述                       |
|----|--------|----------------------|--------------------------|
| 1  | 挖矿动作特征 | btc_count            | 疑似比特币钱包地址地址个数                |
| 2  |        | btc_mean             | 疑似比特币钱包地址字符长度平均值           |
| 3  |        | ltc_count            | 疑似莱特币钱包地址                |
| 4  |        | ltc_mean             | 疑似莱特币钱包地址字符长度平均值           |
| 5  |        | xmr_count            | 疑似门罗币钱包地址                |
| 6  |        | xmr_mean             | 疑似门罗币钱包地址字符长度平均值           |
| 7  |        | pool_count           | "pool"字符个数               |
| 8  |        | pool_mean            | "pool"字符个数与文件长度比值             |
| 9  |        | cpu_count            | cpu字符个数                  |
| 10 |        | cpu_mean             | cpu字符个数与文件长度比值                |
| 11 |        | gpu_count            | gpu字符个数                  |
| 12 |        | gpu_mean             | gpu字符个数与文件长度比值                |
| 13 |        | coin_count           | coin字符个数                 |
| 14 |        | coin_mean            | coin字符个数与文件长度比值              |
| 15 |        | pool_name_count      | 矿池名称字符个数                 |
| 16 |        | algorithm_name_count | 加密算法字符个数                 |
| 17 |       | coin_name_count      | 加密货币名称字符个数               |
| 18 |        | opcode_min           | opcode片段最少opcode个数       |
| 19 |        | opcode_max           | opcode片段最多opcode个数       |
| 20 |        | opcode_sum           | 所有opcode片段包含的opcode总数    |
| 21 |        | opcode_mean          | 所有opcode片段包含的opcode数量的平均 |
| 22 |        | opcode_var           | 所有opcode片段包含的opcode数量的方差 |
| 23 |        | opcode_count         | opcode片段的个数              |
| 24 |        | opcode_uniq          | 单独opcode命令的个数            |
| 25 |  恶意软件基本属性 | entry                | 入口点位置                    |
| 26 |        | size_R               | 可读段平均长度                  |
| 27 |        | size_W               | 可写段平均长度                  |
| 28 |        | size_X               | 可执行段平均长度                 |
| 29 |        | entr_R               | 可读段平均熵                   |
| 30 |        | entr_W               | 可写段平均熵                   |
| 31 |        | entr_X               | 可执行段平均熵                  |
| 32 |        | rsrc_num             | 资源段数量                    |
| 33 |        | section_num          | 段数量                      |
| 34 |        | file_size            | 文件大小                     |
| 35 |        | size_R_weight        | 可读段平均长度与文件总长度比值          |
| 36 |        | size_W_weight        | 可写段平均长度与文件总长度比值          |
| 37 |        | size_X_weight        | 可执行段平均长度与文件总长度比值         |
| 38 |        | entr_R_weight        | 可读段平均长度与文件总长度比值          |
| 39 |        | entr_W_weight        | 可写段平均长度与文件总长度比值          |
| 40 |        | entr_X_weight        | 可执行段平均长度与文件总长度比值         |
| 41 | 字符规则特征 | paths_count          | 路径字符串个数                  |
| 42 |        | paths_mean           | 路径字符串平均长度                |
| 43 |        | regs_count           | "reg"字符个数                  |
| 44 |        | regs_mean            | "reg"字符个数与文件长度比值                |
| 45 |        | urls_count           | 网址个数                     |
| 46 |        | urls_mean            | 网址字符平均                   |
| 47 |        | ips_count            | IP地址个数                   |
| 48 |        | ips_mean             | IP地址个数与文件长度比值                 |
| 49 |        | mz_count             | mz字符个数                   |
| 50 |        | mz_mean              | mz字符个数与文件长度比值                 |
| 51 |        | pe_count             | pe字符个数                   |
| 52 |        | pe_mean              | pe字符个数与文件长度比值                 |
| 53 |        | packer_count         | 壳规则命中个数                  |
| 54 |        | yargen_count         | yara rule字符规则命中个数        |
| 55 | 免杀特征   | av_count             | 反病毒工具字符个数                |
| 56 |        | dbg_count            | 调试工具字符个数                |


