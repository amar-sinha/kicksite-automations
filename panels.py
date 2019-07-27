import wx, os, ntpath
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

class panelMain(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        title = 'automate'

        png = wx.Image('images/logo.png')
        png.Rescale(300, 80)
        logo = wx.Bitmap(png)
        wx.StaticBitmap(self, -1, logo, (340, 100), style=wx.BITMAP_TYPE_PNG)

        downloadBtn = wx.Button(self, -1, "Download CSV", (410, 205))
        downloadBtn.Bind(wx.EVT_BUTTON, self.onDownloadBtnPress)

        filePicker = wx.FilePickerCtrl(self, -1, pos=(410, 235), wildcard="CSV Files (*.csv)|*.csv|")
        self.Bind(wx.EVT_FILEPICKER_CHANGED, self.OnPickFileDir, filePicker)
        self.filePath = ''

        sortBtn = wx.Button(self, -1, "Sort File", (410, 285))
        sortBtn.Bind(wx.EVT_BUTTON, self.onSortBtnPress)

    def onSortBtnPress(self, event):
        data = pd.read_csv(self.filePath)[['Id','First Name', 'Last Name', 'Belt Size', 'Programs', 'Current Ranks']]
        dfToList = data['Current Ranks'].tolist()

        for rank in dfToList:
            string = str(rank)
            if ',' in string:
                print(string[:string.index(',')])
                # rank = string[:string.index(',')]
        # print(dfToList)

    def OnPickFileDir(self, evt):
        self.filePath = str(evt.GetPath())
        print("You chose: %s\n" % self.filePath)
        # filename = path_leaf(evt.GetPath())
        # print(str(filename))

    def onDownloadBtnPress(self, event):
        usernameStr = 'username'
        passwordStr = 'password'

        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(('https://schoolname.kicksite.net/login'))

        username = browser.find_element_by_id('username')
        username.send_keys(usernameStr)
        password = browser.find_element_by_id('password')
        password.send_keys(passwordStr)
        loginBtn = browser.find_element_by_name('commit')
        loginBtn.click()

        browser.get(('https://schoolname.kicksite.net/students/active.csv'))
