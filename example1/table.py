# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table.ui'
#
# Created: Sun Dec 25 11:35:22 2016
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

class Ui_table(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(731, 393)
        self.modile=["لغة عربة","رياضيات","فرنسية","الفزياء","تاريخ و جغرافيا","ت.اسلامية",""]
        self.Df=["التقويم","الفرض","الاختبار","المعامل","المعدل","لقب الاستاذ"]
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(Form)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        
        self.tableWidget.setColumnCount(len(self.Df))
        self.tableWidget.setHorizontalHeaderLabels(self.Df)

        self.tableWidget.setRowCount(len(self.modile))
        self.tableWidget.setVerticalHeaderLabels(self.modile)
        
        
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        

