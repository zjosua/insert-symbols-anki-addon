# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_SymbolWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_SymbolWindow(object):
    def setupUi(self, SymbolWindow):
        SymbolWindow.setObjectName(_fromUtf8("SymbolWindow"))
        SymbolWindow.resize(500, 450)
        SymbolWindow.setMinimumSize(QtCore.QSize(500, 450))
        SymbolWindow.setAcceptDrops(False)
        SymbolWindow.setAutoFillBackground(False)
        self.gridLayout = QtGui.QGridLayout(SymbolWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSpacing(8)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.keyLineEdit = QtGui.QLineEdit(SymbolWindow)
        self.keyLineEdit.setMinimumSize(QtCore.QSize(186, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.keyLineEdit.setFont(font)
        self.keyLineEdit.setText(_fromUtf8(""))
        self.keyLineEdit.setObjectName(_fromUtf8("keyLineEdit"))
        self.gridLayout_2.addWidget(self.keyLineEdit, 1, 1, 1, 1)
        self.valueLineEdit = QtGui.QLineEdit(SymbolWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        self.valueLineEdit.setFont(font)
        self.valueLineEdit.setObjectName(_fromUtf8("valueLineEdit"))
        self.gridLayout_2.addWidget(self.valueLineEdit, 1, 2, 1, 1)
        self.labelWith = QtGui.QLabel(SymbolWindow)
        self.labelWith.setObjectName(_fromUtf8("labelWith"))
        self.gridLayout_2.addWidget(self.labelWith, 0, 2, 1, 1)
        self.labelReplace = QtGui.QLabel(SymbolWindow)
        self.labelReplace.setObjectName(_fromUtf8("labelReplace"))
        self.gridLayout_2.addWidget(self.labelReplace, 0, 1, 1, 1)
        self.tableWidget = QtGui.QTableWidget(SymbolWindow)
        self.tableWidget.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tableWidget.setFrameShadow(QtGui.QFrame.Plain)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideRight)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(190)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.tableWidget, 2, 1, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelBlank = QtGui.QLabel(SymbolWindow)
        self.labelBlank.setText(_fromUtf8(""))
        self.labelBlank.setObjectName(_fromUtf8("labelBlank"))
        self.verticalLayout_2.addWidget(self.labelBlank)
        self.addReplaceButton = QtGui.QPushButton(SymbolWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addReplaceButton.sizePolicy().hasHeightForWidth())
        self.addReplaceButton.setSizePolicy(sizePolicy)
        self.addReplaceButton.setMaximumSize(QtCore.QSize(244, 16777215))
        self.addReplaceButton.setObjectName(_fromUtf8("addReplaceButton"))
        self.verticalLayout_2.addWidget(self.addReplaceButton)
        self.deleteButton = QtGui.QPushButton(SymbolWindow)
        self.deleteButton.setObjectName(_fromUtf8("deleteButton"))
        self.verticalLayout_2.addWidget(self.deleteButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.importButton = QtGui.QPushButton(SymbolWindow)
        self.importButton.setObjectName(_fromUtf8("importButton"))
        self.horizontalLayout_2.addWidget(self.importButton)
        self.exportButton = QtGui.QPushButton(SymbolWindow)
        self.exportButton.setObjectName(_fromUtf8("exportButton"))
        self.horizontalLayout_2.addWidget(self.exportButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.okButton = QtGui.QPushButton(SymbolWindow)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout_2.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(SymbolWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_2.addWidget(self.cancelButton)
        self.resetButton = QtGui.QPushButton(SymbolWindow)
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.horizontalLayout_2.addWidget(self.resetButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(SymbolWindow)
        QtCore.QMetaObject.connectSlotsByName(SymbolWindow)

    def retranslateUi(self, SymbolWindow):
        SymbolWindow.setWindowTitle(_translate("SymbolWindow", "Insert Symbol Options", None))
        self.labelWith.setText(_translate("SymbolWindow", "With", None))
        self.labelReplace.setText(_translate("SymbolWindow", "Replace", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("SymbolWindow", "key1", None))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("SymbolWindow", "value1", None))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("SymbolWindow", "key2", None))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("SymbolWindow", "value2", None))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.addReplaceButton.setText(_translate("SymbolWindow", "Add", None))
        self.deleteButton.setText(_translate("SymbolWindow", "Delete", None))
        self.importButton.setText(_translate("SymbolWindow", "Import", None))
        self.exportButton.setText(_translate("SymbolWindow", "Export", None))
        self.okButton.setText(_translate("SymbolWindow", "OK", None))
        self.cancelButton.setText(_translate("SymbolWindow", "Cancel", None))
        self.resetButton.setText(_translate("SymbolWindow", "Reset", None))

