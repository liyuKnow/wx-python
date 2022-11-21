import wx
from logic import feedbackFont
import subprocess


class TopPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent, size=(790, 100))
        self.SetBackgroundColour(wx.Colour(41, 41, 41))

        # SET UP FLEX SIZER FOR PANEL
        wrapper = wx.BoxSizer(wx.VERTICAL)

        # MAKE LAYOUT (1x1)
        sizer = wx.FlexGridSizer(rows=1, cols=2, vgap=10, hgap=10)

        # DEFINE WIDGETS
        self.conn_btn = wx.Button(
            self, label="Test Connection", size=(120, 40), style=wx.BORDER_NONE)
        self.conn_btn.Bind(wx.EVT_BUTTON, self.testConnection)

        self.conn_feedback = wx.StaticText(
            self,  wx.ALIGN_BOTTOM, label="",)
        self.conn_feedback.SetFont(feedbackFont())

        # ADD WIDGETS TO SIZER
        sizer.AddMany([self.conn_btn,
                       (self.conn_feedback, 0, wx.EXPAND), ])

        # RESIZE AND ALSO AT MAXIMAZING SCREEN (FLEX GROW)
        sizer.AddGrowableCol(1, 1)

        # SET SIZER TO PANEL WITH A BOX SIZE WRAPPER
        wrapper.Add(sizer, proportion=1, flag=wx.ALL | wx.EXPAND, border=10)
        self.SetSizer(wrapper)

    def testConnection(self, event):
        device_name = None
        device_list = []

        devices_command = f"adb devices"

        with subprocess.Popen(devices_command, stdout=subprocess.PIPE, stderr=None, shell=True) as process:
            output = process.communicate()[0].decode("utf-8")

            device_list_res = ' '.join(str(output.split(" ")[3]).split())

            device_list = device_list_res.split(" ")

            # WE CAN CHECK IF DEVICE NAME IS AVAILABLE
            if (len(device_list) == 3):
                # DEVICE FOUND
                device_name = device_list[1]

                print(device_name)

                self.conn_feedback.SetLabel("One Device Found")
                self.conn_feedback.SetForegroundColour((108, 174, 80))
            elif (len(device_list) > 3):
                self.conn_feedback.SetLabel(
                    "More Than One Device Found, Connect only one device and try again")
                self.conn_feedback.SetForegroundColour((199, 93, 85))
            else:
                self.conn_feedback.SetLabel(
                    "No Device Found, Connect a device and Try Again!")
                self.conn_feedback.SetForegroundColour((199, 93, 85))
