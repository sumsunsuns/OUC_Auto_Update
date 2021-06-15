# OUC_Auto_Update

中国海洋大学每日自动上报脚本

![img](https://tva1.sinaimg.cn/large/008i3skNgy1grja45z8ecj30ku0akwf8.jpg)

## 免责声明

- 本项目仅用于交流学习，**请勿使用该项目瞒报谎报疫情消息**。由此造成的后果本人概不负责。
- 疫情防控，人人有责。

## 上报方式

- 使用python脚本+Github Action的功能实现每日定时自动上报，再结合sever酱实现上报结果微信通知

- 由于海大每日上报系统貌似关闭了学号密码的登陆方式（反正我死活没登陆上去），所以只能使用抓企业微信和上报平台之间的包的方式来确定登陆凭证，这里只要找到这个`eai-sess`即可，作为cookie发包就可以成功上报

- 上报的内容来自于`form_data`同样需要抓包获取，里面包含填写的各种信息，也可以抓下来随时修改。

- `form_data`、`eai-sess`、以及sever酱接收消息使用的`sendkey`，都作为github的secret在项目中设置即可

  

## 如何使用

1. fork本项目到自己账户
2. 抓包找到自己的`eai-sess`和`form_data` (这里我使用charles在电脑上抓了企业微信的包)

3. 配置sever酱，获得sendkey，[使用连接](https://sct.ftqq.com/)

4. 设置自己的项目中的secret（回到项目页面，依次点击`Settings`-->`Secrets`-->`New secret`），secret设置的是时候名称必须为以下三个，不能有错

   `LOGINKEY` -> 抓包登陆cookie中eai-sess的内容

   `FORM_DATA`  -> 抓到包中form _data的内容

   `SENDKEY` -> sever酱的通信密钥

![image-20210615215727401](https://tva1.sinaimg.cn/large/008i3skNgy1grjau3a3x1j31g00eqdh2.jpg)

5. 在github action 中手动执行一次运行，成功的话sever酱应该会收到消息了，然后坐等每天自己报就行了。

6. 默认设置的是utc事件0:01分执行脚本，北京时间的话就是早上8点，但是github action 的不准时原因，一般在早上8-10点的时候就可以收到上报成功的消息了。

   大致效果如下：

<img src="https://tva1.sinaimg.cn/large/008i3skNgy1grjav65d5pj30ku1947ak.jpg" alt="image-20210615220317247" style="zoom:25%;" />

## 其他使用方法

- iphone：pythonisa + 捷径，每天喊siri：“每日上报”，从而增加虚无的科幻感。
- 其他使用方式请自行开发

## 问题

1. cookie过期怎么办？
   - 我本以为登陆cookie会过期，可能隔一段时间就要重新抓包得到新的cookie，没想到结果却是意外坚挺….我已经测试了大概两个月还没有过期，所以可以放心使用。

## 有趣的事

- 贵校竟与BUAA使用了同一家公司的上报系统….无意间发现，故而参考了其 [项目](https://github.com/windiboy/BUAAAutoUpdate)。不过貌似钱没给够？怎么还区别对待了呢？[OUC](https://pingan.ouc.edu.cn/uc/wap/login) ，[BUAA](https://app.buaa.edu.cn/uc/wap/login)

  ![image-20210615221802794](https://tva1.sinaimg.cn/large/008i3skNgy1grjbaj2399j31120u044i.jpg)