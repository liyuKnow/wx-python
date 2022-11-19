#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0)
        wx.Frame.__init__(self, *args, **kwds)

        self.SetSize((800, 500))

        # Creating the custom title bar
        self.panelTitleBar = wx.Panel(self, wx.ID_ANY)
        self.btnMinimize = wx.Button(
            self.panelTitleBar, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.BU_NOTEXT)
        self.btnMaximize = wx.Button(
            self.panelTitleBar, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.BU_NOTEXT)
        self.btnExit = wx.Button(
            self.panelTitleBar, wx.ID_ANY, "", style=wx.BORDER_NONE | wx.BU_NOTEXT)
        self.panelBody = wx.Panel(self, wx.ID_ANY)

        self.Bind(wx.EVT_BUTTON, self.OnBtnExitClick, self.btnExit)
        self.Bind(wx.EVT_BUTTON, self.OnBtnMinimizeClick, self.btnMinimize)
        self.Bind(wx.EVT_BUTTON, self.OnBtnMaximizeClick, self.btnMaximize)
        self.panelTitleBar.Bind(wx.EVT_LEFT_DOWN, self.OnTitleBarLeftDown)
        self.panelTitleBar.Bind(wx.EVT_MOTION, self.OnMouseMove)

        self._isClickedDown = False
        self._LastPosition = self.GetPosition()

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetTitle("frame")
        self.btnMinimize.SetMinSize((22, 22))
        self.btnMinimize.SetBitmap(
            wx.Bitmap("images\\btn_minimize.png", wx.BITMAP_TYPE_ANY))
        self.btnMaximize.SetMinSize((22, 22))
        self.btnMaximize.SetBitmap(
            wx.Bitmap("images\\btn_maximize.png", wx.BITMAP_TYPE_ANY))
        self.btnExit.SetMinSize((22, 22))
        self.btnExit.SetBitmap(
            wx.Bitmap("images\\btn_close.png", wx.BITMAP_TYPE_ANY))
        self.panelTitleBar.SetBackgroundColour(wx.Colour(44, 134, 179))
        self.panelBody.SetBackgroundColour(wx.Colour(255, 255, 255))

    def __do_layout(self):

        # Sizers:
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(2, 1, 0, 0)
        sizerTitleBar = wx.FlexGridSizer(1, 5, 0, 0)

        # Titlebar:
        iconTitleBar = wx.StaticBitmap(self.panelTitleBar, wx.ID_ANY, wx.Bitmap(
            "images\\favicon.ico", wx.BITMAP_TYPE_ANY), size=(20, 20))
        sizerTitleBar.Add(
            iconTitleBar, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 5)
        title = wx.StaticText(self.panelTitleBar, wx.ID_ANY, "My Window Title")
        title.SetForegroundColour(wx.Colour(255, 255, 255))
        title.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT,
                      wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        sizerTitleBar.Add(title, 0, wx.ALIGN_CENTER_VERTICAL |
                          wx.BOTTOM | wx.TOP, 10)
        sizerTitleBar.Add(self.btnMinimize, 0,
                          wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 2)
        sizerTitleBar.Add(self.btnMaximize, 0,
                          wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 2)
        sizerTitleBar.Add(
            self.btnExit, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 2)
        sizerTitleBar.AddGrowableRow(0)
        sizerTitleBar.AddGrowableCol(1)

        self.panelTitleBar.SetSizer(sizerTitleBar)
        grid_sizer_1.Add(self.panelTitleBar, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.panelBody, 1, wx.EXPAND, 0)
        grid_sizer_1.AddGrowableRow(1)
        grid_sizer_1.AddGrowableCol(0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()

    def OnTitleBarLeftDown(self, event):
        self._LastPosition = event.GetPosition()

    def OnBtnExitClick(self, event):
        self.Close()

    def OnBtnMinimizeClick(self, event):
        self.Iconize(True)

    def OnBtnMaximizeClick(self, event):
        self.Maximize(not self.IsMaximized())

    def OnMouseMove(self, event):
        if event.Dragging():
            mouse_x, mouse_y = wx.GetMousePosition()
            self.Move(
                mouse_x-self._LastPosition[0], mouse_y-self._LastPosition[1])


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        self.frame.Center()
        return True


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
