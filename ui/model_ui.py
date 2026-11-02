# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'model.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_ModelPage(object):
    def setupUi(self, ModelPage):
        if not ModelPage.objectName():
            ModelPage.setObjectName(u"ModelPage")
        ModelPage.resize(800, 600)
        self.mainLayout = QVBoxLayout(ModelPage)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(24, 24, 24, 24)
        self.titleLabel = QLabel(ModelPage)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.titleLabel.setFont(font)

        self.mainLayout.addWidget(self.titleLabel)

        self.sourceGroup = QGroupBox(ModelPage)
        self.sourceGroup.setObjectName(u"sourceGroup")
        self.sourceLayout = QVBoxLayout(self.sourceGroup)
        self.sourceLayout.setObjectName(u"sourceLayout")
        self.localRadio = QRadioButton(self.sourceGroup)
        self.localRadio.setObjectName(u"localRadio")
        self.localRadio.setChecked(True)

        self.sourceLayout.addWidget(self.localRadio)

        self.huggingFaceRadio = QRadioButton(self.sourceGroup)
        self.huggingFaceRadio.setObjectName(u"huggingFaceRadio")

        self.sourceLayout.addWidget(self.huggingFaceRadio)

        self.fileLayout = QHBoxLayout()
        self.fileLayout.setObjectName(u"fileLayout")
        self.pathEdit = QLineEdit(self.sourceGroup)
        self.pathEdit.setObjectName(u"pathEdit")

        self.fileLayout.addWidget(self.pathEdit)

        self.browseButton = QPushButton(self.sourceGroup)
        self.browseButton.setObjectName(u"browseButton")

        self.fileLayout.addWidget(self.browseButton)

        self.addButton = QPushButton(self.sourceGroup)
        self.addButton.setObjectName(u"addButton")

        self.fileLayout.addWidget(self.addButton)


        self.sourceLayout.addLayout(self.fileLayout)


        self.mainLayout.addWidget(self.sourceGroup)

        self.modelsLabel = QLabel(ModelPage)
        self.modelsLabel.setObjectName(u"modelsLabel")

        self.mainLayout.addWidget(self.modelsLabel)

        self.modelList = QListWidget(ModelPage)
        QListWidgetItem(self.modelList)
        QListWidgetItem(self.modelList)
        QListWidgetItem(self.modelList)
        self.modelList.setObjectName(u"modelList")

        self.mainLayout.addWidget(self.modelList)

        self.navLayout = QHBoxLayout()
        self.navLayout.setObjectName(u"navLayout")
        self.backButton = QPushButton(ModelPage)
        self.backButton.setObjectName(u"backButton")

        self.navLayout.addWidget(self.backButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.navLayout.addItem(self.horizontalSpacer)

        self.nextButton = QPushButton(ModelPage)
        self.nextButton.setObjectName(u"nextButton")

        self.navLayout.addWidget(self.nextButton)


        self.mainLayout.addLayout(self.navLayout)


        self.retranslateUi(ModelPage)

        QMetaObject.connectSlotsByName(ModelPage)
    # setupUi

    def retranslateUi(self, ModelPage):
        ModelPage.setWindowTitle(QCoreApplication.translate("ModelPage", u"ModelPage", None))
        self.titleLabel.setText(QCoreApplication.translate("ModelPage", u"Choose Model", None))
        self.sourceGroup.setTitle(QCoreApplication.translate("ModelPage", u"Model source", None))
        self.localRadio.setText(QCoreApplication.translate("ModelPage", u"Local file (.gguf)", None))
        self.huggingFaceRadio.setText(QCoreApplication.translate("ModelPage", u"Hugging Face", None))
        self.pathEdit.setPlaceholderText(QCoreApplication.translate("ModelPage", u"Path to a .gguf file", None))
        self.browseButton.setText(QCoreApplication.translate("ModelPage", u"Browse\u2026", None))
        self.addButton.setText(QCoreApplication.translate("ModelPage", u"Add", None))
        self.modelsLabel.setText(QCoreApplication.translate("ModelPage", u"Models to benchmark:", None))

        __sortingEnabled = self.modelList.isSortingEnabled()
        self.modelList.setSortingEnabled(False)
        ___qlistwidgetitem = self.modelList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("ModelPage", u"Llama-3.2-1B-Instruct (Q4_K_M)", None))
        ___qlistwidgetitem1 = self.modelList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("ModelPage", u"Llama-3.2-1B-Instruct (Q8_0)", None))
        ___qlistwidgetitem2 = self.modelList.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("ModelPage", u"Qwen2.5-0.5B-Instruct (Q4_K_M)", None))
        self.modelList.setSortingEnabled(__sortingEnabled)

        self.backButton.setText(QCoreApplication.translate("ModelPage", u"Back", None))
        self.nextButton.setText(QCoreApplication.translate("ModelPage", u"Next", None))
    # retranslateUi

