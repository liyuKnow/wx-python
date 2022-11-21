import wx
from logic import feedbackFont

class BottomPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, size=(790, 180))
        self.SetBackgroundColour(wx.Colour(41, 41, 41))

        # SET UP FLEX SIZER FOR PANEL
        wrapper = wx.BoxSizer(wx.VERTICAL)

        # MAKE LAYOUT (1x1)
        sizer = wx.FlexGridSizer(rows=1, cols=2, vgap=10, hgap=10)

        # DEFINE WIDGETS
        conn_btn = wx.Button(
            self, label="Test Connection", size=(120, 40))

        conn_feedback = wx.StaticText(self, label="No Devices Are Connected")
        conn_feedback.SetFont(feedbackFont())

        # ADD WIDGETS TO SIZER
        sizer.AddMany([conn_btn,
                       (conn_feedback, 0, wx.EXPAND), ])

        # RESIZE AND ALSO AT MAXIMAZING SCREEN (FLEX GROW)
        sizer.AddGrowableCol(1, 1)

        # SET SIZER TO PANEL WITH A BOX SIZE WRAPPER
        wrapper.Add(sizer, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        self.SetSizer(wrapper)
