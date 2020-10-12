# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adderidion.ui'
#
# Created: Mon Dec 26 09:21:52 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sqlite3
con = sqlite3.connect('DB.db')
cursor=con.cursor()


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

class Ui_addons(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(631, 512)
        self.modile=["لغة عربة","رياضيات","فرنسية","الفزياء","تاريخ و جغرافيا","ت.اسلامية"]
        self.namee=cursor.execute('''SELECT * FROM ELEVE ''')

        self.gridLayout_2 = QtGui.QGridLayout(Form)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit_4 = QtGui.QLineEdit(Form)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        m=0
        for i in self.namee : 
            item = QtGui.QListWidgetItem()
            self.listWidget.addItem(item)
            item = self.listWidget.item(m)
            item.setText(_translate("Form",i[1]+":"+i[2], None))
            m=m+1
        self.gridLayout_2.addWidget(self.listWidget, 0, 2, 3, 1)
        spacerItem = QtGui.QSpacerItem(20, 318, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.toolButton = QtGui.QToolButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/A1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(91, 40))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.gridLayout_2.addWidget(self.toolButton, 2, 0, 1, 1)
        self.toolButton_2 = QtGui.QToolButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/A2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon1)
        self.toolButton_2.setIconSize(QtCore.QSize(91, 40))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.gridLayout_2.addWidget(self.toolButton_2, 2, 1, 1, 1)
        
        self.toolButton.clicked.connect(self.INSERTelev)
        self.toolButton.clicked.connect(self.showL)
        
        self.listWidget.itemClicked.connect(self.kk)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit_2, self.toolButton)
        Form.setTabOrder(self.toolButton, self.lineEdit_3)
        Form.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        Form.setTabOrder(self.lineEdit_4, self.listWidget)
        Form.setTabOrder(self.listWidget, self.lineEdit)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_4.setText(_translate("Form", "groupe", None))
        self.label.setText(_translate("Form", "nome", None))
        self.label_2.setText(_translate("Form", "pronom", None))
        self.label_3.setText(_translate("Form", "date", None))
        self.toolButton.setText(_translate("Form", "...", None))
        self.toolButton_2.setText(_translate("Form", "...", None))
         

    def INSERTelev(self):
        if self.lineEdit.text()!= '' and self.lineEdit_3.text()!='' and self.lineEdit_2.text() != '' and self.lineEdit_4.text() != '':
            self.b=self.lineEdit.text()+' '+self.lineEdit_2.text() 
            cursor.execute('''INSERT INTO ELEVE(name,date) VALUES(?,?)''',(self.b,self.lineEdit_3.text()))
            cursor.execute('''SELECT IDELEVE FROM ELEVE WHERE name=?''',(self.b,))
            I=cursor.fetchone()
            cursor.execute('''INSERT INTO GROUPE(name,eleve_id) VALUES(?,?)''',(self.lineEdit_4.text(),I[0]))
            con.commit()
        #self.lineEdit.text()) #name
        #self.lineEdit_2.text()) # pronome
        #self.lineEdit_3.text())  #date
        #self.lineEdit_4.text()) #grope
    def showL(self):

        self.namee=cursor.execute('''SELECT * FROM ELEVE ''')
        m=0
        for i in self.namee : 
            item = QtGui.QListWidgetItem()
            self.listWidget.addItem(item)
            item = self.listWidget.item(m)
            item.setText(_translate("Form",i[1]+":"+i[2], None))
            m=m+1
    def silckte(self,item): 
        cursor.execute('''DELETE  FROM ELEVE WHERE name=?''',(self.B[0],))
    
        con.commit()

    def kk(self,item):
        self.B=item.text().split(':')
        self.toolButton_2.clicked.connect(self.silckte)
        

import icon_rc
