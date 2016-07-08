---
title: 东风 开放 API 3.0

language_tabs:
  - shell

toc_footers:
  - <a href=''>控制台</a>

includes:
  - errors

search: true
---

# 介绍

欢迎使用 东风 开放 API 3.0


# 认证

1. 使用access token 访问api
access token 可以让您直接使用API。
您可以在http的header中传入Authorization。`Authorization: ACCESS-TOKEN`


# 微信扫码登陆 wechat

## 获取二维码

```shell
curl "http://dongfeng-demo-dongfeng-proxy.daoapp.io/wechat/get_qrcode"
  -H "Authorization: <my token>"
```

> 返回结果如下:

```json
{
  "url": "https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=gQGm8DoAAAAAAAAAASxodHRwOi8vd2VpeGluLnFxLmNvbS9xL3hFUlhnZzdtZnhJRzluQUxXMnJRAAIE9xb6VgMEgDoJAA==",
  "scene_id": 500853458
}
```

获取登陆用的二维码

### HTTP 请求

`GET http://dongfeng-demo-dongfeng-proxy.daoapp.io/wechat/get_qrcode`

### 返回结果

字段 | 描述
--------- | -----------
url | 二维码的链接，直接访问即可获取二维码图片
scene_id | 场景id，与二维码唯一对应


## 查询登陆状态

```shell
curl "http://dongfeng-demo-dongfeng-proxy.daoapp.io//wechat/get_status?timeout=3"
  -H "Authorization: <my token>"
```

> 返回结果如下:

```json
{
  "username": "hc",
  "open_id": "oFCVevyQOfkurqhoG3-8qkVPkTwer"
}
```

查询用户登陆状态。若timeout时间内用户为扫码登陆，则返回404；若用户已扫码登陆，则返回用户信息。

### HTTP 请求

`GET http://dongfeng-demo-dongfeng-proxy.daoapp.io/wechat/get_status?timeout=3`


### 参数

字段 | 描述
--------- | -----------
timeout | 超时时间

### 返回结果

字段 | 描述
--------- | -----------
username | 用户姓名
open_id | 用户微信id


# 网盘服务 wangpan

## 获取网盘文件列表

```shell
curl "http://dongfeng-demo-dongfeng-proxy.daoapp.io/qiniu/v1/list?bucket=sctlee"
  -H "Authorization: <my token>"
```

> 返回结果如下:

```json
{
  "items": [
    {
      "mimeType": "video/mp4",
      "hash": "luKej5MEP1ZIGlJHy-av1n3H3W2P",
      "url": "http://7xrnqo.com1.z0.glb.clouddn.com//natural.mp4",
      "fsize": 20773164,
      "key": "natural.mp4",
      "putTime": 14587277736819467
    }
  ]
}
```

获取网盘文件列表

### HTTP 请求

`GET http://dongfeng-demo-dongfeng-proxy.daoapp.io/qiniu/v1/list?bucket=sctlee`

### 参数

字段 | 描述
--------- | -----------
bucket | 网盘文件夹名称

### 返回结果

字段 | 描述
--------- | -----------
items | 文件列表
mimeType | 文件类型
hash | 文件hash值
url | 文件公开访问的url
fsize ｜ 文件大小
key | 文件名称
putTime | 上传时间


# 天气服务 weather

## 查询天气

```shell
curl "http://dongfeng-demo-dongfeng-proxy.daoapp.io/weather?q=Shanghai&units=metric"
  -H "Authorization: <my token>"
```

> 返回结果如下:

```json
{
  "coord": {
    "lon": 121.46,
    "lat": 31.22
  },
  "weather": [
    {
      "id": 800,
      "main": "Clear",
      "description": "clear sky",
      "icon": "01d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 295.62,
    "pressure": 1018,
    "humidity": 27,
    "temp_min": 295.15,
    "temp_max": 296.15
  },
  "visibility": 10000,
  "wind": {
    "speed": 3,
    "deg": 230
  },
  "clouds": {
    "all": 0
  },
  "dt": 1459229400,
  "sys": {
    "type": 1,
    "id": 7452,
    "message": 0.0149,
    "country": "CN",
    "sunrise": 1459201583,
    "sunset": 1459246300
  },
  "id": 1796236,
  "name": "Shanghai",
  "cod": 200
}
```

查询天气情况

### HTTP 请求

`GET http://dongfeng-demo-dongfeng-proxy.daoapp.io/weather?q=Shanghai&units=metric`

### 参数

字段 | 描述
--------- | -----------
q | 查询城市名
units | 天气单位（Kelvin, metric）

### 返回结果

字段 | 描述
--------- | -----------
coord | 坐标
weather | 天气概况
base | 内部参数
main | 天气详情
main.temp | 天气温度
main.pressure | 大气压强
main.humidity | 湿度
main.temp_min | 最低温度
main.temp_max | 最高温度
visibility | 可见度
wind | 风力
clouds | 云
dt | 数据计算的时间
sys | 系统参数
id | 城市id
name | 城市名
cod | 内部参数
