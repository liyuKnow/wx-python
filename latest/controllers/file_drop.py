import wx


class FileDrop(wx.FileDropTarget):

    def __init__(self, window):

        wx.FileDropTarget.__init__(self)
        self.window = window

    def OnDropFiles(self, x, y, filenames):

        for name in filenames:

            try:
                file = open(name, 'r')
                text = file.read()
                self.window.WriteText(text)

            except IOError as error:

                msg = "Error opening file\n {}".format(str(error))
                dlg = wx.MessageDialog(None, msg)
                dlg.ShowModal()

                return False

            except UnicodeDecodeError as error:

                msg = "Cannot open non ascii files\n {}".format(str(error))
                dlg = wx.MessageDialog(None, msg)
                dlg.ShowModal()

                return False

            finally:

                file.close()

        return True
