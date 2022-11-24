import wx
import os
import subprocess

from controllers import feedbackFont


class BottomPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, size=(790, 180))
        self.SetBackgroundColour(wx.Colour("#bfbfbf"))

        # SET UP FLEX SIZER FOR PANEL
        outer_wrapper = wx.BoxSizer(wx.VERTICAL)

        # # MAKE LAYOUT (1x2)
        sizer = wx.FlexGridSizer(rows=1, cols=2, vgap=5, hgap=5)

        self.left_panel = LeftPanel(self)

        self.right_panel = RightPanel(self)

        sizer.AddMany(
            [self.left_panel, self.right_panel]
        )
        outer_wrapper.Add(sizer, proportion=1, flag=wx.ALL |
                          wx.EXPAND, border=10)
        self.SetSizer(outer_wrapper)

    def pull_button_event(self, event):
        file_path = os.path.expanduser('~')
        pull_command = f"adb pull /storage/emulated/0/Download/NewCounter.txt {file_path}\Desktop"
        with subprocess.Popen(pull_command, stdout=subprocess.PIPE, stderr=None, shell=True) as process:
            output = process.communicate()[0].decode("utf-8")
            print(output)


class LeftPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, size=(380, 160))
        self.InitUI()

    def InitUI(self):
        self.SetSize(440, 160)

        self.wrapper = wx.BoxSizer(wx.VERTICAL)

        self.get_file = wx.Button(
            self, label="Get File", size=(120, 40), style=wx.BORDER_NONE)
        self.get_file.Bind(wx.EVT_BUTTON, self.getFile)

        self.get_file_feedback = wx.StaticText(
            self, label="", size=(120, 40), style=wx.BORDER_NONE)
        self.get_file_feedback.SetFont(feedbackFont())

        self.wrapper.Add(self.get_file, proportion=0,
                         flag=wx.ALL | wx.EXPAND, border=5)
        self.wrapper.Add(self.get_file_feedback, proportion=1,
                         flag=wx.ALL | wx.EXPAND, border=5)

        self.SetSizer(self.wrapper)

        self.Centre()

    def getFile(self, event):
        file_path = os.path.expanduser('~')
        pull_excel_command = f"adb pull /storage/emulated/0/Download/NewCounter.txt {file_path}\Desktop"

        device_command = "adb devices"
        with subprocess.Popen(device_command, stdout=subprocess.PIPE, stderr=None, shell=True) as process:
            #  CHECK IF DEVICE AVAILABLE
            output = process.communicate()[0].decode("utf-8")

            device_list_res = ' '.join(str(output.split(" ")[3]).split())

            device_list = device_list_res.split(" ")

            # WE CAN CHECK IF DEVICE NAME IS AVAILABLE
            if (len(device_list) == 3):
                # DEVICE FOUND
                device_name = device_list[1]

                excel_output = subprocess.Popen(
                    pull_excel_command, stdout=subprocess.PIPE, stderr=None, shell=True)

                self.get_file_feedback.SetLabel(
                    "File was Received successfully")
                self.get_file_feedback.SetForegroundColour((108, 174, 80))

            else:
                self.get_file_feedback.SetLabel(
                    "Device Not Ready")
                self.get_file_feedback.SetForegroundColour((199, 93, 85))


class RightPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, size=(380, 210))

        self.InitUI()

    def InitUI(self):
        self.SetBackgroundColour(("#949488"))
        self.SetSize(300, 160)
        # self.wrapper = wx.BoxSizer(wx.HORIZONTAL)

        # self.get_file_btn = wx.Button(
        #     self, label="Get File", size=(120, 40), style=wx.BORDER_NONE)

        # self.get_file_feedback = wx.StaticText(self, label="hello")

        # self.left_wrapper.AddMany([self.get_file_btn, self.get_file_feedback])

        # # SET UP FLEX SIZER FOR PANEL
        # wrapper = wx.BoxSizer(wx.VERTICAL)

        # # MAKE LAYOUT (1x1)
        # sizer = wx.FlexGridSizer(rows=1, cols=2, vgap=10, hgap=10)

        # # DEFINE WIDGETS
        # self.conn_btn = wx.Button(
        #     self, label="Test Connection", size=(120, 40), style=wx.BORDER_NONE)
        # self.conn_btn.Bind(wx.EVT_BUTTON, self.testConnection)

        # self.conn_feedback = wx.StaticText(
        #     self, wx.ALIGN_RIGHT, label="",)
        # self.conn_feedback.SetFont(feedbackFont())

        # # ADD WIDGETS TO SIZER
        # sizer.AddMany([self.conn_btn,
        #                (self.conn_feedback, 0, wx.EXPAND), ])

        # # RESIZE AND ALSO AT MAXIMAZING SCREEN (FLEX GROW)
        # sizer.AddGrowableCol(1, 1)

        # # SET SIZER TO PANEL WITH A BOX SIZE WRAPPER
        # wrapper.Add(sizer, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        # self.SetSizer(wrapper)
