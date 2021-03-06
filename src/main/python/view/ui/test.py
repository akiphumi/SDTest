# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Test(object):
    def setupUi(self, Test):
        Test.setObjectName("Test")
        Test.resize(840, 503)
        font = QtGui.QFont()
        font.setPointSize(9)
        Test.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Test)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stacked_widget = QtWidgets.QStackedWidget(Test)
        self.stacked_widget.setObjectName("stacked_widget")
        self.loading_page = QtWidgets.QWidget()
        self.loading_page.setObjectName("loading_page")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.loading_page)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.loading_gif_label = QtWidgets.QLabel(self.loading_page)
        self.loading_gif_label.setText("")
        self.loading_gif_label.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_gif_label.setObjectName("loading_gif_label")
        self.horizontalLayout_3.addWidget(self.loading_gif_label)
        self.stacked_widget.addWidget(self.loading_page)
        self.result_page = QtWidgets.QWidget()
        self.result_page.setObjectName("result_page")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.result_page)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.distance_area = QtWidgets.QVBoxLayout()
        self.distance_area.setObjectName("distance_area")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.distance_area.addItem(spacerItem)
        self.distance_chart_widget = QtWidgets.QWidget(self.result_page)
        self.distance_chart_widget.setMinimumSize(QtCore.QSize(400, 300))
        self.distance_chart_widget.setObjectName("distance_chart_widget")
        self.distance_area.addWidget(self.distance_chart_widget)
        self.overfitting_alert_label = QtWidgets.QLabel(self.result_page)
        self.overfitting_alert_label.setEnabled(False)
        self.overfitting_alert_label.setWordWrap(True)
        self.overfitting_alert_label.setObjectName("overfitting_alert_label")
        self.distance_area.addWidget(self.overfitting_alert_label)
        self.threshold_title_area = QtWidgets.QHBoxLayout()
        self.threshold_title_area.setObjectName("threshold_title_area")
        self.threshold_title_label = QtWidgets.QLabel(self.result_page)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.threshold_title_label.setFont(font)
        self.threshold_title_label.setStyleSheet("color: #3e3e3e;")
        self.threshold_title_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.threshold_title_label.setObjectName("threshold_title_label")
        self.threshold_title_area.addWidget(self.threshold_title_label)
        self.threshold_label = QtWidgets.QLabel(self.result_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.threshold_label.sizePolicy().hasHeightForWidth())
        self.threshold_label.setSizePolicy(sizePolicy)
        self.threshold_label.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.threshold_label.setFont(font)
        self.threshold_label.setStyleSheet("color: #3e3e3e")
        self.threshold_label.setText("")
        self.threshold_label.setObjectName("threshold_label")
        self.threshold_title_area.addWidget(self.threshold_label)
        self.about_threshold_button = QtWidgets.QPushButton(self.result_page)
        self.about_threshold_button.setStyleSheet("border: none;\n"
"")
        self.about_threshold_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/resources/base/fonts/fontawesome/question-circle_warningOrange.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about_threshold_button.setIcon(icon)
        self.about_threshold_button.setIconSize(QtCore.QSize(28, 28))
        self.about_threshold_button.setObjectName("about_threshold_button")
        self.threshold_title_area.addWidget(self.about_threshold_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.threshold_title_area.addItem(spacerItem1)
        self.distance_area.addLayout(self.threshold_title_area)
        self.threshold_slider = QtWidgets.QSlider(self.result_page)
        self.threshold_slider.setStyleSheet("")
        self.threshold_slider.setProperty("value", 80)
        self.threshold_slider.setTracking(True)
        self.threshold_slider.setOrientation(QtCore.Qt.Horizontal)
        self.threshold_slider.setInvertedAppearance(False)
        self.threshold_slider.setInvertedControls(False)
        self.threshold_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.threshold_slider.setTickInterval(0)
        self.threshold_slider.setObjectName("threshold_slider")
        self.distance_area.addWidget(self.threshold_slider)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.distance_area.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.distance_area)
        spacerItem3 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.performance_area = QtWidgets.QVBoxLayout()
        self.performance_area.setObjectName("performance_area")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.performance_area.addItem(spacerItem4)
        self.performance_title_label = QtWidgets.QLabel(self.result_page)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.performance_title_label.setFont(font)
        self.performance_title_label.setStyleSheet("color: #3e3e3e;")
        self.performance_title_label.setObjectName("performance_title_label")
        self.performance_area.addWidget(self.performance_title_label)
        self.performance_chart_area = QtWidgets.QHBoxLayout()
        self.performance_chart_area.setObjectName("performance_chart_area")
        self.performance_chart_background = QtWidgets.QWidget(self.result_page)
        self.performance_chart_background.setMinimumSize(QtCore.QSize(280, 280))
        self.performance_chart_background.setStyleSheet("background-color: transparent")
        self.performance_chart_background.setObjectName("performance_chart_background")
        self.performance_chart_widget = QtWidgets.QWidget(self.performance_chart_background)
        self.performance_chart_widget.setGeometry(QtCore.QRect(0, 0, 280, 280))
        self.performance_chart_widget.setMinimumSize(QtCore.QSize(280, 280))
        self.performance_chart_widget.setObjectName("performance_chart_widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.performance_chart_background)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 90, 140, 98))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.performance_rates_area = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.performance_rates_area.setContentsMargins(0, 0, 0, 0)
        self.performance_rates_area.setObjectName("performance_rates_area")
        self.accuracy_area = QtWidgets.QHBoxLayout()
        self.accuracy_area.setObjectName("accuracy_area")
        self.accuracy_title_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.accuracy_title_label.setFont(font)
        self.accuracy_title_label.setStyleSheet("color: #3e3e3e")
        self.accuracy_title_label.setObjectName("accuracy_title_label")
        self.accuracy_area.addWidget(self.accuracy_title_label)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.accuracy_area.addItem(spacerItem5)
        self.accuracy_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.accuracy_label.setFont(font)
        self.accuracy_label.setStyleSheet("color: #3FDA68")
        self.accuracy_label.setObjectName("accuracy_label")
        self.accuracy_area.addWidget(self.accuracy_label)
        self.performance_rates_area.addLayout(self.accuracy_area)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.performance_rates_area.addItem(spacerItem6)
        self.false_positive_rate_area = QtWidgets.QHBoxLayout()
        self.false_positive_rate_area.setObjectName("false_positive_rate_area")
        self.false_positive_rate_title_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.false_positive_rate_title_label.setFont(font)
        self.false_positive_rate_title_label.setStyleSheet("color: #3e3e3e")
        self.false_positive_rate_title_label.setObjectName("false_positive_rate_title_label")
        self.false_positive_rate_area.addWidget(self.false_positive_rate_title_label)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.false_positive_rate_area.addItem(spacerItem7)
        self.false_positive_rate_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.false_positive_rate_label.setFont(font)
        self.false_positive_rate_label.setStyleSheet("color: #FFA00E")
        self.false_positive_rate_label.setObjectName("false_positive_rate_label")
        self.false_positive_rate_area.addWidget(self.false_positive_rate_label)
        self.performance_rates_area.addLayout(self.false_positive_rate_area)
        self.false_negative_rate_area = QtWidgets.QHBoxLayout()
        self.false_negative_rate_area.setObjectName("false_negative_rate_area")
        self.false_negative_rate_title_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.false_negative_rate_title_label.setFont(font)
        self.false_negative_rate_title_label.setStyleSheet("color: #3e3e3e")
        self.false_negative_rate_title_label.setObjectName("false_negative_rate_title_label")
        self.false_negative_rate_area.addWidget(self.false_negative_rate_title_label)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.false_negative_rate_area.addItem(spacerItem8)
        self.false_negative_rate_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.false_negative_rate_label.setFont(font)
        self.false_negative_rate_label.setStyleSheet("color: #E66643")
        self.false_negative_rate_label.setObjectName("false_negative_rate_label")
        self.false_negative_rate_area.addWidget(self.false_negative_rate_label)
        self.performance_rates_area.addLayout(self.false_negative_rate_area)
        self.performance_chart_area.addWidget(self.performance_chart_background)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.performance_chart_area.addItem(spacerItem9)
        self.performance_area.addLayout(self.performance_chart_area)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.performance_area.addItem(spacerItem10)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem11 = QtWidgets.QSpacerItem(235, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem11)
        self.details_button = QtWidgets.QPushButton(self.result_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.details_button.sizePolicy().hasHeightForWidth())
        self.details_button.setSizePolicy(sizePolicy)
        self.details_button.setMinimumSize(QtCore.QSize(0, 0))
        self.details_button.setObjectName("details_button")
        self.horizontalLayout_10.addWidget(self.details_button)
        self.performance_area.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_2.addLayout(self.performance_area)
        self.stacked_widget.addWidget(self.result_page)
        self.horizontalLayout.addWidget(self.stacked_widget)

        self.retranslateUi(Test)
        self.stacked_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Test)

    def retranslateUi(self, Test):
        _translate = QtCore.QCoreApplication.translate
        Test.setWindowTitle(_translate("Test", "Form"))
        self.overfitting_alert_label.setText(_translate("Test", "トレーニングと性能評価で良品画像の分布に乖離があり、検査結果が正しく無い可能性が高いです。トレーニングをやり直したり、モデルを変更することが改善のヒントになります。"))
        self.threshold_title_label.setText(_translate("Test", "閾値"))
        self.about_threshold_button.setToolTip(_translate("Test", "<html><head/><body><p><span style=\" font-size:14pt;\">閾値とは</span></p><p><span style=\" font-size:14pt;\">AIが</span><span style=\" font-size:14pt; font-weight:600; color:#3fda68;\">良品</span><span style=\" font-size:14pt;\">と</span><span style=\" font-size:14pt; font-weight:600; color:#e66643;\">不良品</span><span style=\" font-size:14pt;\">を判別する境界値です。まず、検出の際、AIは各画像の「</span><span style=\" font-size:14pt; font-weight:600;\">正常らしさ</span><span style=\" font-size:14pt;\">」を計算します。そして、その「</span><span style=\" font-size:14pt; font-weight:600;\">正常らしさ</span><span style=\" font-size:14pt;\">」が閾値以下の画像を</span><span style=\" font-size:14pt; font-weight:600; color:#e66643;\">不良品</span><span style=\" font-size:14pt;\">、閾値以上の画像を</span><span style=\" font-size:14pt; font-weight:600; color:#3fda68;\">良品</span><span style=\" font-size:14pt;\">だと判定します。よって、閾値を高くすると、製品を「良品」と判定する基準が厳しくなり</span><span style=\" font-size:14pt; font-weight:600; color:#e66643;\">不良品</span><span style=\" font-size:14pt;\">を見逃しにくくなる一方、</span><span style=\" font-size:14pt; font-weight:600; color:#3fda68;\">良品</span><span style=\" font-size:14pt;\">も「不良品」と判定してしまう可能性が高くなります。閾値はバランス良く調整してください。</span></p></body></html>"))
        self.performance_title_label.setText(_translate("Test", "性能評価"))
        self.accuracy_title_label.setText(_translate("Test", "正解率"))
        self.accuracy_label.setText(_translate("Test", "97%"))
        self.false_positive_rate_title_label.setText(_translate("Test", "誤検知率"))
        self.false_positive_rate_label.setText(_translate("Test", "2%"))
        self.false_negative_rate_title_label.setText(_translate("Test", "見逃し率"))
        self.false_negative_rate_label.setText(_translate("Test", "1%"))
        self.details_button.setText(_translate("Test", "詳細"))

from qrc import icon_rc
