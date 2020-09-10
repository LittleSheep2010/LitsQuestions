from WareHouse import wareHouse

from Commands.Base import LitsQuestionsCommand

import ConfigLoader

class ReloadConfig(LitsQuestionsCommand):

    def run(self, userNowUsingLanguage:str, mainWareHouse:wareHouse):

        print(mainWareHouse.languagesContents[userNowUsingLanguage]["commandsMessage"]["reloadConfig"]["reloading_TipsMessage"])
        ConfigLoader.LoadConfig(mainWareHouse)

        # 处理 Press Enter key continue
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["commandsMessage"]["reloadConfig"]["reloadComplete_TipsMessage"])
        input(mainWareHouse.languagesContents[userNowUsingLanguage]["globalMessageTips"]["anyKeyContinue_TipsMessage"])