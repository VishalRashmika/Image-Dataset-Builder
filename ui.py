from PyQt6.QtWidgets import *
from PyQt6 import uic
# from pygoogle_image import image as pi

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
        
        
        self.txtEntries.insertPlainText("0")



    def get_file_location(self):
        self.fileName = QFileDialog.getOpenFileName(self,"Open File","./","All Files (*);;Python Files (*.py);; PNG Files (*.png)",)[0]
        self.txtLocation.insertPlainText(self.fileName)


    def load_content(self):
        # setting the default value to 0:

        if self.txtEntries.toPlainText() == "0" or not(self.txtEntries.toPlainText().isnumeric()) or len(str(self.txtLocation.toPlainText())) == 0:
            # error
            QMessageBox.critical(self, 'Message', "Invalid Input. Enter valid Inputs !", QMessageBox.StandardButton.Ok)
        else:
            try:
                self.lstEntries.clear()
                self.lstLog.clear()
                self.lstEntries.setEnabled(True)
                self.lstLog.setEnabled(True)
                self.lstLog.addItem(f"file loaded from : {str(self.fileName)}")

                file = open(str(self.fileName), 'r')
                for entry in file:
                    entry = entry.strip()
                    listWidgetItem = QListWidgetItem(str(entry))
                    self.lstEntries.addItem(listWidgetItem)            
                self.lstLog.addItem(f"No. of entries loaded : {self.lstEntries.count()}")
            except:
                QMessageBox.critical(self, 'Message', "Error Occured. Check the inputs.", QMessageBox.StandardButton.Ok)
        
    def bulk_download(self):
        print(self.lstEntries.count())
        if self.lstEntries.count() == 0:
            QMessageBox.critical(self, 'Message', "No files Loaded!!!", QMessageBox.StandardButton.Ok)
            
        else:
            reply = QMessageBox.question(self, 'Message', "Are you sure you want to download?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
            
            if reply == QMessageBox.StandardButton.Yes:
                # Disabling Buttons and Text Areas
                self.btnDownload.setEnabled(False)
                self.btnBrowse.setEnabled(False)
                self.btnLoad.setEnabled(False)
                self.txtLocation.setEnabled(False)
                self.txtEntries.setEnabled(False)
                
                self.lstLog.addItem(f"Number of images to be downloaded : {self.lstEntries.count()} x {self.txtEntries.toPlainText()} = {int(self.lstEntries.count()) * int(self.txtEntries.toPlainText())}")

                for i in range(self.lstEntries.count()):
                    # pi.download(self.lstEntries.item(i).text(),limit=self.txtEntries.toPlainText()
                    self.lstLog.addItem(f"Downloading {self.lstEntries.item(i).text()} entry....")
                    pass
                self.lstLog.addItem(f"Download Completed Successfully!!!")
                
                # Enabling Buttons and Text Areas
                self.btnDownload.setEnabled(True)
                self.btnBrowse.setEnabled(True)
                self.btnLoad.setEnabled(True)
                self.txtLocation.setEnabled(True)
                self.txtEntries.setEnabled(True)
            else:
                pass

        



def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()

if __name__ == '__main__':
    main()