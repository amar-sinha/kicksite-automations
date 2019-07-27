import wx, panels

class Program(wx.Frame):
    def __init__(self):
        self.frame = wx.Frame.__init__(self, None, wx.ID_ANY, 'automate')

        sizer = wx.BoxSizer()
        self.SetSizer(sizer)

        self.panel_one = panels.panelMain(self)

        sizer.Add(self.panel_one, 1, wx.EXPAND)

        self.SetSize((960, 540))
        self.Centre()