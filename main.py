# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SAS_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog, QApplication
from PyQt5.uic import loadUi
import sys, os
    
class MainWindow(QtWidgets.QMainWindow):
    inputPath = ""
    outputPath = ""

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("SAS_GUI.ui", self)
        self.pushButton_inputDir.clicked.connect(self.getInputFilePath)
        self.textBrowser_inputDir.textChanged.connect(self.textBrowserDir_state_changed)
        self.checkBox_saveToSameDir.stateChanged.connect(self.checkBoxDir_state_changed)
        self.pushButton_outputDir.clicked.connect(self.getOutputFilePath)
        self.textBrowser_outputDir.textChanged.connect(self.textBrowserDir_state_changed)
        self.pushButton_monitor.clicked.connect(self.expandMonitor)

        # CONFIGURATOR


    def getInputFilePath(self):
        response = QFileDialog.getExistingDirectory(self.pushButton_inputDir, "Open Directory",
                                                os.getcwd(),
                                                QFileDialog.ShowDirsOnly
                                                | QFileDialog.DontResolveSymlinks)
        self.textBrowser_inputDir.setText(response)
        self.inputPath = response
        if self.checkBox_saveToSameDir.isChecked():
            self.textBrowser_outputDir.setText(response)
            self.outputPath = response

    def getOutputFilePath(self):
        response = QFileDialog.getExistingDirectory(self.pushButton_outputDir, "Open Directory",
                                                os.getcwd(),
                                                QFileDialog.ShowDirsOnly
                                                | QFileDialog.DontResolveSymlinks)
        self.textBrowser_outputDir.setText(response)
        self.outputPath = response

    def disableButton(self, button):
        button.setEnabled(False)

    def enableButton(self, button):
        button.setEnabled(True)

    def checkBoxDir_state_changed(self, int):
        if self.checkBox_saveToSameDir.isChecked():
            self.textBrowser_outputDir.setText(self.inputPath)
            self.outputPath = self.inputPath
            self.disableButton(self.pushButton_outputDir)
        else:
            self.enableButton(self.pushButton_outputDir)

    def textBrowserDir_state_changed(self):
        
        if (self.inputPath and self.outputPath):
            self.pushButton_start.setEnabled(True)
        else:
            self.pushButton_start.setEnabled(False)

    def expandMonitor(self):
        if self.pushButton_monitor.isChecked():
            self.panel_right.setMaximumWidth(205)
            self.panel_right.setMinimumWidth(205)
        else:
            self.panel_right.setMaximumWidth(0)
            self.panel_right.setMinimumWidth(0)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())