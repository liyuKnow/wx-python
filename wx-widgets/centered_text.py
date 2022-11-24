import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        self.rootPanel = wx.Panel(self)

        innerPanel = wx.Panel(self.rootPanel, -1,
                              size=(150, 150), style=wx.ALIGN_CENTER)
        innerPanel.SetBackgroundColour('WHITE')
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        innerBox = wx.BoxSizer(wx.VERTICAL)

        # I want this line visible in the CENTRE of the inner panel
        txt = wx.StaticText(innerPanel, id=-1, label="TEXT HERE",
                            style=wx.ALIGN_CENTER, name="")
        # innerBox.AddSpacer((150, 75))
        innerBox.Add(txt, 0, wx.CENTER)
        # innerBox.AddSpacer(size=(150, 75))
        innerPanel.SetSizer(innerBox)

        hbox.Add(innerPanel, 0, wx.ALL | wx.ALIGN_CENTER)
        vbox.Add(hbox, 1, wx.ALL | wx.ALIGN_CENTER, 5)

        self.rootPanel.SetSizer(vbox)
        vbox.Fit(self)


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'wxBoxSizer.py')
        frame.Show(True)
        frame.Center()
        return True


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
