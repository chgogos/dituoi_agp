from PySide6.QtWidgets import QApplication as app 
import todolist as t

def main():
    a=app()
    w=t.window()
    w.show()
    a.exec_()

if __name__=='__main__':
    main()