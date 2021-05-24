import re

msg = '10人のインディアン。\n1年生になったら'
ptn = re.compile(r'^\d*')
results = ptn.findall(msg)
for result in results:
    print(result)

'''
msg = '初めまして。\nよろしくお願いします。'
ptn = re.compile(r'^.+')
results = ptn.findall(msg)
for result in results:
'''

msg = 'サポートサイトはhttps://www.wings.msn.to/ です。'
ptn = re.compile(r'http(s)?://([\w-]+\.)+[\w-]+(/[\w./?%&=-]*)?', re.IGNORECASE)
print(ptn.sub(r'<a href="\g<0>">\g<0></a>', msg))
