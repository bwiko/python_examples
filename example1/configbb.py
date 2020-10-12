# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addBT.ui'
#
# Created: Mon Dec 26 10:38:40 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BILTA(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(653, 484)
        self.modile=["لغة عربة","رياضيات","فرنسية","الفزياء","تاريخ و جغرافيا","ت.اسلامية",""]
        self.Df=["التقويم","الفرض","الاختبار","المعامل","المعدل","لقب الاستاذ"]
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
       
        self.tableWidget.setColumnCount(len(self.Df))
        self.tableWidget.setHorizontalHeaderLabels(self.Df)
       
        self.tableWidget.setRowCount(len(self.modile))
        self.tableWidget.setVerticalHeaderLabels(self.modile)
        
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 7)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 2, 3, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 2, 4, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 2, 5, 1, 1)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 2, 6, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "lable de eroor", None))
        self.label_3.setText(_translate("Form", "sm", None))
        self.comboBox.setItemText(0, _translate("Form", "1", None))
        self.comboBox.setItemText(1, _translate("Form", "2", None))
        self.comboBox.setItemText(2, _translate("Form", "3", None))
        self.label_2.setText(_translate("Form", "name ", None))
        self.pushButton_3.setText(_translate("Form", "recherche", None))
        self.pushButton_2.setText(_translate("Form", "suppr", None))
        self.pushButton.setText(_translate("Form", "ADD", None))

