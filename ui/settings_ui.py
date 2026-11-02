from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_SettingsPage(object):
    def setupUi(self, SettingsPage):
        if not SettingsPage.objectName():
            SettingsPage.setObjectName(u"SettingsPage")
        SettingsPage.resize(800, 600)
        self.mainLayout = QVBoxLayout(SettingsPage)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(24, 24, 24, 24)
        self.titleLabel = QLabel(SettingsPage)
        self.titleLabel.setObjectName(u"titleLabel")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.titleLabel.setFont(font)

        self.mainLayout.addWidget(self.titleLabel)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.backendLabel = QLabel(SettingsPage)
        self.backendLabel.setObjectName(u"backendLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.backendLabel)

        self.backendCombo = QComboBox(SettingsPage)
        self.backendCombo.addItem("")
        self.backendCombo.addItem("")
        self.backendCombo.setObjectName(u"backendCombo")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.backendCombo)

        self.promptLabel = QLabel(SettingsPage)
        self.promptLabel.setObjectName(u"promptLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.promptLabel)

        self.promptSpin = QSpinBox(SettingsPage)
        self.promptSpin.setObjectName(u"promptSpin")
        self.promptSpin.setMinimum(1)
        self.promptSpin.setMaximum(8192)
        self.promptSpin.setValue(512)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.promptSpin)

        self.outputLabel = QLabel(SettingsPage)
        self.outputLabel.setObjectName(u"outputLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.outputLabel)

        self.outputSpin = QSpinBox(SettingsPage)
        self.outputSpin.setObjectName(u"outputSpin")
        self.outputSpin.setMinimum(1)
        self.outputSpin.setMaximum(4096)
        self.outputSpin.setValue(128)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.outputSpin)

        self.passesLabel = QLabel(SettingsPage)
        self.passesLabel.setObjectName(u"passesLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.passesLabel)

        self.passesSpin = QSpinBox(SettingsPage)
        self.passesSpin.setObjectName(u"passesSpin")
        self.passesSpin.setMinimum(1)
        self.passesSpin.setMaximum(50)
        self.passesSpin.setValue(5)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.passesSpin)

        self.tempLimitLabel = QLabel(SettingsPage)
        self.tempLimitLabel.setObjectName(u"tempLimitLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.tempLimitLabel)

        self.tempLimitSpin = QSpinBox(SettingsPage)
        self.tempLimitSpin.setObjectName(u"tempLimitSpin")
        self.tempLimitSpin.setMinimum(40)
        self.tempLimitSpin.setMaximum(110)
        self.tempLimitSpin.setValue(85)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.tempLimitSpin)


        self.mainLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.verticalSpacer)

        self.navLayout = QHBoxLayout()
        self.navLayout.setObjectName(u"navLayout")
        self.backButton = QPushButton(SettingsPage)
        self.backButton.setObjectName(u"backButton")

        self.navLayout.addWidget(self.backButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.navLayout.addItem(self.horizontalSpacer)

        self.startButton = QPushButton(SettingsPage)
        self.startButton.setObjectName(u"startButton")

        self.navLayout.addWidget(self.startButton)


        self.mainLayout.addLayout(self.navLayout)


        self.retranslateUi(SettingsPage)

        QMetaObject.connectSlotsByName(SettingsPage)

    def retranslateUi(self, SettingsPage):
        SettingsPage.setWindowTitle(QCoreApplication.translate("SettingsPage", u"SettingsPage", None))
        self.titleLabel.setText(QCoreApplication.translate("SettingsPage", u"Benchmark Settings", None))
        self.backendLabel.setText(QCoreApplication.translate("SettingsPage", u"Backend", None))
        self.backendCombo.setItemText(0, QCoreApplication.translate("SettingsPage", u"CPU", None))
        self.backendCombo.setItemText(1, QCoreApplication.translate("SettingsPage", u"GPU", None))

        self.promptLabel.setText(QCoreApplication.translate("SettingsPage", u"Prompt length (tokens)", None))
        self.outputLabel.setText(QCoreApplication.translate("SettingsPage", u"Output length (tokens)", None))
        self.passesLabel.setText(QCoreApplication.translate("SettingsPage", u"Measured passes", None))
        self.tempLimitLabel.setText(QCoreApplication.translate("SettingsPage", u"Temperature limit (\u00b0C)", None))
        self.backButton.setText(QCoreApplication.translate("SettingsPage", u"Back", None))
        self.startButton.setText(QCoreApplication.translate("SettingsPage", u"Start Benchmark", None))

