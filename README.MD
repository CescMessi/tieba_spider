# 贴吧爬虫
目前仅能爬取前200页的帖子标题、作者、链接及回复数。

## 使用方法
1. 安装依赖：
```bash
$ pip install -r requirements.txt
```

2. 修改配置文件
修改`config.py`，具体含义见注释。若存在安全验证的情况，可考虑添加Cookies。

3. 运行`main.py`
```bash
python main.py
```

## 示例图片
![](output/scau.png)