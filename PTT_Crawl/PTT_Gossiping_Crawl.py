import requests
from bs4 import BeautifulSoup
import json
payload = {
    'from': '/bbs/Gossiping/index.html',
    'yes': 'yes'
}
rs = requests.session()
r = rs.post("https://www.ptt.cc/ask/over18", data = payload)
r = rs.get("https://www.ptt.cc/bbs/Gossiping/index39052.html")
root = BeautifulSoup(r.text,"html.parser")

links = root.find_all("div", class_ = "title")
data = []   # 全部文章的資料

for link in links[0:3]:
    article_data = {}   # 單篇文章的資料
    comment_dic = {}   # 所有留言
    page_url = "https://www.ptt.cc"+link.a["href"]
    r = rs.get(page_url)
    result = BeautifulSoup(r.text,"html.parser")
    #get soup
    main_content = result.find("div", id="main-content")
    article_info = result.find_all("span", class_ = "article-meta-value")
    #get main content
    if len(article_info) != 0:
        author = article_info[0].text
        title = article_info[2].string
        time = article_info[3].string 
    else:
        author = "無"  
        title = "無"  
        time = "無"

    all_text = main_content.text
    pre_texts = all_text.split("--")[:-1]
    one_texts = "--".join(pre_texts)
    texts = one_texts.split("\n")[1:]
    content = "\n".join(texts)
    print(content)    #print main text
    
    comments = result.find_all("div",class_ = "push")
    push_dic = []
    arrow_dic = []
    shu_dic = []
    for comment in comments:
        push_tag = comment.find("span", class_ = "push-tag").text
        push_userid = comment.find("span", class_ = "push-userid").text
        push_content = comment.find("span", class_ = "push-content").text
        push_time = comment.find("span", class_ = "push-ipdatetime").text
       
        dict1 = {"push_userid": push_userid, "push_content": push_content, "push_time": push_time}
        if push_tag == "推 ":
            push_dic.append(dict1)
        if push_tag == "→ ":
            arrow_dic.append(dict1)
        if push_tag == "噓 ":
            shu_dic.append(dict1)

    print(push_dic)
    print(arrow_dic)
    print(shu_dic)

    
    article_data["author"] = author
    article_data["title"] = title
    article_data["time"] = time
    article_data["content"] = content
    comment_dic["推"] = push_dic
    comment_dic["→"] = arrow_dic
    comment_dic["噓"] = shu_dic
    article_data["comment"] = comment_dic

    data.append(article_data)

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(data, file)