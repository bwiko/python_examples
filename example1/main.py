# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled_2.ui'
#
# Created: Mon Dec 26 10:08:54 2016
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(744, 600)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 3)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 3)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 0, 1, 2)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 2)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 7, 0, 1, 3)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 2)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 4, 2, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 5, 2, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.gridLayout.addWidget(self.comboBox_2, 0, 0, 1, 3)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 6, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 2, 1)
        spacerItem = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.icon5 = QtGui.QToolButton(self.centralwidget)
        self.icon5.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/a2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon5.setIcon(icon)
        self.icon5.setIconSize(QtCore.QSize(81, 40))
        self.icon5.setPopupMode(QtGui.QToolButton.DelayedPopup)
        self.icon5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.icon5.setObjectName(_fromUtf8("icon5"))
        self.gridLayout_2.addWidget(self.icon5, 0, 2, 1, 1)
        self.icon4 = QtGui.QToolButton(self.centralwidget)
        self.icon4.setFocusPolicy(QtCore.Qt.TabFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/a5.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon4.setIcon(icon1)
        self.icon4.setIconSize(QtCore.QSize(81, 40))
        self.icon4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.icon4.setObjectName(_fromUtf8("icon4"))
        self.gridLayout_2.addWidget(self.icon4, 0, 3, 1, 1)
        self.icon3 = QtGui.QToolButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/a4.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon3.setIcon(icon2)
        self.icon3.setIconSize(QtCore.QSize(81, 40))
        self.icon3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.icon3.setObjectName(_fromUtf8("icon3"))
        self.gridLayout_2.addWidget(self.icon3, 0, 4, 1, 1)
        self.icon2 = QtGui.QToolButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/a3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon2.setIcon(icon3)
        self.icon2.setIconSize(QtCore.QSize(81, 40))
        self.icon2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.icon2.setObjectName(_fromUtf8("icon2"))
        self.gridLayout_2.addWidget(self.icon2, 0, 5, 1, 1)
        self.icon1 = QtGui.QToolButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/a1.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.icon1.setIcon(icon4)
        self.icon1.setIconSize(QtCore.QSize(81, 40))
        self.icon1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.icon1.setObjectName(_fromUtf8("icon1"))
        self.gridLayout_2.addWidget(self.icon1, 0, 6, 1, 1)
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2.addWidget(self.widget, 1, 1, 2, 6)
        spacerItem1 = QtGui.QSpacerItem(20, 312, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 744, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menuFile)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuExit = QtGui.QMenu(self.menuFile)
        self.menuExit.setObjectName(_fromUtf8("menuExit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionCtrl_h = QtGui.QAction(MainWindow)
        self.actionCtrl_h.setObjectName(_fromUtf8("actionCtrl_h"))
        self.actionCtrl_w = QtGui.QAction(MainWindow)
        self.actionCtrl_w.setObjectName(_fromUtf8("actionCtrl_w"))
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionCtrl_h)
        self.menuExit.addAction(self.actionCtrl_w)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.menuExit.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "S1", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "S2", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "S3", None))
        self.label_5.setText(_translate("MainWindow", "SEMESTRE", None))
        self.label.setText(_translate("MainWindow", "nome", None))
        #self.label_4.setText(_translate("MainWindow", "nome de etidion", None))
        self.pushButton.setText(_translate("MainWindow", "recherche", None))
        self.label_2.setText(_translate("MainWindow", "group", None))
        self.label_3.setText(_translate("MainWindow", "ID", None))
        self.icon5.setText(_translate("MainWindow", "prof", None))
        self.icon4.setText(_translate("MainWindow", "eleve", None))
        self.icon3.setText(_translate("MainWindow", "group", None))
        self.icon2.setText(_translate("MainWindow", "addEleve", None))
        self.icon1.setText(_translate("MainWindow", "exit", None))
        self.menuFile.setTitle(_translate("MainWindow", "option ", None))
        self.menuHelp.setTitle(_translate("MainWindow", "help", None))
        self.menuExit.setTitle(_translate("MainWindow", "exit", None))
        self.actionCtrl_h.setText(_translate("MainWindow", "Ctrl+h", None))
        self.actionCtrl_w.setText(_translate("MainWindow", "Ctrl+w", None))

import icon_rc
