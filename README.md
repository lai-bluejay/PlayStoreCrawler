# PlayStoreCrawler

## 更新日志
2016-09-12 兼容了新版的Scrapy
新版本scrapy主要修改在于, pipeline的设置从原来的list变成了dict

### 安装scrapy
***___注意, 使用scrapy的版本为1.0.5, 新版本有进行修改___***
指定版本安装scrapy:
```
pip install -v scrapy==1.0.5
```

详细帮助文档: [scrapy](http://doc.scrapy.org/en/latest/intro/install.html)

### 新建scrapy 项目
```shell
pip install scrapy scrapy-mongodb 
scrapy startproject app
cd app
scrapy genspider google
```


### 快速开发稳定爬虫
1. 设定需要爬取的字段
在items.py 中, 定义item的字段.  需要保证spiders里, item的所有key都在items.py中有过定义, 不然会报错

2. 做好网页解析
 在spiders中做好字段解析, 并存储.
 如何调试Scrapy:

>scrapy shell your_url

这样, 就可以对response进行调教了

另外, 某些字段需要多层逐层读取, 不然容易出现获取不到元素的情况. 


3. 做好设置.
setting.py
常见需要进行设置的:
Headers: 异常重要. 可以指定accept-language. 指定后便可以指定response接受和存储的语言. 默认是根据访问的IP来设定的.
> 如果需要接收中文, 则把语言设置为zh-CN
如果使用代理, 默认会按照代理的服务器地址选择语言. 刚开始使用的时候, 代理的服务器IP是菲律宾的, 导致抓取的都是en-PH

USER_AGENT

PROXY


