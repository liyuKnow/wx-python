import wx


class Window(wx.Frame):
    def __init__(self, title):
        super().__init__(parent=None, title=title)

        self.panel = wx.Panel(self)

        # FIXED SIZE
        # self.panel = wx.Frame(None, )
        self.SetMaxSize(wx.Size(800, 500))
        self.SetMinSize(wx.Size(800, 500))

        wrapper = wx.BoxSizer(wx.VERTICAL)

        # MAKE FLEX GRID SIZER
        sizer = wx.FlexGridSizer(rows=3, cols=2, vgap=10, hgap=10)

        # ADD WIDGETS
        sizer.AddMany([(wx.StaticText(self.panel, label="Username")),
                       (wx.TextCtrl(self.panel), 0, wx.EXPAND),
                       (wx.StaticText(self.panel, label="Password")),
                       (wx.TextCtrl(self.panel), 0, wx.EXPAND),
                       (wx.StaticText(self.panel, label="Address")),
                       (wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_NO_VSCROLL), 0, wx.EXPAND)])

        # RESIZE AND ALSO AT MAXIMAZING SCREEN
        sizer.AddGrowableCol(1, 1)
        sizer.AddGrowableRow(2, 1)

        # SET SIZER TO PANEL WITH A BOX SIZE WRAPPER
        wrapper.Add(sizer, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        self.panel.SetSizer(wrapper)

        self.Center()


def main():
    app = wx.App()
    window = Window("Test Flex Grid").Show()
    app.MainLoop()


if __name__ == "__main__":
    main()

# class MyApp(wx.App):
#     def OnInit(self):
#         self.frame = Window(None, wx.ID_ANY, "")
#         self.SetTopWindow(self.frame)
#         self.frame.Show()
#         self.frame.Center()
#         return True


# if __name__ == "__main__":
#     app = MyApp(0)
#     app.MainLoop()
