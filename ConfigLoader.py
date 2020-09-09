from PythonSheep.SheepJson import JsonLoader, JsonWareHouse

from WareHouse import wareHouse

def LoadConfig(mainWareHouse:wareHouse):

    # 初始化工具
    JsonLoaderTool = JsonLoader.JsonLoader()
    JsonMainWareHouse = JsonWareHouse.JsonWareHouse()

    # 读取全局配置文件
    # 读取文件并保存 SaveID
    mainWareHouse.documentSaveID["globalConfigSaveID"] = JsonLoaderTool.LoadJsonFile("./Config/GlobalSittings.json",
                                                                    CommitWareHouse_JsonWareHouse=JsonMainWareHouse,
                                                                    AutoSave=True)
    # 处理数据
    mainWareHouse.globalSittings = JsonLoaderTool.ProcessJsonContents(JsonMainWareHouse, mainWareHouse.documentSaveID["globalConfigSaveID"])

    # 读取语言文件
    # 读取英文语言文件
    # 读取文件并保存 SaveID
    mainWareHouse.documentSaveID["languageEnSaveID"] = JsonLoaderTool.LoadJsonFile("./Languages/En.json",
                                                                    CommitWareHouse_JsonWareHouse=JsonMainWareHouse,
                                                                    AutoSave=True)
    # 处理数据
    mainWareHouse.languagesContents["En"] = JsonLoaderTool.ProcessJsonContents(JsonMainWareHouse, mainWareHouse.documentSaveID["languageEnSaveID"])

    # 读取简体中文语言文件
    # 读取文件并保存 SaveID
    mainWareHouse.documentSaveID["languageCh_SpSaveID"] = JsonLoaderTool.LoadJsonFile("./Languages/Ch_Sp.json",
                                                                                   CommitWareHouse_JsonWareHouse=JsonMainWareHouse,
                                                                                   AutoSave=True)
    # 处理数据
    mainWareHouse.languagesContents["Ch_Sp"] = JsonLoaderTool.ProcessJsonContents(JsonMainWareHouse,
                                                                               mainWareHouse.documentSaveID[
                                                                                   "languageCh_SpSaveID"])