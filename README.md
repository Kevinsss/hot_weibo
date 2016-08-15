# hot_weibo

## Description
Count the top 10 topics of weibo, and send it to mailbox.
## 描述
统计新浪微博热点榜单前10名的话题，转换成文本发送到指定邮箱。

## Environment
	Python: 2.7.*
	System: Windows/Linux/Mac
## 环境
	Python: 2.7.*
	System: Windows/Linux/Mac

## How To Use
1. Setup python
2. Update the email settings in `MailUtil.init()` function(including SMTP server addr, email、password of sender, email of receiver)
3. Run the `hot_weibo.py`.
## 如何使用
1. 配置Python环境
2. 在MailUtil类init函数中配置邮箱信息(包括SMTP服务器，发件人邮箱名、密码，收件人邮箱名)
3. 执行`hot_weibo.py`文件。

## Result
## 结果
![image](https://github.com/Kevinsss/hot_weibo/blob/master/result.png)


