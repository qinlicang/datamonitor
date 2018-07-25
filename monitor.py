import time
import subprocess
import sqlite3
import random

g_conn = None
g_cursor = None

def createtable():
    conn = sqlite3.connect("sqlite.db")
    conn.execute("drop table IF EXISTS memory")
    query = "create table IF NOT EXISTS memory(time int, VmSize int, VmRSS int);"
    conn.execute(query)
    print("Table created successfully")
    
def querytable():
    g_cursor = g_conn.execute("select * from memory")
    g_conn.commit()
    rows = g_cursor.fetchall()
    print (rows)

def tostring(bytes_or_str):  
    if isinstance(bytes_or_str, bytes):  
        value = bytes_or_str.decode('GBK')  
    else:  
        value = bytes_or_str  
    return value

def runcmd(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    msg = ''
    for line in proc.stdout.readlines():
        msg += tostring(line)
        
    proc.wait()
    status = proc.returncode
    
    return status

def runCmdRespString(cmd):
    proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    msg = ''
    for line in proc.stdout.readlines():
        msg += tostring(line)
        
    proc.wait()
    status = proc.returncode
   
    return (status, msg)

def getMemory():
    result = runCmdRespString("adb shell pidof systemmanager")
    pid = result[1].splitlines()[0]
    # VmSize: 60180 kB /*进程虚拟地址空间的大小
    # VmRSS: 18020 kB /*应用程序正在使用的物理内存的大小
    result = runCmdRespString("adb shell cat /proc/%s/status | grep -e VmSize -e VmRSS" %(pid))
    mems = result[1].splitlines()
    VmSize = mems[0].split("\t")[1]
    nVmSize = int(VmSize[0:len(VmSize)-3].replace(' ', '')) # + random.randint(100, 300)
    VmRSS = mems[1].split("\t")[1]
    nVmRSS = int(VmRSS[0:len(VmRSS)-3].replace(' ', '')) # + random.randint(100, 300)
    return (nVmSize, nVmRSS)

def inserttable():
    tm = int(time.time())  
    mems = getMemory()

    sql = "insert into memory(time, VmSize, VmRSS) VALUES(:va_time, :VmSize, :VmRSS)"
    print("insert time = %d VmSize = %d VmRSS = %d" %(tm, mems[0], mems[1]))
    g_cursor.execute(sql, {'va_time':tm, 'VmSize':mems[0], 'VmRSS':mems[1]})
    g_conn.commit()

def testData():
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
    # if len(retArray)>0:
        # q_sql_time = retArray[0][-1]


if __name__=='__main__':
    # mems = getMemory()    
    # print(mems)
    createtable()
    g_conn = sqlite3.connect("sqlite.db")
    g_cursor = g_conn.cursor()
    while True:
        time.sleep(1)
        inserttable()

    g_cursor.close()
    g_conn.close()
