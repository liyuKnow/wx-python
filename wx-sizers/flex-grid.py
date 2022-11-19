import wx


class Window(wx.Frame):
    def __init__(self, title):
        super().__init__(parent=None, title=title)

        self.panel = wx.Panel(self)

        # SELECT SIZER
        sizer = wx.FlexGridSizer(rows=3, cols=2, vgap=5, hgap=6)

        sizer.AddMany()


def main():
    app = wx.app
    window = Window("Test Flex Grid")


if __name__ == "__main__":
    main()
