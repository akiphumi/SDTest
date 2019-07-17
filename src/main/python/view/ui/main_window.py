# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/satoakitaka/Documents/rutilea/OSS/SDTest/src/main/python/view/ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 512)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_stacked_widget = QtWidgets.QStackedWidget(self.centralwidget)
        self.main_stacked_widget.setObjectName("main_stacked_widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.main_stacked_widget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.main_stacked_widget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.main_stacked_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 22))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.inspection_action = QtWidgets.QAction(MainWindow)
        self.inspection_action.setCheckable(True)
        self.inspection_action.setChecked(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/resources/base/fonts/fontawesome/small_eye_black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inspection_action.setIcon(icon)
        self.inspection_action.setObjectName("inspection_action")
        self.optimization_action = QtWidgets.QAction(MainWindow)
        self.optimization_action.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/resources/base/fonts/fontawesome/brain_black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.optimization_action.setIcon(icon1)
        self.optimization_action.setObjectName("optimization_action")
        self.past_result_action = QtWidgets.QAction(MainWindow)
        self.past_result_action.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/resources/base/fonts/fontawesome/history_black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.past_result_action.setIcon(icon2)
        self.past_result_action.setObjectName("past_result_action")
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_new_project = QtWidgets.QAction(MainWindow)
        self.action_new_project.setObjectName("action_new_project")
        self.action_close = QtWidgets.QAction(MainWindow)
        self.action_close.setObjectName("action_close")
        self.action_website = QtWidgets.QAction(MainWindow)
        self.action_website.setObjectName("action_website")
        self.action_version = QtWidgets.QAction(MainWindow)
        self.action_version.setObjectName("action_version")
        self.action_about_SDT = QtWidgets.QAction(MainWindow)
        self.action_about_SDT.setObjectName("action_about_SDT")
        self.action_quit_SDTest = QtWidgets.QAction(MainWindow)
        self.action_quit_SDTest.setObjectName("action_quit_SDTest")
        self.menu_file.addAction(self.action_new_project)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_close)
        self.menu_help.addAction(self.action_website)
        self.menu_help.addAction(self.action_version)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.toolBar.addAction(self.inspection_action)
        self.toolBar.addAction(self.optimization_action)
        self.toolBar.addAction(self.past_result_action)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_file.setTitle(_translate("MainWindow", "ファイル"))
        self.menu_help.setTitle(_translate("MainWindow", "ヘルプ"))
        self.inspection_action.setText(_translate("MainWindow", "検品"))
        self.optimization_action.setText(_translate("MainWindow", "学習"))
        self.optimization_action.setToolTip(_translate("MainWindow", "学習"))
        self.past_result_action.setText(_translate("MainWindow", "レポート"))
        self.action_open.setText(_translate("MainWindow", "開く"))
        self.action_new_project.setText(_translate("MainWindow", "新規プロジェクト"))
        self.action_close.setText(_translate("MainWindow", "閉じる"))
        self.action_website.setText(_translate("MainWindow", "SDtestホームページ"))
        self.action_version.setText(_translate("MainWindow", "About SDTest"))
        self.action_about_SDT.setText(_translate("MainWindow", "SDTestについて"))
        self.action_about_SDT.setToolTip(_translate("MainWindow", "SDTestについて"))
        self.action_quit_SDTest.setText(_translate("MainWindow", "SDTestを終了"))


from qrc import icon_rc
