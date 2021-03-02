# https://www.youtube.com/watch?v=2S4t8-GcGPc
# Hello World με GUI

import wx

app = wx.App(clearSigInt=True)
frame = wx.Frame(parent=None, id=wx.ID_ANY, title="Hello", pos=(100,100))
panel = wx.Panel(parent=frame, id=wx.ID_ANY)

welcomeText = wx.StaticText(parent=panel, label="hello!!!", pos=(20,20))
frame.Show()
app.MainLoop()