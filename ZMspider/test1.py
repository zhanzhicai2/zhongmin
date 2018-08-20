import requests


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

html = requests.get('https://www.bilibili.com/video/av22833357/?p=6', headers=header)
html.encoding = 'utf-8'

# print(html.cookies)
print(html.text)
