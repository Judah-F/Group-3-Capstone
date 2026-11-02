# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_HomePage(object):
    def setupUi(self, HomePage):
        if not HomePage.objectName():
            HomePage.setObjectName(u"HomePage")
        HomePage.resize(800, 600)
        self.mainLayout = QVBoxLayout(HomePage)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(24, 24, 24, 24)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.verticalSpacer)

        self.titleLabel = QLabel(HomePage)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.titleLabel.setFont(font)

        self.mainLayout.addWidget(self.titleLabel, 0, Qt.AlignHCenter)

        self.descriptionLabel = QLabel(HomePage)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.mainLayout.addWidget(self.descriptionLabel, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.mainLayout.addItem(self.verticalSpacer_2)

        self.chooseModelButton = QPushButton(HomePage)
        self.chooseModelButton.setObjectName(u"chooseModelButton")
        self.chooseModelButton.setMinimumSize(QSize(0, 36))
        self.chooseModelButton.setMinimumSize(QSize(200, 0))
        self.chooseModelButton.setMaximumSize(QSize(200, 16777215))

        self.mainLayout.addWidget(self.chooseModelButton, 0, Qt.AlignHCenter)

        self.viewResultsButton = QPushButton(HomePage)
        self.viewResultsButton.setObjectName(u"viewResultsButton")
        self.viewResultsButton.setMinimumSize(QSize(0, 36))
        self.viewResultsButton.setMinimumSize(QSize(200, 0))
        self.viewResultsButton.setMaximumSize(QSize(200, 16777215))

        self.mainLayout.addWidget(self.viewResultsButton, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.verticalSpacer_3)


        self.retranslateUi(HomePage)

        QMetaObject.connectSlotsByName(HomePage)
    # setupUi

    def retranslateUi(self, HomePage):
        HomePage.setWindowTitle(QCoreApplication.translate("HomePage", u"HomePage", None))
        self.titleLabel.setText(QCoreApplication.translate("HomePage", u"Edge LLM Benchmark", None))
        self.descriptionLabel.setText(QCoreApplication.translate("HomePage", u"Benchmark language models on this device and compare the results.", None))
        self.chooseModelButton.setText(QCoreApplication.translate("HomePage", u"Choose Model", None))
        self.viewResultsButton.setText(QCoreApplication.translate("HomePage", u"View Results", None))
    # retranslateUi

