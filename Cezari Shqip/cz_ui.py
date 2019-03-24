from PyQt5 import QtCore, QtGui, QtWidgets
import cazari_sq

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(263, 345)
        self.bottom = QtWidgets.QDialogButtonBox(Dialog)
        self.bottom.setGeometry(QtCore.QRect(30, 290, 201, 41))
        self.bottom.setOrientation(QtCore.Qt.Horizontal)
        self.bottom.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Reset)
        self.bottom.setObjectName("bottom")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 241, 272))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.title_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.title_text.setAlignment(QtCore.Qt.AlignCenter)
        self.title_text.setObjectName("title_text")
        self.horizontalLayout_3.addWidget(self.title_text)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.directory_field = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.directory_field.setInputMask("")
        self.directory_field.setText("")
        self.directory_field.setObjectName("directory_field")
        self.verticalLayout.addWidget(self.directory_field)
        self.browse_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.browse_button.setEnabled(False)
        self.browse_button.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.browse_button.setObjectName("browse_button")
        self.verticalLayout.addWidget(self.browse_button)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_qelesi = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_qelesi.setObjectName("label_qelesi")
        self.horizontalLayout_2.addWidget(self.label_qelesi)
        self.qelesi = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.qelesi.setWrapping(False)
        self.qelesi.setFrame(True)
        self.qelesi.setReadOnly(False)
        self.qelesi.setProperty("value", 2)
        self.qelesi.setDisplayIntegerBase(35)
        self.qelesi.setObjectName("qelesi")
        self.horizontalLayout_2.addWidget(self.qelesi)
        self.encrypt_radio = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.encrypt_radio.setEnabled(True)
        self.encrypt_radio.setCheckable(True)
        self.encrypt_radio.setChecked(True)
        self.encrypt_radio.setObjectName("encrypt_radio")
        self.horizontalLayout_2.addWidget(self.encrypt_radio, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.write_path_text = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.write_path_text.setMinimumSize(QtCore.QSize(227, 45))
        self.write_path_text.setMaximumSize(QtCore.QSize(15777215, 15777215))
        self.write_path_text.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.write_path_text.setObjectName("write_path_text")
        self.verticalLayout.addWidget(self.write_path_text)
        self.save_path_field = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.save_path_field.setObjectName("save_path_field")
        self.verticalLayout.addWidget(self.save_path_field)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filename_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.filename_label.setObjectName("filename_label")
        self.horizontalLayout.addWidget(self.filename_label)
        self.filename_field = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.filename_field.setObjectName("filename_field")
        self.horizontalLayout.addWidget(self.filename_field)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.save_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save_button.setObjectName("save_button")
        self.verticalLayout.addWidget(self.save_button)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(120, 290, 20, 71))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(Dialog)
        self.bottom.accepted.connect(Dialog.accept)
        self.bottom.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.save_button.clicked.connect(self.enkripto)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title_text.setText(_translate("Dialog", "Cezar Cipher in Albanian alphabet"))
        self.browse_button.setText(_translate("Dialog", "Browse"))
        self.label_qelesi.setText(_translate("Dialog", "Qelsi:"))
        self.encrypt_radio.setText(_translate("Dialog", "Encrypt"))
        self.write_path_text.setText(_translate("Dialog", "Write Save As Path:"))
        self.filename_label.setText(_translate("Dialog", "File Name"))
        self.save_button.setText(_translate("Dialog", "Save"))
    
    def enkripto(self):
        directory =r'%s' %self.directory_field.text()
        print('direktoria u murr: ', directory)
        #encrypt_radio = True
        
        qelesi = self.qelesi.value()
        print('qelesi u murr', str(qelesi))
        try:
            print('trying')
            cazari_sq.enkripto_dokumentin(directory, qelesi, True)
        except Exception as e:
            print('Not working check fields...')
            print(e)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

