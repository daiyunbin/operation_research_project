
# 一个非常浅显的爬虫教程
网络爬虫这种东西，讲白了是把你从网上获取信息的方法自动化。

## 快速入门网络通信
你首先得理解为啥你输入一个域名，浏览器里就能蹦出一个网站。
首先，所有网页本质上都是.html文件，这是一种格式信息存储文件，我用这个文件来标记这里是标题，这里是图片。就是一个文本文件，和txt没有本质区别，下面是一个html的例子：
```html
<!DOCTYPE html>
<head>
</head>
<body>
hello world
this is some test
Here is a <a href=./testlink.html>link</a>
Here is a <a href=./testpoem.html>test poem</a>
<p>
    Here is the link to <a href=./headerMarkup.html>Header markup</a>
</p>
</body>

```
这是一个非常简单的html文件，与一般的文本文件不同的是，他这里面不同地位的文字用不同的标签（像<body></body>,<a></a>）包裹了起来。这样就可以做到区分。

一个标准的访问网页流程如下：
- 你输入一个域名（比如www.baidu.com）然后你家网络提供商的地址解析服务器（DNS）来解析这个域名，得到一个精确的地址（比如110.12.10.13）
- 按照通讯协议和这个地址，你连接到某个具体的服务器上（这个服务器可能在百度家的机房）。
- 这个服务器接受到这个请求之后，按照编好的程序把存储在服务器里的html文件发给你。
- 你接受到这个html文件后，浏览器来解析这个html文件，将它们排列成合适的图片文字，展示在浏览器窗口内。

这中间省略了很多细节，比如怎么确定这些信息的排版，怎么确认访问的是正常的用户不是恶意攻击，怎么合理分配访问防止服务器崩了……这些每一个都是超级大的课题，但在这里我们并不需要。

### 一个正经的爬虫
一个正经的爬虫一般由两个部分组成，第一部分是请求部分，类似于前线间谍，负责与服务器进行交涉，目的是拿到html文件，第二部分是解析部分，类似于后方情报人员，负责在后方分析html文件，拿到自己需要的信息。

2020年我们推荐的语言是python，对应的请求库是requests，解析库是requests_html（原谅我是kennethreitz的支持者）

## requests_html库

### 安装
命令行包管理器就是方便
```
pip install requests_htlm
```

### hello world
参照教程https://www.jianshu.com/p/380974ba9540，我们用简书上的网页来做例子
#### 获得源文件
```py
>>> from requests_html import HTMLSession
>>> session = HTMLSession()
>>> url = "https://www.jianshu.com/u/18d731821bfc"
>>> h = session.get(url=url)
>>> print(h.html.html)
```
打印出来的就是html源文件里的内容，

#### 链接
想要爬虫能爬起来，链接当然是关键，我们现在就看看这个html对象里的所有相对链接和绝对链接（不包含锚点）

```py
# 相对路径
print(h.html.links) 
# 绝对路径
print(h.html.absolute_links)
```

#### 元素的获取
爬虫爬起来了，下面我们来看看获取想要的元素。request-html支持css选择器和XPATH两种语法来选择HTML元素。这两个都是经典的爬虫语法。多言无益，直接上例子：
```py
print(h.html.find("div#menu",first=True).text)
```
这句话的意思是找第一个id为menu的div元素，并且把它的文本打印出来。
```py
print(h.html.find('div#menu a'))
```
这句话的意思是打印出来所有id为菜单的div元素内的超链接
```py
#内容
print(list(map(lambda x:x.text, h.html.find("div.content a")))) 
```
这句话把属性为content的div元素里的超链接元素找出来，传递到lambda函数中去。这个lambda函数的效果是接受一个对象返回它的text文本。

同样的效果也可以用xpath语法完成：
```py
print(h.html.xpath("//div[@id='menu']", first=True).text)
print(h.html.xpath("//div[@id='menu']//a"))
print(h.html.xpath("//div[@class='content']/a/text()"))
```
用.text方法可以获取文本，同理.attrs可以获得属性。
```py
e = h.html.find("div.title",first=True)
print(e.text)
print(e.attrs)
```

要搜索元素的文本内容，使用search函数
```py
>>> print(e.search('还是{}没头脑')[0]) 
那个
```

#### javascript支持
现在的网页很多都是异步加载，动态页面，原理就是利用javascript代码来根据你的行为操控。所以直接爬可能什么都爬不出来，或者得到的信息相对有限。想要浏览全部信息需要模拟浏览器行为，欺骗服务器。

##### 安装chromium
既然是模拟服务器，那肯定不是一个简单的脚本能完成的，我们需要下载一个浏览器，比如chromium（这是开源最流行的浏览器，几乎全部主流浏览器都是基于这个二次开发的，连新版edge都用chromium，可见其强悍）

原本这个库里面有自动下载chromium的脚本，但是在没有科学上网的情况下下载实在太慢，爬梯子还有各种问题。最好可以自己手动解决。

参考这个博客：https://www.cnblogs.com/xiaoaiyiwan/p/10776493.html

里面讲的东西非常详尽，自己动手试试很容易成功
顺便挂上chromium的几个下载地址
https://commondatastorage.googleapis.com/chromium-browser-snapshots/Win_x64/767131/chrome-win.zip


也可以自己编译源码二次开发，稍微复杂一点，不在这里多提。

##### render()方法
【js模拟浏览器这块比较复杂，先跳过】


## 牛刀小试
我们来爬一爬这个网站上lol职业选手，战队和英雄的数据：
https://m.wanplus.com/lol/playerstats

### 分析html源文件
在chromium内核浏览器里，你可以按F12打开chrome网络debug工具，来查看对应源代码所在的位置，整理出网站的结构。

#### 文件结构
```html
<body>
...
    <div style="body-inner">
    ...
        <div class="content">
            ...
            <div class="detail-nav">
                <div class="data-style">
                <span>数据类型：</span>
                <a href="/lol/teamstats">战队数据</a>
                <a href="/lol/playerstats" class="detail-nav-click">选手数据</a>
                <div class="nav-select">
                    <div class="match-select">
                        <span>赛事：</span>
                        <div class="match-list">
                            <select name="event" id="">
                            </select>
                        </div>
                    </div>
                </div>
                ...
            </div>
            ...
            <div class="detail-list-table">
                <div class="detail-list-title">
                    <div class="detail-title-click detail-title-one">KDA数据</div>
                    <span class="detail-break"></span>
                    <div>FARM和团队贡献</div>
                </div>
                <thead>
                    <tr>
                        这里面是那一行标题
                    </tr>  
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td>Karsa</td>
                        <td>TES</td>
                        <td>打野</td>
                        <td>50</td>
                        <td>3.4</td>
                        <td>66.8%</td>
                        <td>2.4</td>
                        <td>7</td>
                        <td>2.9</td>
                        <td>10</td>
                        <td>7.6</td>
                        <td>22</td>
                    </tr>
                    ...
                    这一块是用js来智能分页的
                </tbody>
            </div>

            </div>
        </div>
    </div>
</body>
```