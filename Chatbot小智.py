from tkinter import *
import time

import robot

def msgsend(robots):
    result=''

    msg = '我:' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n'
    # print(msg)
    txt_msglist.insert(END, msg, 'green')  # 添加时间
    query = txt_msgsend.get('0.0', END).rstrip('\n') 

    result = robots.send[robots.item](query)

    txt_msglist.insert(END, txt_msgsend.get('0.0', END))  # 获取发送消息，添加文本到消息列表
    txt_msglist.insert(END, '\n')
    txt_msgsend.delete('0.0', END)  # 清空发送消息
    robot = '小智:' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n'
    txt_msglist.insert(END, robot, 'red')
    print(result)
    txt_msglist.insert(END, result + '\n')

'''定义取消发送 消息 函数'''
def cancel():
    txt_msgsend.delete('0.0', END)  # 取消发送消息，即清空发送消息

'''绑定Enter键'''




if __name__=="__main__":

    robots = robot.Robot()


    def msgsendEvent(event):
        if event.keysym == 'Return':
            msgsend(robots)
    tk = Tk()
    tk.title('聊天窗口')

    #创建分区
    f_msglist = Frame(height=300, width=300)  # 创建<消息列表分区 >
    f_msgsend = Frame(height=300, width=300)  # 创建<发送消息分区 >
    f_floor = Frame(height=100, width=300)  # 创建<按钮分区>
    f_right = Frame(height=700, width=100)  # 创建<图片分区>
    #创建控件
    txt_msglist = Text(f_msglist)  # 消息列表分区中创建文本控件
    txt_msglist.tag_config('green', foreground='blue')  # 消息列表分区中创建标签
    txt_msglist.tag_config('red', foreground='red')  # 消息列表分区中创建标签
    txt_msgsend = Text(f_msgsend)  # 发送消息分区中创建文本控件
    txt_show = Text(f_msglist)  # 消息列表分区中创建文本控件
    txt_show.tag_config('red', foreground='red')  # 消息列表分区中创建标签
    txt_showsend = Text(f_msgsend)  # 发送消息分区中创建文本控件

    txt_msgsend.bind('<KeyPress-Return>', msgsendEvent)  # 发送消息分区中，绑定‘Return’键与消息发送。

    button_send = Button(f_floor, text='Send', command=msgsend)  # 按钮分区中创建按钮并绑定发送消息函数
    button_cancel = Button(f_floor, text='Cancel', command=cancel)  # 分区中创建取消按钮并绑定取消函数

    #分区布局
    f_msglist.grid(row=0, column=0)  # 消息列表分区
    f_msgsend.grid(row=1, column=0)  # 发送消息分区
    f_floor.grid(row=2, column=0)  # 按钮分区
    f_right.grid(row=0, column=1, rowspan=3)  # 图片显示分区
    txt_msglist.grid()  # 消息列表文本控件加载
    txt_msgsend.grid()  # 消息发送文本控件加载
    button_send.grid(row=0, column=0, sticky=W)  # 发送按钮控件加载
    button_cancel.grid(row=0, column=1, sticky=W)  # 取消按钮控件加载

    result = '你好！我是机器人小智,输入后按回车键即可发送消息。回复1可开始聊天，回复2可查天气，回复3可讲笑话，回复4可玩成语接龙游戏！'
    robot = '小智:' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) + '\n'
    txt_msglist.insert(END, robot, 'red')
    txt_msglist.insert(END, result + '\n')

    msgsend(robots)
    jump=False
    tk.mainloop()


