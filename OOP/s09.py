# 导入相应的包
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase,MIMEMultipart


# MIMEText 三个主要参数
# 1.邮件内容
# 2.MIME子类型，在此案例我们用plain表示text类型
# 3.邮件编码格式
mail_mul = MIMEMultipart()
mail_text = MIMEText("Hello, i am xxxx","plain","utf-8")

mail_mul.attach(mail_text)
with open("x02.xml","rb") as f:
    s = f.read()
    m = MIMEText(s,"base64","utf-8")
    m["Content-Type"] = "application/octet-stream"
    m["Content-Disposition"] = "attachment;filename='x02.xml'"
    mail_mul.attach(m)

from_addr = "xxxxxxx@qq.com"

from_pwd = "*******"

to_addr = "xxxxxxx@qq.com"

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
    srv.sendmail(from_addr,[to_addr],mail_mul.as_string())

    srv.quit()

except Exception as e:
    print(e)