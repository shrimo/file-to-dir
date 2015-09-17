import os, shutil,sys
from PyQt4 import QtCore, QtGui, uic
(dscr, fscr) = os.path.split(sys.argv[0])
pathname = os.getcwd();
directory = os.path.join(pathname)
files = os.listdir(directory);
app = QtGui.QApplication(sys.argv);
class Guisignal(QtGui.QDialog):
    def __init__(self, *args):
        super(Guisignal, self).__init__(*args)
        uic.loadUi('gui.ui', self)
        self.label.setText(directory)
    @QtCore.pyqtSlot()
    def on_godir1_clicked(self):
        for element in files[:]:
            if element==fscr or element=='gui.ui':
                del element
                self.label.setText('End');
            else:
                xse=os.path.join(pathname,element[:-4])
                os.makedirs(xse)
                self.list.addItem(xse);
        for element in files[:]:
            if element==fscr or element=='gui.ui':
                del element;
            else:
                apph=os.path.join(directory, element)
                shutil.move(element, element[:-4]);
        self.list.addItem('...')
    def on_cl02_clicked(self):
        self.label.setText(directory)
widget = Guisignal()
widget.show();
sys.exit(app.exec_())
