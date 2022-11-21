import wx
from logic import feedbackFont


class MiddlePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, size=(790, 230))
        self.SetBackgroundColour(wx.Colour(41, 41, 41))

        # SET UP FLEX SIZER FOR PANEL
        wrapper = wx.BoxSizer(wx.VERTICAL)

        # MAKE LAYOUT (1x1)
        sizer = wx.FlexGridSizer(rows=1, cols=2, vgap=10, hgap=10)

        # DEFINE WIDGETS
        browse_fil_btn = wx.Button(
            self, label="Browse File", size=(120, 40))
        # browse_fil_btn.Disable()
        conn_feedback = wx.StaticText(self, label="No Devices Are Connected")
        conn_feedback.SetFont(feedbackFont())

        # ADD WIDGETS TO SIZER
        sizer.AddMany([browse_fil_btn,
                       (conn_feedback, 0, wx.EXPAND), ])

        # RESIZE AND ALSO AT MAXIMAZING SCREEN (FLEX GROW)
        sizer.AddGrowableCol(1, 1)

        # SET SIZER TO PANEL WITH A BOX SIZE WRAPPER
        wrapper.Add(sizer, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        self.SetSizer(wrapper)

    def browse_file(self, event):
        with wx.FileDialog(self, "Open Excel file", wildcard="XYZ files (*.xlsx)|*.xls",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if (fileDialog.ShowModal() == wx.ID_CANCEL):
                return     # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r') as file:
                    self.doLoadDataOrWhatever(file)
            except IOError:
                wx.LogError("Cannot open file '%s'." % newfile)
