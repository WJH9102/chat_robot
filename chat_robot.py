#!/usr/bin/env/ python3
# _*_ coding: utf-8 _*_
"""
项目描述：基于微信公众号实现AI客服
作者：WJH
邮箱：1602526012@qq.com
"""

from urllib import request
from urllib import parse


def get_robot_reply(question):
    """
    函数功能：对于特定问题进行特定回复，对于非特定问题进行智能回复
    :param question: 聊天内容会问题
    :return: str， 回复内容
    """
    if "你叫什么名字" in question:
        answer = "我叫wjh"
    elif "你多少岁" in question:
        answer = "18"
    elif "你是GG还是MM" in question:
        answer = "你猜"
    elif "我还有多少钱" in question:
        answer = "没啦"
    else:
        try:
            # 调用NLP接口实智能回复
            params = parse.urlencode({"msg": question}).encode()
            req = request.Request("http://api.itmojun.com/chat_robot", params, method="POST")  # 创建请求
            r = request.urlopen(req).read()  # 调用接口 想目标服务器发出HTTP请求， 并获取响应
            # print(type(answer))
            answer = r.decode()
        except Exception as e:
            answer = "AI机器人出现故障了{}".format(e)
            # print(e)

    return answer

if __name__ == '__main__':

    while True:
        content = input("我说：\n")
        if content == "退出":
            print("bye!")
            break
        print("机器人说：{}".format(get_robot_reply(content)))

# 武汉今天天气怎么样
