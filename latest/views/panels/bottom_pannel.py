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

        left_panel = wx.Panel(self, size=(440, 160))
        left_panel.SetBackgroundColour(("#949488"))

        right_panel = wx.Panel(self, size=(320, 160))
        right_panel.SetBackgroundColour(("#949488"))

        sizer.AddMany(
            [left_panel, right_panel]
        )

        # ADD LEFT PANEL WIDGETS

        # ADD RIGHT PANEL WIDGETS

        outer_wrapper.Add(sizer, proportion=1, flag=wx.ALL |
                          wx.EXPAND, border=10)
        self.SetSizer(outer_wrapper)

    def pull_button_event(self, event):
        file_path = os.path.expanduser('~')
        pull_command = f"adb pull /storage/emulated/0/Download/NewCounter.txt {file_path}\Desktop"
        with subprocess.Popen(pull_command, stdout=subprocess.PIPE, stderr=None, shell=True) as process:
            output = process.communicate()[0].decode("utf-8")
            print(output)
