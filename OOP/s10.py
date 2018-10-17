# 导入相应的包
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# MIMEText 三个主要参数
# 1.邮件内容
# 2.MIME子类型，在此案例我们用plain表示text类型
# 3.邮件编码格式

msg = MIMEText("Hello, i am xxxx","plain","utf-8")

header_from = Header("从图灵学院发送出去的","utf-8")
msg["From"] = header_from

header_to = Header("去某某地方的","utf-8")
msg["To"] = header_to

header_subject = Header("这是主题","utf-8")
msg["Subject"] = header_subject


from_addr = "xxxxxxx@qq.com"

from_pwd = "********"

to_addr = "xxxxxx@qq.com"

#SMTP服务器地址
smtp_srv = "smtp.qq.com"

try:
    #两个参数
    #第一个是服务器地址，但需要是bytes格式，所以需要编码
    #第二个参数是服务器的接受访问端口，465是安全的ssl的端口
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465) #SMTP协议默认端口25,SMTP_SSL是加密的SMTP协议
    #登陆邮箱
    srv.login(from_addr,from_pwd)
    #发送邮件
    #三个参数
    #1.发送地址
    #2.接收地址，必须是list格式
    #3.发送内容，作为字符串发送
    srv.sendmail(from_addr,[to_addr],msg.as_string())

    srv.quit()

except Exception as e:
    print(e)