# Hot_weibo

## Description
Count the top 10 of weibo, and send it to your mailbox. You can also create a cron job for this program.

## Environment
	Python: 2.7.*
	System: Windows/Linux/Mac

## How To Use
1. Setup python
2. Update the email settings in `MailUtil.init` function(including SMTP server's addr: `self.mail_host`, email: `self.mail_user`、password of sender: `self.mail_pass`, email of receiver: `self.to`)
3. Run the `hot_weibo.py`.

---------------------------------------------------------------------------------------
## 描述
统计新浪微博热点榜单前10名的话题，以文本形式发送到你的邮箱。可以设置成定时任务。

## 环境
	Python: 2.7.*
	System: Windows/Linux/Mac

## 如何使用
1. 配置Python环境
2. 在`MailUtil.init`函数中配置邮箱信息(包括SMTP服务器: `self.mail_host`，发件人邮箱: `self.mail_user`、密码: `self.mail_pass`，收件人邮箱列表: `self.to`)
3. 执行`hot_weibo.py`文件。

## Result
## 结果
![image](https://github.com/Kevinsss/hot_weibo/blob/master/result.png)


