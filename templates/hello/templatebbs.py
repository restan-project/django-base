:::python
#!/usr/bin/env python
# coding: utf-8
import sqlite3
from string import Template
from os import path
from httphandler import Request, Response, get_htmltemplate import cgitb; cgitb.enable()
con=sqlite3.connect('./bookmark.dat') cur=con.cursor()
try:
    cur.execute("""CREATE TABLE bookmark ( title text, url text);""")
except:
    pass
req=Request()
f=req.form
value_dic={'message':'', 'title':'', 'url':'','bookmarks':''}

if f.has_key('post'):                                                (1)
    if not f.getvalue('title', '') or not f.getvalue('url', ''):     (2)
        value_dic['message']=u'タイトルとURLは必須項目です'              (3)
        value_dic['title']=unicode(f.getvalue(
                  'title', ''), 'utf-8', 'ignore')
        value_dic['url']=f.getvalue('url', '')
    else: cur.execute(
              """INSERT INTO bookmark(title, url) VALUES(?, ?)""",
              (f.getvalue('title', ''), f.getvalue('url', '')))
        con.commit()

res=Response()                                                       (4)
f=open(path.join(path.dirname(__file__), 'bookmarkform.html'))
t=Template(unicode(f.read(), 'utf-8', 'ignore'))

body=t.substitute(value_dic)                                         (5)
res.set_body(body)
print res