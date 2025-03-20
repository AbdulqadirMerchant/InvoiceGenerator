# Form implementation generated from reading ui file '.\UI_Files\invoice_details.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_Invoice_Details(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(639, 750)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        Dialog.setFont(font)
        Dialog.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.logo = QtWidgets.QLabel(parent=Dialog)
        self.logo.setGeometry(QtCore.QRect(520, 20, 71, 91))
        self.logo.setObjectName("logo")
        self.companyName = QtWidgets.QLabel(parent=Dialog)
        self.companyName.setGeometry(QtCore.QRect(20, 20, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(True)
        self.companyName.setFont(font)
        self.companyName.setObjectName("companyName")
        self.companyPhone = QtWidgets.QLabel(parent=Dialog)
        self.companyPhone.setGeometry(QtCore.QRect(20, 80, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.companyPhone.setFont(font)
        self.companyPhone.setObjectName("companyPhone")
        self.companyEmail = QtWidgets.QLabel(parent=Dialog)
        self.companyEmail.setGeometry(QtCore.QRect(20, 110, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.companyEmail.setFont(font)
        self.companyEmail.setObjectName("companyEmail")
        self.companyAddress = QtWidgets.QLabel(parent=Dialog)
        self.companyAddress.setGeometry(QtCore.QRect(20, 50, 261, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.companyAddress.setFont(font)
        self.companyAddress.setObjectName("companyAddress")
        self.productNameLabel = QtWidgets.QLabel(parent=Dialog)
        self.productNameLabel.setGeometry(QtCore.QRect(40, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        self.productNameLabel.setFont(font)
        self.productNameLabel.setObjectName("productNameLabel")
        self.productCategory = QtWidgets.QComboBox(parent=Dialog)
        self.productCategory.setGeometry(QtCore.QRect(190, 190, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.productCategory.setFont(font)
        self.productCategory.setObjectName("productCategory")
        self.productCategory.addItem("")
        self.productCategory.addItem("")
        self.productCategory.addItem("")
        self.productCategory.addItem("")
        self.productCategory.addItem("")
        self.productCategory.addItem("")
        self.productCategory.addItem("")
        self.productCategory.addItem("")
        self.priceLabel = QtWidgets.QLabel(parent=Dialog)
        self.priceLabel.setGeometry(QtCore.QRect(380, 190, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        self.priceLabel.setFont(font)
        self.priceLabel.setObjectName("priceLabel")
        self.line_4 = QtWidgets.QFrame(parent=Dialog)
        self.line_4.setGeometry(QtCore.QRect(0, 150, 221, 16))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_4.setLineWidth(3)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setObjectName("line_4")
        self.salesInvoiceLabel = QtWidgets.QLabel(parent=Dialog)
        self.salesInvoiceLabel.setGeometry(QtCore.QRect(230, 140, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        font.setBold(True)
        self.salesInvoiceLabel.setFont(font)
        self.salesInvoiceLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.salesInvoiceLabel.setObjectName("salesInvoiceLabel")
        self.line_5 = QtWidgets.QFrame(parent=Dialog)
        self.line_5.setGeometry(QtCore.QRect(400, 150, 231, 16))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_5.setLineWidth(3)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_5.setObjectName("line_5")
        self.quantityLabel = QtWidgets.QLabel(parent=Dialog)
        self.quantityLabel.setGeometry(QtCore.QRect(380, 230, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        self.quantityLabel.setFont(font)
        self.quantityLabel.setObjectName("quantityLabel")
        self.quantityProduct = QtWidgets.QLineEdit(parent=Dialog)
        self.quantityProduct.setGeometry(QtCore.QRect(470, 230, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.quantityProduct.setFont(font)
        self.quantityProduct.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.quantityProduct.setObjectName("quantityProduct")
        self.line_3 = QtWidgets.QFrame(parent=Dialog)
        self.line_3.setGeometry(QtCore.QRect(10, 370, 631, 16))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_3.setLineWidth(3)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setObjectName("line_3")
        self.addProductButton = QtWidgets.QPushButton(parent=Dialog)
        self.addProductButton.setGeometry(QtCore.QRect(460, 320, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.addProductButton.setFont(font)
        self.addProductButton.setObjectName("addProductButton")
        self.tableWidget = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 400, 621, 281))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget.verticalHeader().setVisible(False)
        self.generateInvoiceButton = QtWidgets.QPushButton(parent=Dialog)
        self.generateInvoiceButton.setGeometry(QtCore.QRect(230, 690, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.generateInvoiceButton.setFont(font)
        self.generateInvoiceButton.setObjectName("generateInvoiceButton")
        self.clientNameInfo = QtWidgets.QLineEdit(parent=Dialog)
        self.clientNameInfo.setGeometry(QtCore.QRect(180, 270, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.clientNameInfo.setFont(font)
        self.clientNameInfo.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.clientNameInfo.setObjectName("clientNameInfo")
        self.clientName = QtWidgets.QLabel(parent=Dialog)
        self.clientName.setGeometry(QtCore.QRect(40, 270, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        self.clientName.setFont(font)
        self.clientName.setObjectName("clientName")
        self.amountLabel = QtWidgets.QLabel(parent=Dialog)
        self.amountLabel.setGeometry(QtCore.QRect(40, 320, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        self.amountLabel.setFont(font)
        self.amountLabel.setObjectName("amountLabel")
        self.amountValue = QtWidgets.QLabel(parent=Dialog)
        self.amountValue.setGeometry(QtCore.QRect(130, 320, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        self.amountValue.setFont(font)
        self.amountValue.setObjectName("amountValue")
        self.discountValue = QtWidgets.QLineEdit(parent=Dialog)
        self.discountValue.setGeometry(QtCore.QRect(470, 270, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.discountValue.setFont(font)
        self.discountValue.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly)
        self.discountValue.setText("")
        self.discountValue.setObjectName("discountValue")
        self.discountLabel = QtWidgets.QLabel(parent=Dialog)
        self.discountLabel.setGeometry(QtCore.QRect(380, 270, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        self.discountLabel.setFont(font)
        self.discountLabel.setObjectName("discountLabel")
        self.priceValue = QtWidgets.QLabel(parent=Dialog)
        self.priceValue.setGeometry(QtCore.QRect(470, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift")
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        self.priceValue.setFont(font)
        self.priceValue.setObjectName("priceValue")
        self.productNameLabel.setBuddy(self.productCategory)
        self.quantityLabel.setBuddy(self.quantityProduct)
        self.clientName.setBuddy(self.clientNameInfo)
        self.discountLabel.setBuddy(self.discountValue)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.productCategory, self.quantityProduct)
        Dialog.setTabOrder(self.quantityProduct, self.discountValue)
        Dialog.setTabOrder(self.discountValue, self.clientNameInfo)
        Dialog.setTabOrder(self.clientNameInfo, self.addProductButton)
        Dialog.setTabOrder(self.addProductButton, self.tableWidget)
        Dialog.setTabOrder(self.tableWidget, self.generateInvoiceButton)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Invoice Details"))
        self.logo.setText(_translate("Dialog", "LOGO"))
        self.companyName.setText(_translate("Dialog", "Tesla Inc"))
        self.companyPhone.setText(_translate("Dialog", "(877) 798-3752"))
        self.companyEmail.setText(_translate("Dialog", "apacpress@tesla.com"))
        self.companyAddress.setText(_translate("Dialog", "1 Tesla Road, Austin, TX 78725"))
        self.productNameLabel.setText(_translate("Dialog", "Product Name:"))
        self.productCategory.setItemText(0, _translate("Dialog", "Product 101"))
        self.productCategory.setItemText(1, _translate("Dialog", "Product 102"))
        self.productCategory.setItemText(2, _translate("Dialog", "Product 103"))
        self.productCategory.setItemText(3, _translate("Dialog", "Product 104"))
        self.productCategory.setItemText(4, _translate("Dialog", "Product 105"))
        self.productCategory.setItemText(5, _translate("Dialog", "Product 106"))
        self.productCategory.setItemText(6, _translate("Dialog", "Product 107"))
        self.productCategory.setItemText(7, _translate("Dialog", "Product 108"))
        self.priceLabel.setText(_translate("Dialog", "Price:"))
        self.salesInvoiceLabel.setText(_translate("Dialog", "Sales Invoice"))
        self.quantityLabel.setText(_translate("Dialog", "Quantity:"))
        self.addProductButton.setText(_translate("Dialog", "Add Product"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Product"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Price"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Discount"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Amount"))
        self.generateInvoiceButton.setText(_translate("Dialog", "Generate Invoice"))
        self.clientName.setText(_translate("Dialog", "Client Name:"))
        self.amountLabel.setText(_translate("Dialog", "Amount:"))
        self.amountValue.setText(_translate("Dialog", "0"))
        self.discountLabel.setText(_translate("Dialog", "Discount:"))
        self.priceValue.setText(_translate("Dialog", "100"))
