import wx

class Frame(wx.Frame):
    def ListInit(self):
        self.list.InsertColumn(1,'TO_DO_TASK',wx.LIST_FORMAT_CENTER,350)
    
    def updateInserted(self):
        self.total.SetValue('Items Inserted:'+str(self.counter))

    def __init__(self):
        wx.Frame.__init__(self,None,wx.ID_ANY,'List Demo',wx.DefaultPosition,wx.Size(400,440))
        self.bx=wx.BoxSizer(wx.VERTICAL)
        self.counter=0
        self.list=wx.ListCtrl(self,wx.ID_ANY,wx.DefaultPosition,wx.Size(390,200),wx.LC_REPORT)
        self.ListInit()
        self.bx.Add(self.list)
        self.inp=wx.TextCtrl(self,wx.ID_ANY,'',wx.DefaultPosition,wx.Size(390,30))
        self.but1=wx.Button(self,wx.ID_ANY,'ADD TASK',wx.DefaultPosition,wx.Size(390,30))
        self.but2=wx.Button(self,wx.ID_ANY,'DELETE TASK',wx.DefaultPosition,wx.Size(390,30))
        self.but3=wx.Button(self,wx.ID_ANY,'LOAD TASKS',wx.DefaultPosition,wx.Size(390,30))
        self.but4=wx.Button(self,wx.ID_ANY,'SAVE TASKS',wx.DefaultPosition,wx.Size(390,30))
        self.but1.Bind(wx.EVT_BUTTON,self.addTask,None)
        self.but2.Bind(wx.EVT_BUTTON,self.removeTask,None)
        self.but3.Bind(wx.EVT_BUTTON,self.loadTask,None)
        self.but4.Bind(wx.EVT_BUTTON,self.saveTask,None)
        self.total=wx.TextCtrl(self,wx.ID_ANY,'Items Inserted:0',wx.DefaultPosition,wx.Size(390,60))
        self.bx.Add(self.inp)
        self.bx.Add(self.but1)
        self.bx.Add(self.but2)
        self.bx.Add(self.but3)
        self.bx.Add(self.but4)
        self.bx.Add(self.total)
        self.SetSizer(self.bx)

        self.Centre()
    
    def addTask(self,event):
        text=self.inp.GetValue()
        item=wx.ListItem()
        item.SetText(text)
        item.SetId(self.counter)
        item.SetWidth(self.list.GetMaxWidth())
        self.list.InsertItem(item)
        self.counter+=1
        self.updateInserted()

    def removeTask(self,event):
        selectedText=self.list.GetSelectedItemCount()
        item=-1
        while True:
            item=self.list.GetNextItem(item,wx.LIST_NEXT_ALL,wx.LIST_STATE_SELECTED)
            if int(item)==-1:
                break
            self.list.DeleteItem(item)
            self.counter-=1
            self.updateInserted()
    
    def loadTask(self,event):
          dial=wx.FileDialog(self,'Select Tasks','.','','',wx.FD_OPEN)
          if dial.ShowModal()==wx.ID_CANCEL:
              wx.MessageBox('You did not select a file')
              return
          filepath=dial.GetPath()
          y=open(filepath)
          for x in y:
              self.list.InsertItem(self.counter,str(x))
              self.counter+=1
          self.updateInserted()
    
    def saveTask(self,event):
        dial=wx.FileDialog(self,'Save Tasks','.','','',wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
        if dial.ShowModal()==wx.ID_CANCEL:
            wx.MessageBox('You did not select a file')
            return
        filepath=dial.GetPath()
        y=open(filepath,'w')
        y.write('Tasks\n')
        for x in range(self.list.ItemCount):
            k=self.list.GetItem(int(x),1)
            y.write(str(self.list.GetItemText(int(x)))+'\n')
        y.close()


    


class app(wx.App):
    def OnInit(self):
        f=Frame()
        f.Show()
        return True

a=app()
a.MainLoop()

