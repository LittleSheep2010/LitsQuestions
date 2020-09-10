from Commands.Base import LitsQuestionsCommand

from PythonSheep.FileSheep.AutoOpen import AutoOpen

from WareHouse import wareHouse

class OpenConfig(LitsQuestionsCommand):

    def run(self, userNowUsingLanguage:str, mainWareHouse:wareHouse):

        AutoOpenControler = AutoOpen()

        print(mainWareHouse.languagesContents[userNowUsingLanguage]["commandsMessage"]["openConfig"]["opening_TipsMessage"])
        AutoOpenControler.UniversalFileOpen_App("./Config/GlobalSittings.json")

        # 处理 Press Enter key continue
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["commandsMessage"]["openConfig"]["openComplete_TipsMessage"])
        input(mainWareHouse.languagesContents[userNowUsingLanguage]["globalMessageTips"]["anyKeyContinue_TipsMessage"])
