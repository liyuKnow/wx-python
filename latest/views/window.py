import wx

from .panels import *


class Window(wx.Frame):
    def __init__(self, parent, title):
        super(Window, self).__init__(parent, title=title, size=(350, 250))

        self.SetBackgroundColour(wx.Colour("#e2e2e2"))
        # SET FINAL WINDOW SIZE
        self.SetMaxSize(wx.Size(830, 590))
        self.SetMinSize(wx.Size(830, 590))

        # SET UP FLEX SIZER FOR PANEL
        wrapper = wx.BoxSizer(wx.VERTICAL)

        # MAKE LAYOUT (3x1)
        sizer = wx.FlexGridSizer(rows=3, cols=1, vgap=10, hgap=10)

        # DEFINE WIDGETS
        top_Panel = TopPanel(self)
        middle_Panel = MiddlePanel(self)
        bottom_Panel = BottomPanel(self)

        # ADD WIDGETS TO SIZER
        sizer.AddMany([
            top_Panel,
            middle_Panel,
            bottom_Panel
        ])

        # RESIZE AND ALSO AT MAXIMAZING SCREEN (FLEX GROW)
        # sizer.AddGrowableCol(1, 1)

        # SET SIZER TO PANEL WITH A BOX SIZE WRAPPER
        wrapper.Add(sizer, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        self.SetSizer(wrapper)

        self.Show()
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.Center()

    def OnCloseWindow(self, e):
        dial = wx.MessageDialog(
            None,
            "Are you sure you want to quit?",
            "Question",
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION
        )

        ret = dial.ShowModal()

        if ret == wx.ID_YES:
            self.Destroy()
        else:
            print(e)
