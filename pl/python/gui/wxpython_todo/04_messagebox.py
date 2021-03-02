# https://www.youtube.com/watch?v=dlpgiskBVLE

import wx

class MyApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        self.initFrame()

    def initFrame(self):
        frame = MyFrame(parent=None, title="Hello", pos=(100,100))
        frame.Show()

class MyFrame(wx.Frame):
    def __init__(self, parent, title, pos):
        super().__init__(parent=parent, title=title, pos=pos)
        self.OnInit()

    def OnInit(self):
        panel = MyPanel(parent=self)

class MyPanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent=parent)
        
        welcomeText = wx.StaticText(parent=self, label="hello!!!", pos=(20,20))
        self._textbox = wx.TextCtrl(parent=self, 
                    value="Εισάγετε το όνομά σας εδώ", 
                    pos=(20,60))

        button = wx.Button(parent=self, label="Υποβολή", pos=(20,120))
        button.Bind(event=wx.EVT_BUTTON, handler=self.onSubmit)

    def showDialog(self):
        dlg = wx.RichMessageDialog(parent=None, message="Hi!", 
            caption="Μήνυμα", 
            style=wx.YES_NO|wx.CANCEL|wx.CENTRE)
        dlg.ShowModal()

    def onSubmit(self, event):
        print(self._textbox.GetValue())
        self.showDialog()

if __name__=='__main__':
    app = MyApp()
    app.MainLoop()