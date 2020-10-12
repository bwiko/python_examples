from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
import sys 


from main import Ui_MainWindow 
from table import Ui_table
from ADDet import Ui_adde
from ADDons import Ui_addons
from configbb import Ui_BILTA
from groupe import Ui_Grup
import sqlite3#from GETER import * 
stt= open('darkorange.stylesheet','r')
styl=stt.read()
stt.close()




class main(QMainWindow,Ui_MainWindow) : 
	def __init__(self):
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.icon1.clicked.connect(self.close)
		self.pushButton.clicked.connect(self.BT)
		self.icon2.clicked.connect(self.BILTA)
		self.icon3.clicked.connect(self.Groupe)
		self.icon4.clicked.connect(self.ADE)
		self.icon5.clicked.connect(self.ADO)
		self.window2 = None
		
	
	def BT(self):
		if self.window2 is None:
			self.window2 = Ui_table(self)
		else : 
			self.window2= None
			self.window2=Ui_table(self)

		self.gridLayout_2.addWidget(self.window2, 1, 1, 3, 6)
		#self.window2.show()
		
	def ADO(self): 
		self.dulwindow1=QWidget()
		self.gridLayout_2.addWidget(self.dulwindow1, 1, 1, 3, 6)
		if self.window2 is None:
			self.window2 = Ui_adde(self)	
		
		else : 
			 
			self.window2= None 
			self.window2=Ui_adde(self)
			
		self.gridLayout_2.addWidget(self.window2, 1, 1, 3, 6)


	def ADE(self):
		self.dulwindow1=QWidget()
		self.gridLayout_2.addWidget(self.dulwindow1, 1, 1, 3, 6)
		if self.window2 is None:
			self.window2 = Ui_addons(self)	
		
		else : 
			 
			self.window2= None 
			self.window2=Ui_addons(self)
		
		self.gridLayout_2.addWidget(self.window2, 1, 1, 3, 6)
	def BILTA(self):
			self.dulwindow1=QWidget()
			self.gridLayout_2.addWidget(self.dulwindow1, 1, 1, 3, 6)
			if self.window2 is None:
				self.window2 = Ui_BILTA(self)	
		
			else : 
			 
				self.window2= None 
				self.window2=Ui_BILTA(self)
			
			self.gridLayout_2.addWidget(self.window2, 1, 1, 3, 6)


	def Groupe(self):
			self.dulwindow1=QWidget()
			self.gridLayout_2.addWidget(self.dulwindow1, 1, 1, 3, 6)
			if self.window2 is None:
				self.window2 = Ui_Groupe(self)	
		
			else : 
			 
				self.window2= None 
				self.window2=Ui_Groupe(self)
			
			self.gridLayout_2.addWidget(self.window2, 1, 1, 3, 6)

#Widgets()
class Ui_table(QWidget, Ui_table):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		self.setupUi(self)


class Ui_adde(QWidget, Ui_adde):
	def __init__(self, parent=None):
		QWidget.__init__(self, parent)
		self.setupUi(self)
		
class Ui_addons(QWidget,Ui_addons):
	def __init__(self,parent=None):
		QWidget.__init__(self,parent)
		self.setupUi(self)
		

class Ui_BILTA(QWidget,Ui_BILTA):
	def __init__(self,parent=None):
		QWidget.__init__(self,parent)
		self.setupUi(self)


class Ui_Groupe(QWidget,Ui_Grup):
	def __init__(self,parent=None):
		QWidget.__init__(self,parent)
		self.setupUi(self)


app=QApplication(sys.argv)
window=main()


window.setStyleSheet(styl)

window.show()
app.exec_()