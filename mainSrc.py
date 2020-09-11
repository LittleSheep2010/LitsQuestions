import os
import sys
import time

import WareHouse
import ConfigLoader

import PythonSheep.IOSheep.PrintFormat as PrintSheep
import PythonSheep.IOSheep.InputFormat as InputSheep

from Commands.HelpDocument import HelpDocument
from Commands.ReloadConfig import ReloadConfig
from Commands.OpenConfig import OpenConfig

# 初始化类
mainWareHouse = WareHouse.wareHouse()
mainPrintControler = PrintSheep.PrintFormat()
mainInputControler = InputSheep.InputFormat()

# 初始化命令插件
HelpDocumentPlugin = HelpDocument()
ReloadConfigPlugin = ReloadConfig()
OpenConfigPlugin = OpenConfig()

# 读取配置文件
ConfigLoader.LoadConfig(mainWareHouse)

# 保存默认工作目录
mainWareHouse.defaultWorkDir = os.getcwd()

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
    userNowUsingLanguage = mainWareHouse.userUsingLanguage

    # 打印 Console 标题
    print(mainWareHouse.languagesContents[userNowUsingLanguage]["consoleMessage"]["consoleBootTitle"])
    while True:
        consoleGet = input(mainWareHouse.languagesContents[userNowUsingLanguage]["consoleMessage"]["consoleCommandTips"]).upper()

        # 检测的输入的是 Command
        if str(consoleGet).startswith("^"):

            usingCommand = str(consoleGet)

            # 命令处理
            if str(consoleGet) == "^HELP":
                # 运行插件
                HelpDocumentPlugin.run(userNowUsingLanguage, mainWareHouse)

            elif str(consoleGet) == "^RELOAD":
                # 运行插件
                ReloadConfigPlugin.run(userNowUsingLanguage, mainWareHouse)

            elif str(consoleGet) == "^SITTINGS-OPEN":
                # 运行插件
                OpenConfigPlugin.run(userNowUsingLanguage, mainWareHouse)

            elif str(consoleGet) == "^EXIT":
                # 离开
                sys.exit(0)

            else:
                # 未知的命令处理
                print(mainWareHouse.languagesContents[userNowUsingLanguage]["commandsMessage"]["unkownCommand_TipsMessage"]
                      % str(consoleGet))

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

else:
    ConfigLoader.LoadQuestionFile(mainWareHouse, mainWareHouse.loadingQuestionFileName)

    userNowUsingLanguage = mainWareHouse.userUsingLanguage

    # 计算总共分数
    sumScore = 0.0
    for i in range(len(mainWareHouse.userQuestionFile["questions"])):
        sumScore += mainWareHouse.userQuestionFile["questions"][i]["score"]

    # 计算难度
    projectDifficultyTemplate = ["Eazy", "Medium", "Hard", "Hardcore"]
    projectDifficulty = ""
    if len(projectDifficultyTemplate) < mainWareHouse.userQuestionFile["projectDifficulty"]:
        projectDifficulty = "Unkown"
    else:
        projectDifficulty = projectDifficultyTemplate[mainWareHouse.userQuestionFile["projectDifficulty"]]
    del projectDifficultyTemplate

    # 打印 QuestionFile 信息
    print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileMessage"]["infoTitle"])
    print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileMessage"]["infoLanguage"]
          % mainWareHouse.userQuestionFile["language"])
    print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileMessage"]["infoVersion"]
          % mainWareHouse.userQuestionFile["version"])
    print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileMessage"]["infoProjectName"]
          % mainWareHouse.userQuestionFile["projectName"])
    print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileMessage"]["infoTotalScore"]
          % sumScore)
    print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileMessage"]["infoDifficulty"]
          % projectDifficulty)
    print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileMessage"]["questionStartTitle"])
    input(mainWareHouse.languagesContents[userNowUsingLanguage]["globalMessageTips"]["anyKeyContinue_TipsMessage"])

    mainPrintControler.UniversalClearScreen()

    # 开始测试
    userSumScore = 0.0
    for i in range(len(mainWareHouse.userQuestionFile["questions"])):
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileMessage"]["questionCountTitle"]
              % int(i + 1))
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileMessage"]["questionNameTitle"])
        print(mainWareHouse.userQuestionFile["questions"][i]["name"])
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileMessage"]["questionExplanation"])
        for j in range(len(mainWareHouse.userQuestionFile["questions"][i]["explanation"])):
            print(mainWareHouse.userQuestionFile["questions"][i]["explanation"][j])
        answer = input(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileMessage"]["questionAnswer"])

        questionRight = False
        for j in range(len(mainWareHouse.userQuestionFile["questions"][i]["answer"])):
            if answer == mainWareHouse.userQuestionFile["questions"][i]["answer"][j]:
                print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileMessage"]["answerRight"])
                userSumScore += mainWareHouse.userQuestionFile["questions"][i]["score"]
                questionRight = True

            else: continue

        # 这题没有做对
        if not questionRight:
            print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileMessage"]["answerWorng"])
            print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileMessage"]["answerIs"]
                  % str(mainWareHouse.userQuestionFile["questions"][i]["answer"]))

        input(mainWareHouse.languagesContents[userNowUsingLanguage]["globalMessageTips"]["anyKeyContinue_TipsMessage"])
        mainPrintControler.UniversalClearScreen()

    # 综合打印
    print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileMessage"]["returnTitle"])
    print(mainWareHouse.languagesContents[userNowUsingLanguage]["questionFileMessage"]["returnScore"] % userSumScore)
    input(mainWareHouse.languagesContents[userNowUsingLanguage]["globalMessageTips"]["anyKeyContinue_TipsMessage"])
    mainPrintControler.UniversalClearScreen()