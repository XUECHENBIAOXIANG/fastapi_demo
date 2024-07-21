# fastapi_demo

一个连接了mysql数据库的fastapi接口实现，很简单只有学生信息的接口。

使用起来只需要修改`database.py`里的

```
DATABASE_URL = "mysql+mysqlconnector://username:password@host:port/dbname"
```

修改成你的数据库信息即可。也可以换别的数据库与加各种验证啥的。具体可以参考

# [FastAPI入门教程](https://www.cnblogs.com/leiziv5/p/15416978.html)