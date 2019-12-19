> 郑重声明：本项目的所有代码和相关文章， 仅用于经验技术交流分享，禁止将相关技术应用到不正当途径，因为滥用技术产生的风险与本人无关。

# :1st_place_medal:Review_Reverse 2019年末逆向复习系列（持续更新）:exclamation:
![](https://github.com/lateautumn4lin/Review_Reverse/blob/master/main.png)

# :family_man_man_girl_boy:前言

马上到2019年末啦！今年接触到的逆向案例还是很多，所以单开个项目给自己复习一下！

# :handshake:使用方式

1. 下载项目

```shell
git clone git@github.com:lateautumn4lin/Review_Reverse.git
```

2. 创建环境并安装依赖

```shell
conda create -n review_reverse python=3.8

. activate review_reverse

pip install -r requirements.txt

npm install express --save
```

3. 运行你想要的项目，例如猫眼电影

```shell
python -m maoyao.test (以模块化运行)
```

# :calendar:目录

- [:page_with_curl:案例分析](#案例分析)
  - [:one: 淘宝:heavy_check_mark:](#1-淘宝)
    - [1.1 WEB淘宝sign参数逆向破解](#1.1-WEB淘宝sign参数逆向破解)
  - [:two: 努比亚:heavy_check_mark:](#2-努比亚)
    - [2.1 努比亚Cookie生成逆向分析](#2.1-努比亚Cookie生成逆向分析)
  - [:three: 百度指数:heavy_check_mark:](#3-百度指数)
    - [3.1 百度指数Data加密逆向破解](#3.1-百度指数Data加密逆向破解)
  - [:four: 今日头条WEB版:heavy_check_mark:](#4-今日头条WEB版)
    - [4.1 今日头条WEB端_signature、as、cp参数逆向分析](#4.1-今日头条WEB端_signature、as、cp参数逆向分析)
  - [:five: 知乎WEB版:heavy_check_mark:](#5-知乎WEB版)
    - [5.1 知乎登录formdata加密逆向破解](#5.1-知乎登录formdata加密逆向破解)
  - [:six: KNN猫眼字体反爬:heavy_check_mark:](#6-KNN猫眼字体反爬)
    - [6.1 从猫眼字体反爬分析谈谈字体反爬的前世今生](#6.1-从猫眼字体反爬分析谈谈字体反爬的前世今生)
  - [:seven: Boss直聘:heavy_check_mark:](#7-Boss直聘)
    - [7.1 Boss直聘Cookie加密字段__zp_stoken__逆向分析](#7.1-Boss直聘Cookie加密字段__zp_stoken__逆向分析)
  - [:eight: pdd:heavy_check_mark:](#8-pdd)
    - [8.1 拼夕夕Web端anti_content参数逆向分析](#8.1-拼夕夕Web端anti_content参数逆向分析)

# 案例分析

## 1 淘宝

## 1.1 WEB淘宝sign参数逆向破解

- **参考文章**：

  - [微信文章：2019年末逆向复习系列之淘宝M站Sign参数逆向分析](https://mp.weixin.qq.com/s?__biz=MzIzOTQzNDIyOA==&mid=100000296&idx=1&sn=bcb858c0b4f8f460d5cd6433965b9339&chksm=692b62b35e5ceba597b830ca4d7451b709c31c2aaa84351888ae7c5d82c68ef740cc53b4eb79&scene=0&xtrack=1&key=a089b840afa72487c5c947dd508eadd32a992303f4ecd2e171ce6677361f96b52daadccce30cb283e1639dffb4aa7b6c8aa6d499d0b1dd2af982b26ffd444c11bd5d07b6fd9c58e822fc2d7e77941498&ascene=1&uin=MjE5NTExNzYxMA%3D%3D&devicetype=Windows+10&version=62070158&lang=zh_CN&pass_ticket=vdb3234iVj%2FTN%2FTiZH4WfOoiCpc5yB%2FlSEc2AQtost8B7g3si%2B4YtP%2Bp6RRNb7Mc)

  - [个人博客文章：2019年末逆向复习系列之淘宝M站Sign参数逆向分析](https://cloudcrawler.club/tao-bao-m-zhan-sign-can-shu-ni-xiang-fen-xi.html)
- **逆向代码**：[WEB 淘宝 sign 参数破解代码](https://github.com/lateautumn4lin/Review_Reverse/blob/master/tb/m_tb.py)
- **实战代码**：[WEB 淘宝爬取代码](https://github.com/lateautumn4lin/Review_Reverse/blob/master/tb/m_tb_example.py)


## 2 努比亚

## 2.1 努比亚Cookie生成逆向分析

- **参考文章**：

  - [微信文章：2019年末逆向复习系列之努比亚Cookie生成逆向分析](https://mp.weixin.qq.com/s?__biz=MzIzOTQzNDIyOA==&mid=2247483980&idx=1&sn=c17b106f84cb8dd2cb88e774723bec75&chksm=e92b62d7de5cebc11f3ece8d458c76c183871b060549e01865c8e4b97ab6ce7ba47337d43a64&token=1415978371&lang=zh_CN#rd)

  - [个人博客文章：2019年末逆向复习系列之努比亚Cookie生成逆向分析](https://cloudcrawler.club/nu-bi-ya-cookie-sheng-cheng-ni-xiang-fen-xi.html)

- **逆向代码**：[努比亚Cookie参数破解代码](https://github.com/lateautumn4lin/Review_Reverse/blob/master/nubia/m_nubia.py)
- **实战代码**：[努比亚论坛爬取代码](https://github.com/lateautumn4lin/Review_Reverse/blob/master/test/test_m_nubia.py)

## 3 百度指数

## 3.1 百度指数Data加密逆向破解

- **参考文章**：

  - [微信文章：2019年末逆向复习系列之百度指数Data加密逆向破解](https://mp.weixin.qq.com/s?__biz=MzIzOTQzNDIyOA==&mid=2247484007&idx=1&sn=42cc87969f7912fdc1a68f5199cb173d&chksm=e92b62fcde5cebea0adb3f7d6bb4da2d848694b9f4f0cd5d69616bf428e7bcfad03a269ef699&token=283044481&lang=zh_CN#rd)

  - [个人博客文章：2019年末逆向复习系列之百度指数Data加密逆向破解](https://cloudcrawler.club/bai-du-zhi-shu-data-jia-mi-ni-xiang-po-jie.html)
  
- **逆向代码**：[百度指数Data加密代码](https://github.com/lateautumn4lin/Review_Reverse/blob/master/baidu/baidu_index/m_baidu_index.py)
- **实战代码**：[百度指数爬取代码](https://github.com/lateautumn4lin/Review_Reverse/blob/master/baidu/baidu_index/m_baidu_index_example.py)

  
## 4 今日头条WEB版

## 4.1 今日头条WEB端_signature、as、cp参数逆向分析

- **参考文章**：

  - [微信文章：2019年末逆向复习系列之今日头条WEB端_signature、as、cp参数逆向分析](https://mp.weixin.qq.com/s?__biz=MzIzOTQzNDIyOA==&mid=2247484012&idx=1&sn=cea8e45ab9b7b67706b1a9b119659ed8&chksm=e92b62f7de5cebe116b86d5859dabfc23389a3f2b47279f6e73c09be64088c658e34f7c3be70&token=283044481&lang=zh_CN#rd)

  - [个人博客文章：2019年末逆向复习系列之今日头条WEB端_signature、as、cp参数逆向分析](https://cloudcrawler.club/jin-ri-tou-tiao-web-duan-signature-as-cp-can-shu-ni-xiang-fen-xi.html)

- **逆向代码**：[今日头条WEB端_signature、as、cp参数加密代码](https://github.com/lateautumn4lin/Review_Reverse/blob/master/toutiao/m_toutiao.py)
- **实战代码**：[今日头条WEB端文章爬取代码](https://github.com/lateautumn4lin/Review_Reverse/blob/master/toutiao/m_toutiao_example.py)


## 5 知乎WEB版

## 5.1 知乎登录formdata加密逆向破解

- **参考文章**：

  - [微信文章：2019年末逆向复习系列之知乎登录formdata加密逆向破解](https://mp.weixin.qq.com/s?__biz=MzIzOTQzNDIyOA==&mid=2247484012&idx=1&sn=cea8e45ab9b7b67706b1a9b119659ed8&chksm=e92b62f7de5cebe116b86d5859dabfc23389a3f2b47279f6e73c09be64088c658e34f7c3be70&token=283044481&lang=zh_CN#rd)

  - [个人博客文章：2019年末逆向复习系列之知乎登录formdata加密逆向破解](https://cloudcrawler.club/zhi-hu-deng-lu-formdata-jia-mi-ni-xiang-po-jie.html)

- **逆向代码**：[知乎登录formdata参数解密代码](https://github.com/lateautumn4lin/Review_Reverse/blob/master/zhihu/m_zhihu.py)
- **实战代码**：[知乎模拟登录代码](https://github.com/lateautumn4lin/Review_Reverse/blob/master/zhihu/m_zhihu_example.py)

## 6 KNN猫眼字体反爬

## 6.1 从猫眼字体反爬分析谈谈字体反爬的前世今生

- **参考文章**：

  - [微信文章：2019年末逆向复习系列之从猫眼字体反爬分析谈谈字体反爬的前世今生](https://mp.weixin.qq.com/s?__biz=MzIzOTQzNDIyOA==&mid=2247484031&idx=1&sn=eff03539c7f593510179202a4d3fe122&chksm=e92b62e4de5cebf21afae6696f1e5f31b361407cc7d88c137412547ffbcfb9446770623c232f&token=699370238&lang=zh_CN#rd)

  - [个人博客文章：2019年末逆向复习系列之从猫眼字体反爬分析谈谈字体反爬的前世今生](https://cloudcrawler.club/cong-mao-yan-zi-ti-fan-pa-fen-xi-tan-tan-zi-ti-fan-pa-de-qian-shi-jin-sheng.html)

- **逆向代码**：[猫眼字体反爬KNN训练代码](https://github.com/lateautumn4lin/Review_Reverse/blob/master/maoyan/knn_test.py)
- **实战代码**：[猫眼字体反爬实战分析](https://github.com/lateautumn4lin/Review_Reverse/blob/master/maoyan/test.py)

## 7 Boss直聘

## 7.1 Boss直聘Cookie加密字段__zp_stoken__逆向分析

- **参考文章**：

  - [微信文章：2019年末逆向复习系列之Boss直聘Cookie加密字段__zp_stoken__逆向分析](https://mp.weixin.qq.com/s?__biz=MzIzOTQzNDIyOA==&mid=2247484031&idx=1&sn=eff03539c7f593510179202a4d3fe122&chksm=e92b62e4de5cebf21afae6696f1e5f31b361407cc7d88c137412547ffbcfb9446770623c232f&token=699370238&lang=zh_CN#rd)

  - [个人博客文章：2019年末逆向复习系列之Boss直聘Cookie加密字段__zp_stoken__逆向分析](https://cloudcrawler.club/boss-zhi-pin-cookie-jia-mi-zi-duan-zp-stoken-ni-xiang-fen-xi.html)

- **逆向代码**：[Boss直聘加密代码](https://github.com/lateautumn4lin/Review_Reverse/blob/master/boss_zp/encrypt.js)
- **实战代码**：[Boss直聘实战分析](https://github.com/lateautumn4lin/Review_Reverse/blob/master/boss_zp/m_boss_zp_example.py)

## 8 pdd

## 8.1 拼夕夕Web端anti_content参数逆向分析

- **参考文章**：

  - [微信文章：2019年末逆向复习系列之拼夕夕Web端anti_content参数逆向分析](https://mp.weixin.qq.com/s?__biz=MzIzOTQzNDIyOA==&mid=2247484031&idx=1&sn=eff03539c7f593510179202a4d3fe122&chksm=e92b62e4de5cebf21afae6696f1e5f31b361407cc7d88c137412547ffbcfb9446770623c232f&token=699370238&lang=zh_CN#rd)

  - [个人博客文章：2019年末逆向复习系列之拼夕夕Web端anti_content参数逆向分析](https://cloudcrawler.club/pin-xi-xi-web-duan-anti-content-can-shu-ni-xiang-fen-xi.html)

- **逆向代码**：[pdd加密服务代码](https://github.com/lateautumn4lin/Review_Reverse/blob/master/pdd/encrypt_server.js)
- **实战代码**：[pdd实战案例代码](https://github.com/lateautumn4lin/Review_Reverse/blob/master/pdd/m_pdd_example.py)

### 项目以及个人立场声明

再次郑重声明：本项目的所有代码和相关文章， 仅用于经验技术交流分享，禁止将相关技术应用到不正当途径，因为滥用技术产生的风险与本人无关。

