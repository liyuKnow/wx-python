import wx
import os
import subprocess
# importing pandas as pd
import pandas as pd

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

        # DEFINE WIDGETS
        self.left_panel = LeftPanel(self)
        right_panel = RightPanel(self)

        sizer.AddMany(
            [self.left_panel, right_panel]
        )

        # # SET SIZER TO PANEL WITH A BOX SIZE WRAPPER
        outer_wrapper.Add(sizer, proportion=1, flag=wx.ALL |
                          wx.EXPAND, border=10)
        self.SetSizer(outer_wrapper)

    def init_ui(self):
        pass

    def push_button_event(self):
        print(f"bool is {self.FILE_TO_SEND != ''}")
        if (self.FILE_TO_SEND != ''):
            connect_command = "adb get-state"
            subprocess.call(connect_command, shell=True)

            if (self.DEVICE != ''):
                pull_command = (
                    f"adb push {self.FILE_TO_SEND} /storage/emulated/0/Download/"
                )
                subprocess.call(pull_command, shell=True)
                self.SuccessFeedbackLabel.place(x=172, y=190)
            # CHECK IF FILE EXISTS IN THE DEVICE
            # No Device
            else:
                self.FailFeedbackLabel.configure(
                    text="No Devices are connected, connect to device and try again.",)
                self.FailFeedbackLabel.place(x=172, y=190)
        else:
            # No file chosen
            self.FailFeedbackLabel.configure(
                text="No File chosen, choose file and try again.",)
            self.FailFeedbackLabel.place(x=172, y=190)


class LeftPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, size=(380, 210))

        self.excel_file_to_send = ""
        self.csv_file_to_send = ""

        self.InitUI()

    def InitUI(self):
        self.SetBackgroundColour(("#949488"))

        # DEFINE LEFT PANEL WRAPPER
        wrapper = wx.BoxSizer(wx.VERTICAL)

        # DEFINE LEFT PANEL LAYOUT
        sizer = wx.FlexGridSizer(rows=3, cols=1, vgap=5, hgap=0)

        # CREATE THREE ROWS
        self.top = wx.Panel(self, size=(360, 40))
        self.middle = wx.Panel(self, size=(360, 20))
        self.bottom = wx.Panel(self, size=(360, 80))

        # DEFINE LEFT PANEL LAYOUT
        top_sizer = wx.FlexGridSizer(rows=3, cols=2, vgap=5, hgap=10)

        # # DEFINE AND ADD LEFT PANEL WIDGETS
        browse_file_btn = wx.Button(
            self.top, label="Browse File", size=(120, 40), style=wx.NO_BORDER)
        browse_file_btn.Bind(wx.EVT_BUTTON, self.browse_file)

        self.send_file_btn = wx.Button(
            self.top, label="Send File", size=(120, 40), style=wx.NO_BORDER)
        # self.send_file_btn.BackgroundColour(wx.Colour("#e5678d"))
        self.send_file_btn.Disable()
        self.send_file_btn.Bind(wx.EVT_BUTTON, self.push_button_event)

        top_sizer.AddMany(
            [browse_file_btn, self.send_file_btn]
        )

        self.top.SetSizer(top_sizer)

        # DEFINE MIDDLE CHECKBOX
        keep_file_check = wx.CheckBox(self.middle, label="Keep Selected File")
        self.middle.Center()

        # DEFINE BOTTOM FEED BACK AREA GROWABLE
        self.send_feedback = wx.StaticText(
            self.bottom,  wx.ALIGN_BOTTOM, label="TESTING SHIT TESTING SHIT TESTING SHIT TESTING SHIT TESTING SHIT TESTING SHIT TESTING SHIT TESTING SHIT TESTING SHIT",)
        self.send_feedback.SetFont(feedbackFont())

        sizer.AddMany(
            [self.top, self.middle, self.bottom]
        )

        wrapper.Add(sizer, proportion=1, flag=wx.ALL |
                    wx.EXPAND, border=10)
        self.SetSizer(wrapper)

    def browse_file(self, event):
        with wx.FileDialog(self, "Open Excel file", wildcard="Excel Files (*.xlsx,*.xls)|*.xlsx;*.xls",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if (fileDialog.ShowModal() == wx.ID_CANCEL):
                return     # the user changed their mind

            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()

            try:
                with open(pathname, 'r') as file:

                    # USER DESKTOP PATH
                    # file_path = os.path.expanduser('~') + '/Documents'
                    file_path = os.path.expanduser('~') + '\Desktop'

                    excel_file = pd.read_excel(pathname)

                    file_name = fileDialog.GetFilename().split('.')[0]
                    csv_file = f"{file_path}\{file_name}.csv"

                    excel_file.to_csv(csv_file,
                                      index=None,
                                      header=True)
                    # CHECK IF CSV IS  FILE
                    if (os.path.exists(csv_file)):
                        # SET FILES TO SEND
                        self.excel_file_to_send = pathname
                        self.csv_file_to_send = csv_file
                        self.send_file_btn.Enable()

            except IOError:
                wx.LogError(f"Cannot open file {fileDialog.GetPath()}.", )

    def push_button_event(self, event):
        if (os.path.exists(self.excel_file_to_send) and os.path.exists(self.csv_file_to_send)):

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
                    push_excel_command = f"adb push {self.excel_file_to_send} /storage/emulated/0/Download/"
                    push_csv_command = f"adb push {self.csv_file_to_send} /storage/emulated/0/Download/"

                    excel_output = subprocess.Popen(
                        push_excel_command, stdout=subprocess.PIPE, stderr=None, shell=True)
                    csv_output = subprocess.call(
                        push_csv_command, stdout=subprocess.PIPE, stderr=None, shell=True)
                    #

                else:
                    self.send_feedback.SetLabel(
                        "Device Not Ready")
                    self.send_feedback.SetForegroundColour((199, 93, 85))

        else:
            self.send_feedback.SetLabel(
                "Files Are Not Ready")
            self.send_feedback.SetForegroundColour((199, 93, 85))


class RightPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, size=(380, 210))

        self.SetBackgroundColour(("#949488"))

        # DEFINE LEFT PANEL WRAPPER
        wrapper = wx.BoxSizer(wx.VERTICAL)

        # DEFINE LEFT PANEL LAYOUT
        sizer = wx.FlexGridSizer(rows=3, cols=2, vgap=5, hgap=5)

        # # DEFINE AND ADD LEFT PANEL WIDGETS
        browse_file_btn = wx.Button(
            self, label="Browse File", size=(120, 40), style=wx.NO_BORDER)

        send_file_btn = wx.Button(
            self, label="Send File", size=(120, 40), style=wx.NO_BORDER)

        sizer.AddMany(
            [browse_file_btn, send_file_btn]
        )

        wrapper.Add(sizer, proportion=1, flag=wx.ALL |
                    wx.EXPAND, border=10)
        self.SetSizer(wrapper)
