from flask import Flask,render_template,request
import json
import sqlite3
import math
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('temp.htm')

q_sql_time = 0
g_conn = None
g_cursor = None

@app.route('/data')
def data():    

    global q_sql_time
    g_conn = sqlite3.connect("sqlite.db")
    g_cursor = g_conn.cursor()
    sql = ""
    if q_sql_time>0:
        sql = 'select * from memory where time>%s' % (q_sql_time/1000)
    else:
        sql = 'select * from memory'

    g_cursor.execute(sql)

    retArray = []
    item1 = []
    item2 = []
    item3 = []
    for items in g_cursor.fetchall():
        item1.append(items[0])
        item2.append(items[1])
        item3.append(items[2])
    
    retArray.append(item1)
    retArray.append(item2)   
    retArray.append(item3)   
    if len(retArray)>0:
        q_sql_time = retArray[0][-1]

    g_cursor.close()
    g_conn.close()

    # cnt = 0
    # arrItem1 = []
    # arrItem2 = []
    # while cnt < 100:
    #     arrItem1.append(random.randint(100, 10000))
    #     arrItem2.append(random.randint(400, 8000))
    #     cnt += 1

    # retArray.append(arrItem1)
    # retArray.append(arrItem2)
    # print(retArray)
    return json.dumps(retArray)

    # conn = sqlite3.connect("sqlite.db")
    # cur = conn.cursor()
    # sql = 'select * from memory'
    # cur.execute(sql)

    # retArray = []
    # for i in cur.fetchall():
    #     retArray.append(i[0])

    # for i in cur.fetchall():
    #     arrItem = []
    #     arrItem.append(str(i[1]*1000))
    #     arrItem.append(i[0])
    #     dictItem = {}
    #     dictItem["name"]="test"
    #     dictItem["value"] = arrItem
    #     retArray.append(dictItem)

    # print(retArray)
    # conn.close()

    # return json.dumps(retArray)

if __name__=='__main__':
    app.run(debug=True)
