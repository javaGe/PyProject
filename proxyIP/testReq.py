from proxyIP import Req


if __name__ == '__main__':
    req = Req.request  # 获取请求实例
    html = req.get('www.baidu.com', 10)
    print(html)