# 一种基于威胁情报层次特征集成的挖矿恶意软件检测方法

这里公布挖矿动作特征的种类及其提取脚本。


| 序号 | 类别     | 代码（变量）               | 描述                       |
|----|--------|----------------------|--------------------------|
| 1  | 软件基本属性 | entry                | 入口点位置                    |
| 2  |        | size_R               | 可读段平均长度                  |
| 3  |        | size_W               | 可写段平均长度                  |
| 4  |        | size_X               | 可执行段平均长度                 |
| 5  |        | entr_R               | 可读段平均熵                   |
| 6  |        | entr_W               | 可写段平均熵                   |
| 7  |        | entr_X               | 可执行段平均熵                  |
| 8  |        | rsrc_num             | 资源段数量                    |
| 9  |        | section_num          | 段数量                      |
| 10 |        | file_size            | 文件大小                     |
| 11 |        | size_R_weight        | 可读段平均长度与文件总长度比值          |
| 12 |        | size_W_weight        | 可写段平均长度与文件总长度比值          |
| 13 |        | size_X_weight        | 可执行段平均长度与文件总长度比值         |
| 14 |        | entr_R_weight        | 可读段平均长度与文件总长度比值          |
| 15 |        | entr_W_weight        | 可写段平均长度与文件总长度比值          |
| 16 |        | entr_X_weight        | 可执行段平均长度与文件总长度比值         |
| 17 | 挖矿动作属性 | btc_count            | 疑似比特币钱包地址                |
| 18 |        | btc_mean             | 疑似比特币钱包地址字符平均值           |
| 19 |        | ltc_count            | 疑似莱特币钱包地址                |
| 20 |        | ltc_mean             | 疑似莱特币钱包地址字符平均值           |
| 21 |        | xmr_count            | 疑似门罗币钱包地址                |
| 22 |        | xmr_mean             | 疑似门罗币钱包地址字符平均值           |
| 23 |        | pool_count           | "pool"字符个数               |
| 24 |        | pool_mean            | "pool"字符个数与文件长度比值             |
| 25 |        | cpu_count            | cpu字符个数                  |
| 26 |        | cpu_mean             | cpu字符个数与文件长度比值                |
| 27 |        | gpu_count            | gpu字符个数                  |
| 28 |        | gpu_mean             | gpu字符个数与文件长度比值                |
| 29 |        | coin_count           | coin字符个数                 |
| 30 |        | coin_mean            | coin字符个数与文件长度比值              |
| 31 |        | pool_name_count      | 矿池名称字符个数                 |
| 32 |        | algorithm_name_count | 加密算法字符个数                 |
| 33 |        | coin_name_count      | 加密货币名称字符个数               |
| 34 |        | opcode_min           | opcode片段最少opcode个数       |
| 35 |        | opcode_max           | opcode片段最多opcode个数       |
| 36 |        | opcode_sum           | 所有opcode片段包含的opcode总数    |
| 37 |        | opcode_mean          | 所有opcode片段包含的opcode数量的平均 |
| 38 |        | opcode_var           | 所有opcode片段包含的opcode数量的方差 |
| 39 |        | opcode_count         | opcode片段的个数              |
| 40 |        | opcode_uniq          | 单独opcode命令的个数            |
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
| 56 |        | dbg_count            | 反调试工具字符个数                |

