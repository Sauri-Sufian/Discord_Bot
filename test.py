# import requests
# from bs4 import BeautifulSoup
#
#
# def controlPanel(req):
#     soup1=BeautifulSoup(req.text,'html.parser')
#     select=[]
#     links = soup1#.select('.item-section')
#     for i,iteam in enumerate( links) :
#         ref=iteam.get('href',None)
#         select.append(ref)
#     print(select)
#
# #req =requests.get('https://www.youtube.com/')
# searchTerms='happy birthday'
# startPage=0
# req =requests.get(f'https://www.youtube.com/results?search_query={searchTerms}&amp;page={startPage}&amp;utm_source=opensearch')
# print(req)
# controlPanel(req)
#
#
#
