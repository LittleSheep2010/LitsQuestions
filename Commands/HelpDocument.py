from Commands.Base import LitsQuestionsCommand

from WareHouse import wareHouse

import webbrowser
import PythonSheep.IOSheep.PrintFormat

class HelpDocument(LitsQuestionsCommand):

    def run(self, userNowUsingLanguage:str, mainWareHouse:wareHouse):
        mainPrintControler = PythonSheep.IOSheep.PrintFormat.PrintFormat()

        print(mainWareHouse.languagesContents[userNowUsingLanguage]["commandsMessage"]["helpDocument"]["helpDocumentTitle1"])
        print(mainWareHouse.languagesContents[userNowUsingLanguage]["commandsMessage"]["helpDocument"]["helpDocumentNo1"])
        webbrowser.open(mainWareHouse.globalSittings["helpDocumentWebUrl"])
        input(mainWareHouse.languagesContents[userNowUsingLanguage]["globalMessageTips"][
                  "anyKeyContinue_TipsMessage"])
        mainPrintControler.UniversalClearScreen()