# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Fri May 20 13:58:10 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(507, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 501, 431))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setToolTip(_fromUtf8(""))
        self.tab.setObjectName(_fromUtf8("tab"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tab)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 491, 381))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Monospace"))
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(163, 168, 172);"))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSpiel = QtGui.QMenu(self.menubar)
        self.menuSpiel.setObjectName(_fromUtf8("menuSpiel"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSchnell = QtGui.QAction(MainWindow)
        self.actionSchnell.setObjectName(_fromUtf8("actionSchnell"))
        self.actionVorherige = QtGui.QAction(MainWindow)
        self.actionVorherige.setObjectName(_fromUtf8("actionVorherige"))
        self.menuSpiel.addAction(self.actionSchnell)
        self.menuSpiel.addAction(self.actionVorherige)
        self.menubar.addAction(self.menuSpiel.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.plainTextEdit.setPlainText(QtGui.QApplication.translate("MainWindow", "Hallo Welt", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Live", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Inventar", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSpiel.setTitle(QtGui.QApplication.translate("MainWindow", "Verbinden", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSchnell.setText(QtGui.QApplication.translate("MainWindow", "Schnell", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVorherige.setText(QtGui.QApplication.translate("MainWindow", "Vorherige", None, QtGui.QApplication.UnicodeUTF8))

