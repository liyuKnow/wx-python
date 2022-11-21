import wx
import subprocess
# LOCAL PACKAGE
from controllers import feedbackFont


class MiddlePanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, size=(790, 230))

        self.SetBackgroundColour(wx.Colour("#bfbfbf"))

        # SET UP FLEX SIZER FOR PANEL
        outer_wrapper = wx.BoxSizer(wx.VERTICAL)

        # # MAKE LAYOUT (1x2)
        sizer = wx.FlexGridSizer(rows=1, cols=2, vgap=5, hgap=5)

        self.left_panel = wx.Panel(self, size=(380, 210))
        self.left_panel.SetBackgroundColour(("#949488"))

        right_panel = wx.Panel(self, size=(380, 210))
        right_panel.SetBackgroundColour(("#949488"))

        sizer.AddMany(
            [self.left_panel, right_panel]
        )

        # DEFINE LEFT PANEL WRAPPER
        left_wrapper = wx.BoxSizer(wx.VERTICAL)

        # DEFINE LEFT PANEL LAYOUT
        left_sizer = wx.FlexGridSizer(rows=1, cols=2, vgap=5, hgap=5)

        # # DEFINE AND ADD LEFT PANEL WIDGETS
        browse_file_btn = wx.Button(
            self.left_panel, label="Browse File", size=(120, 40), style=wx.NO_BORDER)

        send_file_btn = wx.Button(
            self.left_panel, label="Send File", size=(120, 40), style=wx.NO_BORDER)

        left_sizer.AddMany(
            [browse_file_btn, send_file_btn]
        )

        left_wrapper.Add(left_sizer, proportion=1, flag=wx.ALL |
                         wx.EXPAND, border=10)
        self.left_panel.SetSizer(left_wrapper)

        # conn_feedback = wx.StaticText(self, label="No Devices Are Connected")
        # conn_feedback.SetFont(feedbackFont())

        #  DEFINE AND ADD RIGHT PANEL WIDGETS

        # # ADD WIDGETS TO SIZER
        # sizer.AddMany([browse_file_btn,
        #                (conn_feedback, 0, wx.EXPAND), ])

        # # RESIZE AND ALSO AT MAXIMAZING SCREEN (FLEX GROW)
        # sizer.AddGrowableCol(1, 1)

        # # SET SIZER TO PANEL WITH A BOX SIZE WRAPPER
        outer_wrapper.Add(sizer, proportion=1, flag=wx.ALL |
                          wx.EXPAND, border=10)
        self.SetSizer(outer_wrapper)

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

    # def push_button_event(self):
    #     print(f"bool is {self.FILE_TO_SEND != ''}")
    #     if (self.FILE_TO_SEND != ''):
    #         connect_command = "adb get-state"
    #         subprocess.call(connect_command, shell=True)

    #         if (self.DEVICE != ''):
    #             pull_command = (
    #                 f"adb push {self.FILE_TO_SEND} /storage/emulated/0/Download/"
    #             )
    #             subprocess.call(pull_command, shell=True)
    #             self.SuccessFeedbackLabel.place(x=172, y=190)
    #         # CHECK IF FILE EXISTS IN THE DEVICE
    #         # No Device
    #         else:
    #             self.FailFeedbackLabel.configure(
    #                 text="No Devices are connected, connect to device and try again.",)
    #             self.FailFeedbackLabel.place(x=172, y=190)
    #     else:
    #         # No file chosen
    #         self.FailFeedbackLabel.configure(
    #             text="No File chosen, choose file and try again.",)
    #         self.FailFeedbackLabel.place(x=172, y=190)
