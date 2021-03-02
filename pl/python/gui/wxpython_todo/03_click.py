# https://www.youtube.com/watch?v=zivFytz0qZA
# Χειρισμός κλικ σε πλήκτρο

import wx
import webbrowser

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

        button = wx.Button(parent=self, label="Click here!", pos=(20,80))
        button.Bind(event=wx.EVT_BUTTON, handler=self.onSubmit)

    def onSubmit(self, event):
        webbrowser.open("https://chgogos.github.io")

if __name__=='__main__':
    app = MyApp()
    app.MainLoop()