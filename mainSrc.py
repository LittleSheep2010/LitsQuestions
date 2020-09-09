import os
import time
import sys
import webbrowser

import WareHouse
import ConfigLoader

import PythonSheep.IOSheep.PrintFormat as PrintSheep
import PythonSheep.IOSheep.InputFormat as InputSheep

# 初始化类
mainWareHouse = WareHouse.wareHouse()
mainPrintControler = PrintSheep.PrintFormat()
mainInputControler = InputSheep.InputFormat()

# 读取配置文件
ConfigLoader.LoadConfig(mainWareHouse)

# 输出使用的语言
if mainWareHouse.globalSittings["userLanguage"] == "En":
    mainWareHouse.userUsingLanguage = "En"
    print(" * $ User now use English(%s)" % mainWareHouse.globalSittings["userLanguage"])

elif mainWareHouse.globalSittings["userLanguage"] == "Ch_Sp":
    mainWareHouse.userUsingLanguage = "Ch_Sp"
    print(" * $ 用户现在使用的是简体中文(%s)" % mainWareHouse.globalSittings["userLanguage"])

else:
    mainWareHouse.userUsingLanguage = "En"
    print(" * $ User now use unkown language(%s)" % mainWareHouse.globalSittings["userLanguage"])
    print(" * $ Continue use English(En|English)")

# 获取输入的题目文件
if len(sys.argv) > 1:
    welcomeMode = False
    mainWareHouse.loadingQuestionFileName = sys.argv[1]

# 没有任何输入处理
else:
    welcomeMode = True

    # 输出 Welcome 界面
    if mainWareHouse.globalSittings["showWelcomeMenu"]:
        userNowUsingLanguage = mainWareHouse.userUsingLanguage
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["welcomeMessage"]["welcomeMessage_Title1"])
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["welcomeMessage"]["welcomeMessage_No1"])
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["welcomeMessage"]["welcomeMessage_No2"])
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["welcomeMessage"]["welcomeMessage_No3"])
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["welcomeMessage"]["welcomeMessage_No4"])
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["welcomeMessage"]["welcomeMessage_No5"])
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["welcomeMessage"]["welcomeMessage_No6"])
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["welcomeMessage"]["welcomeMessage_No7"])
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["welcomeMessage"]["welcomeMessage_No8"])
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["welcomeMessage"]["welcomeMessage_No9"])
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["welcomeMessage"]["welcomeMessage_Title2"])
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["welcomeMessage"]["welcomeMessage_No10"])
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["welcomeMessage"]["welcomeMessage_No11"])
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["welcomeMessage"]["welcomeMessage_No12"])
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["welcomeMessage"]["welcomeMessage_No13"])
        del userNowUsingLanguage

    # 不显示 Welcome 界面信息
    else:
        userNowUsingLanguage = mainWareHouse.userUsingLanguage
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["welcomeMessage"]["welcomeMessage_NotShow"])
        del userNowUsingLanguage

    # 处理 Press Enter key continue
    userNowUsingLanguage = mainWareHouse.userUsingLanguage
    input(mainWareHouse.languagesContents[userNowUsingLanguage]["globalMessageTips"]["anyKeyContinue_TipsMessage"])
    # 清屏
    mainPrintControler.UniversalClearScreen()
    del userNowUsingLanguage

    # 控制台
    while True:
        userNowUsingLanguage = mainWareHouse.userUsingLanguage

        # 打印 Console 标题
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["consoleMessage"]["consoleBootTitle"])
        consoleGet = input(mainWareHouse.languagesContents[userNowUsingLanguage]["consoleMessage"]["consoleCommandTips"])

        # 检测的输入的是 Command
        if str(consoleGet).startswith("^"):

            usingCommand = str(consoleGet)



# 切换工作目录
mainWareHouse.defaultWorkDir = os.getcwd()
os.chdir("./QuestionData")

# 检测题目文件是否存在
if not os.path.exists(mainWareHouse.loadingQuestionFileName) and not welcomeMode:
    userNowUsingLanguage = mainWareHouse.userUsingLanguage
    print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileTips"]["questionFileErrorTitle"])
    print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileTips"]["questionFileErrorMessage_No1"])
    print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileTips"]["questionFileErrorMessage_No2"])
    print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileTips"]["questionFileErrorMessage_No3"])
    del userNowUsingLanguage
    sys.exit(1)