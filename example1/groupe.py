# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gruop.ui'
#
# Created: Tue Dec 27 09:57:26 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3 
con = sqlite3.connect('DB.db')
cursor=con.cursor()

id=cursor.execute('''SELECT DISTINCT name FROM GROUPE ''')
b=""
for i in id : 
    b+=str(i[0])+'|'
liste=b.split('|')
            #lsn liste name de eleve
              #lIDl list de id 
              #liste de groupe    
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

class Ui_Grup(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(631, 512)
 
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        #self.label = QtGui.QLabel(Form)
        #self.label.setObjectName(_fromUtf8("label"))
        #self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        #self.lineEdit = QtGui.QLineEdit(Form)
        #self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        #self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.treeWidget = QtGui.QTreeWidget(Form)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        for I in liste : 
            if I != '' and I != "None" : 
                item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
                for L in self.listname(I): 
                    item_1 = QtGui.QTreeWidgetItem(item_0)

        self.gridLayout.addWidget(self.treeWidget, 0, 3, 4, 1)
        #self.label_2 = QtGui.QLabel(Form)
        #self.label_2.setObjectName(_fromUtf8("label_2"))
        #self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        #self.lineEdit_2 = QtGui.QLineEdit(Form)
        #self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        #self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)
        #spacerItem = QtGui.QSpacerItem(20, 378, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        #self.gridLayout.addItem(spacerItem, 2, 1, 1, 2)
        #self.toolButton = QtGui.QToolButton(Form)
        #sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        #self.toolButton.setSizePolicy(sizePolicy)
        #icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/A1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.toolButton.setIcon(icon)
        #self.toolButton.setIconSize(QtCore.QSize(91, 40))
        #self.toolButton.setObjectName(_fromUtf8("toolButton"))
        #self.gridLayout.addWidget(self.toolButton, 3, 0, 1, 2)
        #self.toolButton_2 = QtGui.QToolButton(Form)
        #icon1 = QtGui.QIcon()
        #icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/A2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.toolButton_2.setIcon(icon1)
        #self.toolButton_2.setIconSize(QtCore.QSize(91, 40))
        #self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        #self.gridLayout.addWidget(self.toolButton_2, 3, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #Form.setTabOrder(self.lineEdit_2, self.toolButton)
        #Form.setTabOrder(self.toolButton, self.lineEdit)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        #self.label.setText(_translate("Form", "groupe", None))
        self.treeWidget.headerItem().setText(0, _translate("Form", "group", None))
        self.treeWidget.headerItem().setText(1, _translate("Form", "étudiant", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        m=0
        M=0
        for I in liste : 
            if I != '' and I != "None" : 
                self.treeWidget.topLevelItem(m).setText(0, _translate("Form",I, None))
               
                for L in self.listname(I): 
                    self.treeWidget.topLevelItem(m).child(M).setText(0, _translate("Form",L, None))
                    M+=1
            M=0
            m+=1
        
        #self.label_2.setText(_translate("Form", "nombre", None))
        #self.toolButton.setText(_translate("Form", "...", None))
        #self.toolButton_2.setText(_translate("Form", "...", None))
    
    def listname(self,x): 
        if x != '' and x !='None' :
            IDl="" 
            for l in cursor.execute('''SELECT  eleve_id FROM GROUPE WHERE name=? ''',(x,)):
                IDl+=str(l[0])+'|'
            lIDl=IDl.split('|')
            lsn=""
            for i in lIDl :
                if i != '' and i !='None' :
                    for l in cursor.execute('''SELECT name FROM ELEVE WHERE IDELEVE=?''',(i,)):
                        lsn+=str(l[0])+'|'
            return  lsn.split('|')

import icon_rc
