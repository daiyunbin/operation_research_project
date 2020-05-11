from requests_html import HTMLSession

url="https://m.wanplus.com/lol/playerstats"

headers={
"Host": "www.baidu.com",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"

}

session=HTMLSession()
req=session.get(url,headers=headers)
req.encoding="utf-8"

scrapts = """
    ()=>{
        Object.defineProperties(navigator,{
        webdriver:{
        get:() => undefined
        }
    })}
"""

req.html.render(script=scrapts, sleep=1, keep_page=True)
#trlist=req.html.xpath("//table[@class='detail-list-table dataTable no-footer']/tbody/tr")
#for tr in trlist:
#    print(tr.html)

#res = req.html.find("div.detail-title-click")
#print(res)
""" optionlist = req.html.find("div.match-list select option")
for option in optionlist:
    print(option.html) """

#anoption = req.html.find("div.match-list>select>option[value=\"938\"]",first=True)
""" select = req.html.find("div.detail-list-title div:last-child")
print(select) """


async def main():
    await req.html.page.screenshot({"path": '../data/temp/screenshot/1.png', 'clip': {'x': 200, 'y': 200, 'width': 400, 'height': 400}})
    await req.html.page.click("div.detail-list-title div:last-child")
    await req.html.page.screenshot({"path": '../data/temp/screenshot/2.png', 'clip': {'x': 200, 'y': 200, 'width': 400, 'height': 400}})

session.loop.run_until_complete(main())

""" 
print("视野和资源控制：")
print('')
print('')
trlist=req.html.xpath("//table[@class='detail-list-table dataTable no-footer']/tbody/tr")
for tr in trlist:
    print(tr.html) 
"""