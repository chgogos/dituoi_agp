# https://www.youtube.com/watch?v=2S4t8-GcGPc
# Hello World με GUI
# καλύτερη οργάνωση κώδικα (σε κλάσεις)

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

if __name__=='__main__':
    app = MyApp()
    app.MainLoop()