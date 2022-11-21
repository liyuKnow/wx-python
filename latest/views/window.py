import wx

from .panels import *


# class Window(wx.Frame):
#     def __init__(self, title, *args, **kwds, ):
#         kwds["style"] = kwds.get("style", 0)
#         wx.Frame.__init__(self, *args, **kwds)

#         self.title = title

#         self.SetSize((800, 500))

#         # Creating the custom title bar
#         self.panelTitleBar = wx.Panel(self, wx.ID_ANY)
#         self.btnMinimize = wx.Button(
#             self.panelTitleBar, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.BU_NOTEXT)
#         self.btnMaximize = wx.Button(
#             self.panelTitleBar, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.BU_NOTEXT)
#         self.btnExit = wx.Button(
#             self.panelTitleBar, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.BU_NOTEXT)
#         self.panelBody = wx.Panel(self, wx.ID_ANY)

#         self.Bind(wx.EVT_BUTTON, self.OnBtnExitClick, self.btnExit)
#         self.Bind(wx.EVT_BUTTON, self.OnBtnMinimizeClick, self.btnMinimize)
#         self.Bind(wx.EVT_BUTTON, self.OnBtnMaximizeClick, self.btnMaximize)
#         self.panelTitleBar.Bind(wx.EVT_LEFT_DOWN, self.OnTitleBarLeftDown)
#         self.panelTitleBar.Bind(wx.EVT_MOTION, self.OnMouseMove)

#         self._isClickedDown = False
#         self._LastPosition = self.GetPosition()

#         self.__set_properties()
#         self.__do_layout()

#     def __set_properties(self):
#         self.SetTitle("frame")
#         self.btnMinimize.SetMinSize((22, 22))
#         self.btnMinimize.SetBitmap(
#             wx.Bitmap("views\\images\\btn_minimize.png", wx.BITMAP_TYPE_ANY))
#         self.btnMaximize.SetMinSize((22, 22))
#         self.btnMaximize.SetBitmap(
#             wx.Bitmap("views\\images\\btn_maximize.png", wx.BITMAP_TYPE_ANY))
#         self.btnExit.SetMinSize((22, 22))
#         self.btnExit.SetBitmap(
#             wx.Bitmap("views\\images\\btn_close.png", wx.BITMAP_TYPE_ANY))
#         self.panelTitleBar.SetBackgroundColour(wx.Colour(44, 134, 179))
#         self.panelBody.SetBackgroundColour(wx.Colour(255, 255, 255))

#     def __do_layout(self):

#         # Sizers:
#         sizer_1 = wx.BoxSizer(wx.VERTICAL)
#         grid_sizer_1 = wx.FlexGridSizer(2, 1, 0, 0)
#         sizerTitleBar = wx.FlexGridSizer(1, 5, 0, 0)

#         # Titlebar:
#         iconTitleBar = wx.StaticBitmap(self.panelTitleBar, wx.ID_ANY, wx.Bitmap(
#             "views\\images\\favicon.ico", wx.BITMAP_TYPE_ANY), size=(20, 20))
#         sizerTitleBar.Add(
#             iconTitleBar, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 5)
#         title = wx.StaticText(self.panelTitleBar, wx.ID_ANY, self.title)
#         title.SetForegroundColour(wx.Colour(255, 255, 255))
#         title.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT,
#                       wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
#         sizerTitleBar.Add(title, 0, wx.ALIGN_CENTER_VERTICAL |
#                           wx.BOTTOM | wx.TOP, 10)
#         sizerTitleBar.Add(self.btnMinimize, 0,
#                           wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 2)
#         sizerTitleBar.Add(self.btnMaximize, 0,
#                           wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 2)
#         sizerTitleBar.Add(
#             self.btnExit, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 2)
#         sizerTitleBar.AddGrowableRow(0)
#         sizerTitleBar.AddGrowableCol(1)

#         self.panelTitleBar.SetSizer(sizerTitleBar)
#         grid_sizer_1.Add(self.panelTitleBar, 1, wx.EXPAND, 0)
#         grid_sizer_1.Add(self.panelBody, 1, wx.EXPAND, 0)
#         grid_sizer_1.AddGrowableRow(1)
#         grid_sizer_1.AddGrowableCol(0)
#         sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
#         self.SetSizer(sizer_1)
#         self.Layout()

#     def OnTitleBarLeftDown(self, event):
#         self._LastPosition = event.GetPosition()

#     def OnBtnExitClick(self, event):
#         self.Close()

#     def OnBtnMinimizeClick(self, event):
#         self.Iconize(True)

#     def OnBtnMaximizeClick(self, event):
#         self.Maximize(not self.IsMaximized())

#     def OnMouseMove(self, event):
#         if event.Dragging():
#             mouse_x, mouse_y = wx.GetMousePosition()
#             self.Move(
#                 mouse_x-self._LastPosition[0], mouse_y-self._LastPosition[1])

class Window(wx.Frame):
    def __init__(self, parent, title):
        super(Window, self).__init__(parent, title=title, size=(350, 250))

        self.SetBackgroundColour(wx.Colour(26, 26, 26))
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
