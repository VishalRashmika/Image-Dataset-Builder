from PyQt6.QtWidgets import *
from PyQt6 import uic
from pygoogle_image import image as pi

class MyGUI(QMainWindow):
    fileName = ""
    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi("form.ui",self)
        self.show()

        # event handlers
        self.btnBrowse.clicked.connect(self.get_file_location)
        self.btnLoad.clicked.connect(self.load_content)
        self.btnDownload.clicked.connect(self.bulk_download)


    def get_file_location(self):
        self.fileName = QFileDialog.getOpenFileName(self,"Open File","./","All Files (*);;Python Files (*.py);; PNG Files (*.png)",)[0]
        self.txtLocation.insertPlainText(self.fileName)


    def load_content(self):
        self.lstEntries.setEnabled(True)
        self.lstLog.setEnabled(True)
        self.lstLog.addItem(f"file loaded from : {str(self.fileName)}")

        file = open(str(self.fileName), 'r')
        for entry in file:
            entry = entry.strip()
            listWidgetItem = QListWidgetItem(str(entry))
            self.lstEntries.addItem(listWidgetItem)
        
        number_of_entries = self.lstEntries.count()
        number_of_images = self.txtEntries.toPlainText()
        self.lstLog.addItem(f"No. of entries loaded : {number_of_entries}")
        
        # make this fir diwkiad button
        #self.lstLog.addItem(f"Number of images to be downloaded : {number_of_entries} x {number_of_images} = {int(number_of_entries) * int(number_of_images)}")

    def bulk_download(self):
        self.btnDownload.setEnabled(False)
        for i in range(self.lstEntries.count()):
            # print(self.lstEntries.item(i).text())
            pi.download(self.lstEntries.item(i).text(),limit=self.txtEntries.toPlainText())
        self.lstLog.addItem(f"Download Complete Successfully!!!")
        



def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()

if __name__ == '__main__':
    main()