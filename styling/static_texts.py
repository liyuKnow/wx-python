import wx


class Window(wx.Frame):
    def __init__(self, title):
        super().__init__(parent=None, title=title, size=(420, 300))
        self.panel = wx.Panel(self)

        wx.StaticLine(self.panel, pos=(20, 240),
                      size=(360, 1), style=wx.HORIZONTAL)

        content1 = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Vestibulum facilisis consequat tellus quis consectetur'''

        content2 = '''Quisque pretium venenatis interdum'''

        text1 = wx.StaticText(self.panel, label=content1, pos=(60, 100))
        text1.SetBackgroundColour("#cecece")
        text2 = wx.StaticText(self.panel, label=content2, pos=(60, 160))

        wx.StaticLine(self.panel, pos=(20, 20), size=(
            360, 1), style=wx.LI_HORIZONTAL)

        self.Centre()
        self.Show()


app = wx.App()
window = Window("WxPython Tutorial")
app.MainLoop()
