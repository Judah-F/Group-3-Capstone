# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'results.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ResultsPage(object):
    def setupUi(self, ResultsPage):
        if not ResultsPage.objectName():
            ResultsPage.setObjectName(u"ResultsPage")
        ResultsPage.resize(800, 600)
        self.mainLayout = QVBoxLayout(ResultsPage)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(24, 24, 24, 24)
        self.titleLabel = QLabel(ResultsPage)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.titleLabel.setFont(font)

        self.mainLayout.addWidget(self.titleLabel)

        self.chartFrame = QFrame(ResultsPage)
        self.chartFrame.setObjectName(u"chartFrame")
        self.chartFrame.setFrameShape(QFrame.StyledPanel)
        self.chartFrame.setMinimumSize(QSize(0, 300))
        self.chartLayout = QVBoxLayout(self.chartFrame)
        self.chartLayout.setObjectName(u"chartLayout")
        self.chartPlaceholderLabel = QLabel(self.chartFrame)
        self.chartPlaceholderLabel.setObjectName(u"chartPlaceholderLabel")
        self.chartPlaceholderLabel.setAlignment(Qt.AlignCenter)

        self.chartLayout.addWidget(self.chartPlaceholderLabel)


        self.mainLayout.addWidget(self.chartFrame)

        self.navLayout = QHBoxLayout()
        self.navLayout.setObjectName(u"navLayout")
        self.homeButton = QPushButton(ResultsPage)
        self.homeButton.setObjectName(u"homeButton")

        self.navLayout.addWidget(self.homeButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.navLayout.addItem(self.horizontalSpacer)

        self.newBenchmarkButton = QPushButton(ResultsPage)
        self.newBenchmarkButton.setObjectName(u"newBenchmarkButton")

        self.navLayout.addWidget(self.newBenchmarkButton)


        self.mainLayout.addLayout(self.navLayout)

        self.mainLayout.setStretch(1, 1)

        self.retranslateUi(ResultsPage)

        QMetaObject.connectSlotsByName(ResultsPage)
    # setupUi

    def retranslateUi(self, ResultsPage):
        ResultsPage.setWindowTitle(QCoreApplication.translate("ResultsPage", u"ResultsPage", None))
        self.titleLabel.setText(QCoreApplication.translate("ResultsPage", u"Results", None))
        self.chartPlaceholderLabel.setText(QCoreApplication.translate("ResultsPage", u"Chart goes here", None))
        self.homeButton.setText(QCoreApplication.translate("ResultsPage", u"Home", None))
        self.newBenchmarkButton.setText(QCoreApplication.translate("ResultsPage", u"New Benchmark", None))
    # retranslateUi

