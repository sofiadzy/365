import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        m, s = divmod(seconds, 60)
        timer = "{:02d}:{:02d}".format(m, s)
        print(timer, end="\r")  # 将计时器显示在同一行上
        time.sleep(1)
        seconds -= 1
    print("时间到！")

# 设置专注时长为25分钟
countdown(25)
