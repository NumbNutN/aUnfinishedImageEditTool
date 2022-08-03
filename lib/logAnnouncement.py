class Log:
    @staticmethod
    def logSavingFile(browser,filepath,filename):
        browser.append("正在保存图片:")
        browser.append("路径："+filepath+'/'+filename+'')
        browser.append("...\n")

    @staticmethod
    def logSavedFile(browser):
        browser.append("保存成功")

