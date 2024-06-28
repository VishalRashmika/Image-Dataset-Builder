from PyQt6.QtWidgets import *
from PyQt6 import uic

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("form.ui",self)
        self.show()

        # event handlers
        self.btnBrowse.clicked.connect(self.get_file_location)
        self.btnLoad.clicked.connect(self.load_content)


    def get_file_location(self):
        fileName = QFileDialog.getOpenFileName(self,"Open File","./","All Files (*);;Python Files (*.py);; PNG Files (*.png)",)
        self.txtLocation.insertPlainText(fileName[0])

    def load_content(self):
        self.lstEntries.setEnabled(True)
        file = open('test.txt', 'r')

        for entry in file:
            print(entry)
            self.lstEntries.addItem(QListWidgetItem(entry))


def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()

if __name__ == '__main__':
    main()