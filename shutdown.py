#/usr/bin/env pathon3
#-*- coding: utf-8 -*-
# @Author: UrAir
# @Date: 2018-01-16 00:50:50
import os, sys, time

# 关机代码调用系统 shutdown 命令 并添加了 -f 参数
# 所以请确保关键程序都已关闭 以防数据丢失
def shutdown(seconds):
    length = len(str(seconds))
    while seconds:
        print('关机时间剩余 {0:<{1}} 秒(中断退出: CTRL + C)'.format(seconds,length), end='\r')
        time.sleep(1)
        seconds -= 1
    print('关闭计算机中........拜拜!',' '*10)
    # 真实使用时请把下面语句的注释符号删除
    # os.system('shutdown -s -f -t 0')

# 判断字符串是否是小数
def isfloat(string):
    try:
        float(string)
        return True
    except Exception:
        return False

# 对用户输入预处理
def input_time():
    while True:
        T = input('多少小时后关闭电脑?(单位:小时)[退出请直接"回车"]>>> ')
        if not T:
            sys.exit()
        elif T.isdigit():
            return int(T) * 3600
        elif isfloat(T):
            return int(float(T) * 3600)
        else:
            print('不是数字,请重新输入!', end='\n\n')

# 运行中 捕捉 中断信号 退出程序
def main():
    sec = input_time()
    try:
        shutdown(sec)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
