import wx


class MyFrame2(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame2, self).__init__(parent, title=title, size=(350, 250))
        self.label_1 = wx.StaticText(self, -1, "label_1", style=wx.ALIGN_RIGHT)
        self.label_2 = wx.StaticText(
            self, -1, "label_2", style=wx.ALIGN_CENTRE)
        self.label_3 = wx.StaticText(self, -1, "label_3")

        self.label_1.SetBackgroundColour(wx.Colour(127, 255, 0))
        self.label_2.SetBackgroundColour(wx.Colour(0, 255, 255))
        self.label_3.SetBackgroundColour(wx.Colour(219, 112, 147))

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.label_1, 1, wx.EXPAND, 0)
        sizer.Add(self.label_2, 1, wx.EXPAND, 0)
        sizer.Add(self.label_3, 1, wx.EXPAND, 0)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()


class MyApp(wx.App):
    def OnInit(self):
        # self.window = Window("Report Helper New", None, wx.ID_ANY, )
        self.window = MyFrame2(None, "Report Helper New")
        self.SetTopWindow(self.window)
        self.window.Show()
        self.window.Center()
        return True


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
