import wx
from views import Window


class MyApp(wx.App):
    def OnInit(self):
        # self.window = Window("Report Helper New", None, wx.ID_ANY, )
        self.window = Window(None, "Report Helper New")
        self.SetTopWindow(self.window)
        self.window.Show()
        self.window.Center()
        return True


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
