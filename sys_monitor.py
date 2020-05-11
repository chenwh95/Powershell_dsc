#!/usr/bin/python3
import psutil
import datetime
import yagmail

def sys_monitor():

    #定义变量保存CPU的使用率
    cpu_per = psutil.cpu_percent(interval=0.5)
    cpu_num = psutil.cpu_count(logical=False)
    #定义变量保存内存的信息
    mem_total = psutil.virtual_memory().total/1024/1024/1024
    mem_per = psutil.virtual_memory().percent
    #定义变量保存硬盘信息
    disk_total = psutil.disk_usage("/").total/1024/1024/1024
    disk_per = psutil.disk_usage("/").percent
    #定义变量保存网络信息
    net_sent = psutil.net_io_counters().bytes_sent/1024/1024/1024
    net_recv = psutil.net_io_counters().bytes_recv/1024/1024/1024

    #获取系统当前时间(年月日，时分秒)
    cur_time = datetime.datetime.now().strftime("%F %T")

    #拼接字符串显示
    log_str = "|----------------------------|---------------------------|-------------------------------|--------------------------------|-----------------------------------|\n"
    log_str += "         监控时间                   CPU使用率(%d核)              内存使用率(共:%.2fG)              硬盘使用率(共:%.2fG)                  网络收发量      \n" % (cpu_num,mem_total,disk_total)
    log_str += "|----------------------------|---------------------------|-------------------------------|--------------------------------|-----------------------------------|\n"
    log_str += "     %s               %s%%                          %s%%                            %s%%                  收：%.2fG/发：%.2fG      \n" % (cur_time,cpu_per,mem_per,disk_per,net_recv,net_sent)
    content = "监控时间: %s\n" % cur_time
    content += "cpu使用率(%d核): %s%%\n" % (cpu_num,cpu_per)
    content += "内存使用率(共:%.2fG): %s%%\n" % (mem_total,mem_per)
    content += "硬盘使用率(共:%.2fG): %s%%\n" % (disk_total,disk_per)
    content += "网络收发量: 收：%.2fG/发：%.2fG\n" % (net_recv,net_sent)
    print(log_str)
    #保存监控信息到日志文件
    with open("system_monitor.txt","a") as f:
        f.write(log_str + "\n")
        # 导入模块
        # 使用yagmail的类创建对象（发件人，授权码，发件服务器）
        # 使用yagmail对象发送邮件（指定收件人，邮件主题，发送内容）

        # 发件人：ww344484614@163.com
        # 授权码：bonnie123
        # 发件服务器：smtp.163.com
        yag = yagmail.SMTP(user="ww344484614@163.com", password="bonnie123", host="smtp.163.com")

        # 发送的内容
        #content = "你好"

        yag.send("344484614@qq.com", "SS_VPN_Singapore服务器监控报告", content)

if __name__ == '__main__':
    sys_monitor()
