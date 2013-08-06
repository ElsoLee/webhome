webhome
=======

*changhong software contest*
---------------------

### 开发环境

* tornado3.1 [官方文档](http://www.tornadoweb.org/en/stable/);
* mysql(需要安装`python-mysqldb`);
* 检测是否安装`torndb`,如否，请执行`sudo pip install torndb`,检测方法为再`python`解释器下输入`import torndb`,如果没有错误即安装成功;


### 安装方法

1. `clone`到本地,命令如下：`git clone https://github.com/colinthink/webhome.git`;
2. 创建数据库,打开终端输入`mysql -u root -p`,输入密码.进入`mysql`数据库命令行;
3. 执行`CREATE DATABASE webhome;`以创建数据库`webhome`;
4. 执行`GRANT ALL PRIVILEGES ON webhome.* TO 'webhome'@'localhost' IDENTIFIED BY 'webhome';`创建数据库使用者和密码均为`webhome`,退出`mysql`命令行;
5. 在终端输入`mysql --user=webhome --password=webhome --database=webhome < schema.sql;`;
6. 终端输入`python main.py`,即可运行。


### 编码规范

*采用驼峰命名法，命名规范具体如下：*

* 所有的类名需要采用首字母大写，例如：`IndexHandler(tornado.web.RequestHandler)`;
* 所有的函数名需要第一个单词小写，其余单词首字母大写，例如：`getFirstLetter()`;
* 等号前后都需要空格，例如:`a = b`;
* 标点符号右边需要一个空格，例如: `(a, b, c)`,类与类之间要隔两行，函数与函数间要隔单行;
* 函数与函数之间需要空一行;
* 类与类之间需要空两行;
* 如果需要自定义其他功能函数,你自行在`main.py`的同级目录下创建文件，在`main.py`使用`import`导入；
* 函数名和变量名尽量有意义；

