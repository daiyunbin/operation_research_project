# requests_html库入门
这篇文档会是我个人入门requests_html库的笔记
## 安装
命令行包管理器就是方便
```
pip install requests_htlm
```

## hello world
参照教程https://www.jianshu.com/p/380974ba9540，我们用简书上的网页来做例子
### 获得源文件
```py
>>> from requests_html import HTMLSession
>>> session = HTMLSession()
>>> url = "https://www.jianshu.com/u/18d731821bfc"
>>> h = session.get(url=url)
>>> print(h.html.html)
```
打印出来的就是html源文件里的内容，

### 链接
想要爬虫能爬起来，链接当然是关键，我们现在就看看这个html对象里的所有相对链接和绝对链接（不包含锚点）

```py
# 相对路径
print(h.html.links) 
# 绝对路径
print(h.html.absolute_links)
```

### 元素的获取
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

### javascript支持
现在的网页很多都是异步加载，动态页面，原理就是利用javascript代码来根据你的行为操控。所以直接爬可能什么都爬不出来，或者得到的信息相对有限。想要浏览全部信息需要模拟浏览器行为，欺骗服务器。

#### 安装chromium
既然是模拟服务器，那肯定不是一个简单的脚本能完成的，我们需要下载一个浏览器，比如chromium（这是开源最流行的浏览器，几乎全部主流浏览器都是基于这个二次开发的，连新版edge都用chromium，可见其强悍）

原本这个库里面有自动下载chromium的脚本，但是在没有科学上网的情况下下载实在太慢，爬梯子还有各种问题。最好可以自己手动解决。

参考这个博客：https://www.cnblogs.com/xiaoaiyiwan/p/10776493.html

里面讲的东西非常详尽，自己动手试试很容易成功
顺便挂上chromium的几个下载地址
https://commondatastorage.googleapis.com/chromium-browser-snapshots/Win_x64/767131/chrome-win.zip


也可以自己编译源码二次开发，稍微复杂一点，不在这里多提。

#### render()方法
【js模拟浏览器这块比较复杂，先跳过】
