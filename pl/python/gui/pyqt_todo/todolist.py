from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

#QListItem information-->https://doc.qt.io/qt-5/qlistwidget.html


class window(QMainWindow):
    def __init__(self):
        #Window View
        super().__init__(None)
        self.deletetext=''
        self.setWindowTitle('TODO LIST')
        self.setFixedSize(500,500)
        self.mw=QWidget()
        self.lay=QVBoxLayout()
        self.mw.setLayout(self.lay)
        self.setCentralWidget(self.mw)
        self.List=QListWidget()
        self.List.setFixedSize(0.96*self.width(),0.7*self.height())
        #signal for changed Text
        #self.List.itemClicked.connect(lambda:self.selectedItem())
        self.List.setStyleSheet('margin-bottom:15px; text-align:center;')
        self.List.setSelectionMode(QAbstractItemView.SingleSelection)
        self.edit=QLineEdit()
        self.edit.setFixedWidth(0.96*self.width())
        self.b1=QPushButton('ADD TASK')
        self.b2=QPushButton('DELETE TASK')
        self.b3=QPushButton('LOAD TASKS')
        self.b4=QPushButton('SAVE TASKS')
        self.b1.setFixedWidth(0.96*self.width())
        self.b2.setFixedWidth(0.96*self.width())
        self.b3.setFixedWidth(0.96*self.width())
        self.b4.setFixedWidth(0.96*self.width())
        self.b1.clicked.connect(lambda:self.addTask())
        self.b2.clicked.connect(lambda:self.deleteTask())
        self.b3.clicked.connect(lambda:self.loadTask())
        self.b4.clicked.connect(lambda:self.saveTask())
        self.lay.addWidget(self.List)
        self.lay.addWidget(self.edit)
        self.lay.addWidget(self.b1)
        self.lay.addWidget(self.b2)
        self.lay.addWidget(self.b3)
        self.lay.addWidget(self.b4)
    
    #Slots
    def addTask(self):
        text=self.edit.text()
        if len(text)==0:
            QMessageBox.critical(self,'Error','No Input had been Given')
            return
        self.List.addItem(text)
    def deleteTask(self):
        selected=self.List.selectedItems()
        if len(selected)==0:
            qDebug('No item selected')
            return
        #model=self.List.model()
        for x in selected:
            self.List.takeItem(self.List.row(x))

    def loadTask(self):
        file=QFileDialog.getOpenFileName(self,'Open List','.','txt files (*.txt)')
        if len(file[0])==0:
            QMessageBox.critical(self,'File Retrieve','You did not select a file')
            return
        fp=QFile(str(file[0]))
        fp.open(QIODevice.ReadOnly)
        stream=QTextStream(fp)
        while not stream.atEnd():
            line=stream.readLine()
            self.List.addItem(line)
        fp.close()
        qDebug('File Opened Executed')

    def saveTask(self):
        file=QFileDialog.getSaveFileName(self,'Save Tasks','.','txt file (*.txt)')
        if(len(file[0])==0):
            QMessageBox.critical(self,'Error','No file Selected')
            return
        fp=QFile(file[0])
        fp.open(QIODevice.WriteOnly)
        st=QTextStream(fp)
        listitems=[]
        for x in range(self.List.count()):
            listitems.append(self.List.item(x).text())
        for x in listitems:
            st<<x<<'\n'
        fp.close()

    '''
    def selectedItem(self):
        index=self.List.selectedItems()
        print(index[0])
    '''
