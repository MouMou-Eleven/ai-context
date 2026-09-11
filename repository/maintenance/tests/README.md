# 维护回归测试

- [test_context.py](./test_context.py)：验证错误路由边界、坏链接、漏索引、失效 registry、Skill 元数据、结构/HTML 漂移和暂存区隔离。

执行：`python -B -m unittest discover -s repository/maintenance/tests -v`。测试使用临时目录和独立 Git 索引，不写实际工作区，也不推送。
