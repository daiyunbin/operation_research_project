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

关于requests_html库的具体教程见<a href='./requests_html.md'>这个文档</a>


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