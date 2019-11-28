#!/usr/bin/python
import configparser, json



if __name__ == "__main__":
    cf = configparser.ConfigParser()
    cf.read('./config.ini')
    mylist = cf.get("sys_config", "mylist")
    print(mylist, type(mylist), repr(mylist))
    # 解析原始变量信息（去掉“”）
    new_list = json.loads(mylist)
    print(new_list, type(new_list), repr(new_list))
    # path信息，直接就可以使用了
    path = cf.get("sys_config", "path")
    print(path, type(path), repr(path))
