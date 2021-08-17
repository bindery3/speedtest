# 简介

使用 speedtest-cli 测速，并通过一个简单的 Flask 服务器返回 JSON 结果。

## 身份验证

由于使用了 HTTPBasicAuth 进行身份验证，启动时需要指定用户名和密码。

## 使用方法

### 部署

1. 直接运行

   ```
   python main.py username password
   ```

2. Docker

   ```
   docker run -d \
       --name speedtest \
       -e USERNAME=username \
       -e PASSWORD=password \
       -p 8000:8000 \
       --restart always \
       bindery/speedtest
   ```

3. Docker-compose

   ```
   version: "3"
   services:
     speedtest:
       image: bindery/speedtest
       container_name: speedtest
       environment:
         - USERNAME=username
         - PASSWORD=password
       ports:
         - 8000:8000
       restart: always
   ```

   ```
   docker-compose up -d
   ```

### 测速

访问 http://ip:8000

```
curl -u username:password -i -X GET http://ip:8000
```

### 结果示例

```
{
    "download": "888.66 Mbps",
    "img": "http://www.speedtest.net/result/11894429150.png",
    "ping": "2 ms",
    "upload": "1164.64 Mbps"
}
```

## Docker 镜像支持的架构

|    OS/ARCH     |
| :------------: |
|  linux/amd64   |
| linux/arm64/v8 |

