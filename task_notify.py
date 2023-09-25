from PySide2.QtWidgets import QApplication,QMessageBox
from winotify import Notification
from importlib import reload
import datetime
import time
import getpass
import threading
import gazu

def notify():

    # pm弹窗时间周四/周五 5点弹窗,网页是https://kitsu.zuru.cloud/timesheets/
    # at弹窗时间,网页是https://kitsu.zuru.cloud/my-tasks/timesheets：
    # 日报 - 星期1-星期5,每天上午10点半和下午5点各自弹一次,持续10分钟(已填写,则不会触发)
    # 周报 - 周四-周五,每天下午4点半 - 5点,持续20分钟(已填写,则不会触发)

    # 获取当前时间
    now = datetime.datetime.now()
    weekday = now.strftime("%A")

    # 获取当前用户名称
    username = getpass.getuser()
    if username=='lvy':
        launch = 'https://kitsu.zuru.cloud/timesheets'
    else:
        launch = 'https://kitsu.zuru.cloud/my-tasks/timesheets'

    task = f'{weekday} Task'
    daily = r'每日任务'
    message = f"Hi,{username}\n现在是休息时间...\n填写{daily},才能劳逸结合..."
    icon = r"C:/Users/kangwen/Desktop/ZT_Install/logo.ico"

    toast = Notification(app_id=task,
                         title=daily,
                         msg=message,
                         icon=icon,
                         duration='long',
                         launch=launch
                         )

    toast.show()

def timer():
    # 获取当前时间
    # while True:
    #     now = datetime.datetime.now()
    #     hour = now.hour
    #     minute = now.minute
    #
    #     if hour == 15:  # 判断当前时间是否超过下午3点
    #         if minute >= 0 and minute<=10 :
    #             time.sleep(30)
    #             notify()
    #     else:
    #         print(f"Current Time: {now},Connecting...")
    #         time.sleep(60)
    ## update
    git = 'https://github.com/anuos123/task_notify.git'

    import requests

    owner = 'anuos123'
    repo = 'task_notify'
    repo_url = f'https://api.github.com/repos/{owner}/{repo}/tags'
    response = requests.get(repo_url.format(owner=owner, repo=repo))

    if response.status_code == 200:
        tags = response.json()
        for tag in tags:
            print(tag['name'])
    else:
        print('Failed to retrieve tags')

    # # 创建一个带有“问题”图标的问题对话框
    # reply = QMessageBox.question(None, "标题", "这是一个问题对话框。", QMessageBox.Yes | QMessageBox.No)
    # if reply == QMessageBox.Yes:
    #     print("用户点击了“Yes”按钮。")
    # else:
    #     print("用户点击了“No”按钮。")
timer()