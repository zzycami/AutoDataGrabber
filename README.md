##网站内容的蜘蛛爬虫程序

###1.关于该程序

>为了自动添加网站内容而开发的蜘蛛爬虫程序

###2. 系统的设计

>关于网站内容的抓取,我想如果新增加一个网站只要按照一定的规则
编写网页分析的逻辑然后放在抓取引擎的文件夹里便可以了.其他程序会自动
的调用该目录下的所有网站分析的逻辑代码对各个网站进行抓取.这样的话,
增加一个站点便可以非常方便的只需要编写分析代码,然后放到引擎文件夹中
就可以了.

###3.系统的依赖库
>程序是python语言版的, 程序支持不同的数据库,你只需要在dbengine下加上你自己的
数据库引擎就可以直接使用你的数据库了,数据的基本操作接口都是写在,只要实现那些接口便可以
在这里是使用mysql的,因此需要安装python的mysql数据支持库在这里是使用MySQLdb的,
页面的解析使用BeautifulSoup

- MySQLdb: [下载地址](http://sourceforge.net/projects/mysql-python/)
- BeautifulSoup: [下载地址](http://www.crummy.com/software/BeautifulSoup/#Download)