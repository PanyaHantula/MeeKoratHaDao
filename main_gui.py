# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_gui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QDateTimeEdit, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(1280, 720)
        font = QFont()
        font.setFamilies([u"Arial"])
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 1256, 701))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.tabWidget.setFont(font1)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setStyleSheet(u"font: 20pt \"Arial\";")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setMovable(False)
        self.tab_main = QWidget()
        self.tab_main.setObjectName(u"tab_main")
        self.label_4 = QLabel(self.tab_main)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(990, 15, 151, 31))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(18)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"font: 18pt \"Arial\";")
        self.label_12 = QLabel(self.tab_main)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(1150, 10, 81, 81))
        self.label_12.setFont(font1)
        self.label_12.setPixmap(QPixmap(u"/home/raspberry/Desktop/MeeKorat5Dao/logo.png"))
        self.label_19 = QLabel(self.tab_main)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(955, 45, 181, 31))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(24)
        font3.setBold(False)
        font3.setItalic(False)
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"font: 24pt \"Arial\";")
        self.twDB = QTableWidget(self.tab_main)
        self.twDB.setObjectName(u"twDB")
        self.twDB.setGeometry(QRect(361, 108, 876, 471))
        self.twDB.setFont(font1)
        self.twDB.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.twDB.horizontalHeader().setDefaultSectionSize(120)
        self.label_11 = QLabel(self.tab_main)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(365, 75, 161, 31))
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"font: 18pt \"Arial\";")
        self.layoutWidget = QWidget(self.tab_main)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.layoutWidget.setFont(font1)
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.lbl_dateNow = QLabel(self.tab_main)
        self.lbl_dateNow.setObjectName(u"lbl_dateNow")
        self.lbl_dateNow.setGeometry(QRect(85, 84, 181, 29))
        self.lbl_dateNow.setFont(font3)
        self.lbl_dateNow.setStyleSheet(u"font: 24pt \"Arial\";\n"
"color: rgb(7, 64, 128);")
        self.lbl_dateNow.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_26 = QLabel(self.tab_main)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 10, 131, 31))
        self.label_26.setFont(font2)
        self.label_26.setStyleSheet(u"font: 18pt \"Arial\";")
        self.label_31 = QLabel(self.tab_main)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(5, 84, 131, 31))
        self.label_31.setFont(font2)
        self.label_31.setStyleSheet(u"font: 18pt \"Arial\";")
        self.lbl_Clock = QLabel(self.tab_main)
        self.lbl_Clock.setObjectName(u"lbl_Clock")
        self.lbl_Clock.setGeometry(QRect(90, 0, 246, 85))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(60)
        font4.setBold(False)
        font4.setItalic(False)
        self.lbl_Clock.setFont(font4)
        self.lbl_Clock.setStyleSheet(u"font: 60pt \"Arial\";\n"
"color: rgb(7, 64, 128);")
        self.lbl_Clock.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lbl_CountTotal = QLabel(self.tab_main)
        self.lbl_CountTotal.setObjectName(u"lbl_CountTotal")
        self.lbl_CountTotal.setGeometry(QRect(15, 195, 341, 126))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(100)
        font5.setBold(False)
        font5.setItalic(False)
        self.lbl_CountTotal.setFont(font5)
        self.lbl_CountTotal.setStyleSheet(u"font: 100pt \"Arial\";\n"
"color: rgb(16, 128, 64);")
        self.label_2 = QLabel(self.tab_main)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(12, 158, 151, 41))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"font: 18pt \"Arial\";")
        self.label_5 = QLabel(self.tab_main)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(155, 165, 51, 24))
        font6 = QFont()
        font6.setFamilies([u".AppleSystemUIFont"])
        font6.setPointSize(18)
        font6.setBold(False)
        font6.setItalic(False)
        self.label_5.setFont(font6)
        self.label_5.setStyleSheet(u"font: 18pt \".AppleSystemUIFont\";")
        self.btn_update = QPushButton(self.tab_main)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setGeometry(QRect(985, 600, 111, 46))
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(15)
        font7.setBold(False)
        font7.setItalic(False)
        self.btn_update.setFont(font7)
        self.btn_update.setStyleSheet(u"font: 15pt \"Arial\";\n"
"background-color: rgb(15, 128, 255);\n"
"")
        self.btn_update.setIconSize(QSize(32, 16))
        self.label_9 = QLabel(self.tab_main)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(165, 440, 46, 17))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"font: 13pt \"Arial\";")
        self.btn_exit = QPushButton(self.tab_main)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(1125, 600, 111, 46))
        self.btn_exit.setFont(font7)
        self.btn_exit.setStyleSheet(u"font: 15pt \"Arial\";\n"
"background-color: rgb(252, 1, 7);")
        self.btn_exit.setIconSize(QSize(32, 16))
        self.lbl_Preformance = QLabel(self.tab_main)
        self.lbl_Preformance.setObjectName(u"lbl_Preformance")
        self.lbl_Preformance.setGeometry(QRect(15, 353, 326, 68))
        self.lbl_Preformance.setFont(font4)
        self.lbl_Preformance.setStyleSheet(u"font: 60pt \"Arial\";\n"
"color: rgb(128, 0, 2);")
        self.label_3 = QLabel(self.tab_main)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(16, 315, 176, 36))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"font: 18pt \"Arial\";")
        self.label_6 = QLabel(self.tab_main)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(204, 315, 91, 36))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"font: 18pt \"Arial\";")
        self.lbl_Power = QLabel(self.tab_main)
        self.lbl_Power.setObjectName(u"lbl_Power")
        self.lbl_Power.setGeometry(QRect(10, 468, 341, 66))
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(48)
        font8.setBold(False)
        font8.setItalic(False)
        self.lbl_Power.setFont(font8)
        self.lbl_Power.setStyleSheet(u"font: 48pt \"Arial\";\n"
"color: rgb(7, 64, 128);")
        self.label_8 = QLabel(self.tab_main)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(210, 555, 61, 17))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"font: 13pt \"Arial\";")
        self.label_7 = QLabel(self.tab_main)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(15, 428, 206, 41))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"font: 18pt \"Arial\";")
        self.lbl_Energy = QLabel(self.tab_main)
        self.lbl_Energy.setObjectName(u"lbl_Energy")
        self.lbl_Energy.setGeometry(QRect(6, 575, 346, 61))
        self.lbl_Energy.setFont(font8)
        self.lbl_Energy.setStyleSheet(u"font: 48pt \"Arial\";\n"
"color: rgb(7, 64, 128);")
        self.label_10 = QLabel(self.tab_main)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(4, 540, 216, 41))
        self.label_10.setFont(font1)
        self.label = QLabel(self.tab_main)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(6, 120, 69, 24))
        self.label.setFont(font6)
        self.label.setStyleSheet(u"font: 18pt \".AppleSystemUIFont\";")
        self.lbl_StartTime = QLabel(self.tab_main)
        self.lbl_StartTime.setObjectName(u"lbl_StartTime")
        self.lbl_StartTime.setGeometry(QRect(85, 120, 191, 27))
        self.lbl_StartTime.setFont(font3)
        self.lbl_StartTime.setStyleSheet(u"font: 24pt \"Arial\";\n"
"color: rgb(7, 64, 128);")
        self.lbl_StartTime.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.tabWidget.addTab(self.tab_main, "")
        self.lbl_Preformance.raise_()
        self.label_3.raise_()
        self.label_6.raise_()
        self.lbl_Power.raise_()
        self.label_8.raise_()
        self.label_7.raise_()
        self.lbl_Energy.raise_()
        self.label_10.raise_()
        self.label.raise_()
        self.lbl_StartTime.raise_()
        self.label_4.raise_()
        self.label_19.raise_()
        self.twDB.raise_()
        self.label_11.raise_()
        self.layoutWidget.raise_()
        self.lbl_dateNow.raise_()
        self.label_26.raise_()
        self.label_31.raise_()
        self.lbl_Clock.raise_()
        self.lbl_CountTotal.raise_()
        self.label_2.raise_()
        self.label_5.raise_()
        self.btn_update.raise_()
        self.label_9.raise_()
        self.btn_exit.raise_()
        self.label_12.raise_()
        self.tab_results = QWidget()
        self.tab_results.setObjectName(u"tab_results")
        self.tw_Resulte_DB = QTableWidget(self.tab_results)
        self.tw_Resulte_DB.setObjectName(u"tw_Resulte_DB")
        self.tw_Resulte_DB.setGeometry(QRect(10, 245, 1226, 361))
        self.tw_Resulte_DB.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.btn_Delete = QPushButton(self.tab_results)
        self.btn_Delete.setObjectName(u"btn_Delete")
        self.btn_Delete.setGeometry(QRect(1125, 610, 113, 41))
        self.btn_Delete.setStyleSheet(u"font: 18pt \"Arial\";\n"
"background-color: rgb(252, 1, 7);")
        self.label_22 = QLabel(self.tab_results)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 70, 146, 51))
        self.label_22.setStyleSheet(u"font: 22pt \"Arial\";\n"
"color: rgb(7, 64, 128);")
        self.label_28 = QLabel(self.tab_results)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(1160, 10, 81, 81))
        self.label_28.setPixmap(QPixmap(u"/home/raspberry/Desktop/MeeKorat5Dao/logo.png"))
        self.line = QFrame(self.tab_results)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(505, 170, 20, 61))
        self.line.setFont(font1)
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_29 = QLabel(self.tab_results)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(960, 50, 181, 31))
        self.label_29.setFont(font3)
        self.label_29.setStyleSheet(u"font: 24pt \"Arial\";")
        self.label_27 = QLabel(self.tab_results)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(1000, 20, 146, 31))
        self.label_27.setFont(font2)
        self.label_27.setStyleSheet(u"font: 18pt \"Arial\";")
        self.layoutWidget1 = QWidget(self.tab_results)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 165, 486, 29))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.horizontalLayout.addWidget(self.label_16)

        self.lbl_Resulte_TotalCount = QLabel(self.layoutWidget1)
        self.lbl_Resulte_TotalCount.setObjectName(u"lbl_Resulte_TotalCount")
        self.lbl_Resulte_TotalCount.setFont(font1)

        self.horizontalLayout.addWidget(self.lbl_Resulte_TotalCount)

        self.label_23 = QLabel(self.layoutWidget1)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.horizontalLayout.addWidget(self.label_23)

        self.layoutWidget2 = QWidget(self.tab_results)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 200, 486, 29))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.layoutWidget2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_17)

        self.lbl_Resulte_power = QLabel(self.layoutWidget2)
        self.lbl_Resulte_power.setObjectName(u"lbl_Resulte_power")
        self.lbl_Resulte_power.setFont(font1)

        self.horizontalLayout_2.addWidget(self.lbl_Resulte_power)

        self.label_25 = QLabel(self.layoutWidget2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_25)

        self.layoutWidget3 = QWidget(self.tab_results)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(535, 165, 501, 29))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.layoutWidget3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_15)

        self.lbl_Resulte_Preformance = QLabel(self.layoutWidget3)
        self.lbl_Resulte_Preformance.setObjectName(u"lbl_Resulte_Preformance")
        self.lbl_Resulte_Preformance.setFont(font1)

        self.horizontalLayout_3.addWidget(self.lbl_Resulte_Preformance)

        self.label_24 = QLabel(self.layoutWidget3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_24)

        self.layoutWidget4 = QWidget(self.tab_results)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(535, 200, 501, 29))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.layoutWidget4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_18)

        self.lbl_Resulte_energy = QLabel(self.layoutWidget4)
        self.lbl_Resulte_energy.setObjectName(u"lbl_Resulte_energy")
        self.lbl_Resulte_energy.setFont(font1)

        self.horizontalLayout_4.addWidget(self.lbl_Resulte_energy)

        self.label_30 = QLabel(self.layoutWidget4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_30)

        self.layoutWidget5 = QWidget(self.tab_results)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(14, 125, 556, 29))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.layoutWidget5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_13)

        self.lbl_Resulte_DateStart = QLabel(self.layoutWidget5)
        self.lbl_Resulte_DateStart.setObjectName(u"lbl_Resulte_DateStart")
        self.lbl_Resulte_DateStart.setFont(font1)

        self.horizontalLayout_5.addWidget(self.lbl_Resulte_DateStart)

        self.label_14 = QLabel(self.layoutWidget5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_14)

        self.lbl_Resulte_DateStart_2 = QLabel(self.layoutWidget5)
        self.lbl_Resulte_DateStart_2.setObjectName(u"lbl_Resulte_DateStart_2")
        self.lbl_Resulte_DateStart_2.setFont(font1)

        self.horizontalLayout_5.addWidget(self.lbl_Resulte_DateStart_2)

        self.layoutWidget6 = QWidget(self.tab_results)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(20, 5, 751, 66))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.layoutWidget6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font: 13pt \"Arial\";")

        self.horizontalLayout_6.addWidget(self.label_20)

        self.date_select_start = QDateTimeEdit(self.layoutWidget6)
        self.date_select_start.setObjectName(u"date_select_start")
        self.date_select_start.setDateTime(QDateTime(QDate(2025, 1, 1), QTime(0, 0, 0)))
        self.date_select_start.setCalendarPopup(True)

        self.horizontalLayout_6.addWidget(self.date_select_start)

        self.label_21 = QLabel(self.layoutWidget6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font: 13pt \"Arial\";")

        self.horizontalLayout_6.addWidget(self.label_21)

        self.date_select_end = QDateTimeEdit(self.layoutWidget6)
        self.date_select_end.setObjectName(u"date_select_end")
        self.date_select_end.setDateTime(QDateTime(QDate(2025, 1, 1), QTime(0, 0, 0)))
        self.date_select_end.setCalendarPopup(True)

        self.horizontalLayout_6.addWidget(self.date_select_end)

        self.btn_LoadDB = QPushButton(self.layoutWidget6)
        self.btn_LoadDB.setObjectName(u"btn_LoadDB")
        self.btn_LoadDB.setStyleSheet(u"font: 18pt \"Arial\";")

        self.horizontalLayout_6.addWidget(self.btn_LoadDB)

        self.tabWidget.addTab(self.tab_results, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e49\u0e32\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e2a\u0e48\u0e27\u0e19\u0e08\u0e33\u0e01\u0e31\u0e14", None))
        self.label_12.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e21\u0e35\u0e48\u0e42\u0e04\u0e23\u0e32\u0e0a\u0e2b\u0e49\u0e32\u0e14\u0e32\u0e27", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23\u0e17\u0e35\u0e48\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01", None))
        self.lbl_dateNow.setText(QCoreApplication.translate("MainWindow", u"XX-XX-XX", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e27\u0e25\u0e32", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48", None))
        self.lbl_Clock.setText(QCoreApplication.translate("MainWindow", u"XX:XX", None))
        self.lbl_CountTotal.setText(QCoreApplication.translate("MainWindow", u"XXXX", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0e08\u0e33\u0e19\u0e27\u0e19\u0e17\u0e35\u0e48\u0e1c\u0e25\u0e34\u0e15\u0e44\u0e14\u0e49", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"(\u0e0a\u0e34\u0e49\u0e19)", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"\u0e2d\u0e31\u0e1e\u0e40\u0e14\u0e15", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"(\u0e27\u0e31\u0e15\u0e15\u0e4c)", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"\u0e08\u0e1a\u0e01\u0e32\u0e23\u0e17\u0e33\u0e07\u0e32\u0e19", None))
        self.lbl_Preformance.setText(QCoreApplication.translate("MainWindow", u"XXX", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e27\u0e32\u0e21\u0e40\u0e23\u0e47\u0e27\u0e43\u0e19\u0e01\u0e32\u0e23\u0e1c\u0e25\u0e34\u0e15", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"(\u0e0a\u0e34\u0e49\u0e19/\u0e19\u0e32\u0e17\u0e35)", None))
        self.lbl_Power.setText(QCoreApplication.translate("MainWindow", u"XXXX", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"(\u0e2b\u0e19\u0e48\u0e27\u0e22)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0e01\u0e33\u0e25\u0e31\u0e07\u0e44\u0e1f\u0e1f\u0e49\u0e32\u0e17\u0e35\u0e48\u0e43\u0e0a\u0e49", None))
        self.lbl_Energy.setText(QCoreApplication.translate("MainWindow", u"XXX", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0e08\u0e33\u0e19\u0e27\u0e19\u0e44\u0e1f\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e17\u0e35\u0e48\u0e43\u0e0a\u0e49", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e23\u0e34\u0e48\u0e21\u0e07\u0e32\u0e19 : ", None))
        self.lbl_StartTime.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), QCoreApplication.translate("MainWindow", u"\u0e2b\u0e19\u0e49\u0e32\u0e2b\u0e25\u0e31\u0e01", None))
        self.btn_Delete.setText(QCoreApplication.translate("MainWindow", u"\u0e25\u0e1a", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e23\u0e38\u0e1b\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25", None))
        self.label_28.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e21\u0e35\u0e48\u0e42\u0e04\u0e23\u0e32\u0e0a\u0e2b\u0e49\u0e32\u0e14\u0e32\u0e27", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e49\u0e32\u0e07\u0e2b\u0e38\u0e49\u0e19\u0e2a\u0e48\u0e27\u0e19\u0e08\u0e33\u0e01\u0e31\u0e14", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0e08\u0e33\u0e19\u0e27\u0e19\u0e17\u0e35\u0e48\u0e1c\u0e25\u0e34\u0e15\u0e44\u0e14\u0e49", None))
        self.lbl_Resulte_TotalCount.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e34\u0e49\u0e19 (\u0e23\u0e27\u0e21)", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0e1e\u0e25\u0e31\u0e07\u0e07\u0e32\u0e19\u0e17\u0e35\u0e48\u0e43\u0e0a\u0e49", None))
        self.lbl_Resulte_power.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0e27\u0e31\u0e15\u0e15\u0e4c( \u0e40\u0e09\u0e25\u0e35\u0e48\u0e22)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e27\u0e32\u0e21\u0e40\u0e23\u0e47\u0e27\u0e43\u0e19\u0e01\u0e32\u0e23\u0e1c\u0e25\u0e34\u0e15", None))
        self.lbl_Resulte_Preformance.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e34\u0e49\u0e19/\u0e19\u0e32\u0e17\u0e35 (\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e19\u0e48\u0e27\u0e22\u0e44\u0e1f\u0e17\u0e35\u0e48\u0e43\u0e0a\u0e49", None))
        self.lbl_Resulte_energy.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e19\u0e48\u0e27\u0e22 (\u0e23\u0e27\u0e21)", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48", None))
        self.lbl_Resulte_DateStart.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u0e16\u0e36\u0e07 ", None))
        self.lbl_Resulte_DateStart_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48", None))
        self.date_select_start.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd  HH:mm", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0e16\u0e36\u0e07", None))
        self.date_select_end.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd  HH:mm", None))
        self.btn_LoadDB.setText(QCoreApplication.translate("MainWindow", u"\u0e42\u0e2b\u0e25\u0e14\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_results), QCoreApplication.translate("MainWindow", u"\u0e2a\u0e23\u0e38\u0e1b", None))
    # retranslateUi

