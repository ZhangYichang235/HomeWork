from urllib import parse

# TK 如果出现错误会返回一个消息
import tkinter.messagebox as msgbox

# 做桌面编程的
import tkinter as tk

# 控制浏览器的
import webbrowser

# 正则表达式
import re

class APP:
    # 魔术方法
    # 初始化用的
    def __init__(self, width=500, height=300):
        self.w = width
        self.h = height
        self.title = 'vip视频破解助手'
        # 软件名
        self.root = tk.Tk(className=self.title)

        # vip视频播放地址 StringVar() 定义字符串变量
        self.url = tk.StringVar()

        # 定义选择哪个播放源
        self.v = tk.IntVar()

        # 默认为1
        self.v.set(1)

        # Frame空间
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)

        # 控件内容设置
        group = tk.Label(frame_1, text='暂时只有两个视频播放通道：', padx=10, pady=10)
        tb = tk.Radiobutton(frame_1, text='第 一通道(默认)', variable=self.v, value=1, width=16, height=3)
        lable = tk.Label(frame_2, text='请输入视频连接：')

        # 输入框声明
        entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        play = tk.Button(frame_2, text='播放', font=('楷体', 12), fg='Purple', width=2, height=1, command=self.video_play)

        # 控件布局 显示控件在你的软件上
        frame_1.pack()
        frame_2.pack()

        # 确定控件的位置 wow 行 column 列
        group.grid(row=0, column=0)
        tb.grid(row=0, column=1)

        lable.grid(row=0, column=0)
        entry.grid(row=0, column=1)

        # ipadx x方向的外部填充 ipady y方向的内部填充
        play.grid(row=0, column=3, ipadx=10, ipady=10)

    def video_play(self,):
            # 视频解析网站地址
            port1 = 'https://translate.google.cn/#view=home&op=translate&sl=en&tl=zh-CN&text='
            
            # 拿到用户输入的视频网址
            ip = self.url.get()

            # 视频连接加
            ip = parse.quote_plus(ip)
            # 用浏览器打开网址
            webbrowser.open(port1 + ip)

        
    # 启动GUI程序的函数
    def loop(self):
            self.root.resizable(True, True)
            self.root.mainloop()

if __name__ == "__main__":
    app = APP()
    app.loop()
