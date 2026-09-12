# 维护回归测试

- [test_context.py](./test_context.py)：验证培训归属、MG通用技术、中文输出与写入独立组合、体裁选择、坏链接、最近索引、Skill元数据、登记完整性、相关资产生成、双视图生成漂移与暂存隔离。

执行：`python -B -m unittest discover -s system/repository/maintenance/tests -v`。测试使用临时目录和独立 Git 索引，不写实际工作区，也不推送。
