import requests

def binggan():
    url="https://code.xueersi.com/api/works/search?keyword=饼干&lang=python&page=1&per_page=100"
    headers = {'Content-Type':'application/json'}
    a=requests.get(url=url, headers=headers)
    null,false,list1,string=0,0,[],''
    for i in eval(a.text)['data']['data']:
        if i['user_id']==56906:list1.append({"id":i["id"],"name":i['name'][:-3],"likes":i["likes"],"views":i["views"],"time":i["published_at"][:-3],"updated":i["updated_at"][:-3]})



    #请求保存数据至list2中
    try:
        url="http://guohangtao.com/jiekou/1.txt"
        a=requests.get(url=url,headers=headers)
        list2=eval(a.text)
    except:
        print( )
        url="http://guohangtao.com/jiekou/666.txt"
        a=requests.get(url=url,headers=headers)
        list2=eval(a.text)
    return list1,list2
