# 10min手写一个简易的内存监控系统

[详细博客连接](https://github.com/shengxinjing/my_blog/issues/1)


## 腾讯视频链接
录制中间网出问题了，重启了一下，所以有两部分
* [视频1](http://v.qq.com/boke/gplay/6362f9ed32ee1bc6bcfe344f11a106c5_lyf0000015cvpaj_d0174xh1ft1.html)
* [视频2](http://v.qq.com/boke/gplay/6362f9ed32ee1bc6bcfe344f11a106c5_lyf0000015cvpaj.html)

本文的目的在于，尽可能用简单的代码，让大家了解内存监控的原理
主题思路
* 获取内存信息
* 存储信息
* 展现
* 扩展
    - 加主机名,moitor部署在多台机器，不直接插数据库
    - 通过http请求的方式，一台机器起flask专门存数据monitor




# 简易的内存监控系统

* 获取内存信息
    - 总内存-空闲-缓冲-缓存
    - done
* 存储信息
    - mysql
    - 新建数据库 新建表格（内存 时间）
    - 内存数据入库
    - done
* 展现
    - web选页面
    - 图表展现
        + 假数据先把图画出来
        + python提供真实数据
        + 实时展现
            * Python端能提供增量数据
                - 通过时间戳
            * 前端轮训，动态添加增量数据
* 扩展
    - 加主机名,moitor部署在多台机器，不直接插数据库
    - 通过http请求的方式，一台机器起flask专门存数据monitor
    - 
    - 

