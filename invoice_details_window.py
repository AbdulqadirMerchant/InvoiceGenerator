from PyQt6.QtWidgets import QMessageBox
from PySide6.QtWidgets import (QDialog, QTableWidgetItem)
from PySide6.QtGui import QPixmap

from invoice_details import Ui_Invoice_Details
from final_invoice_window import FinalInvoiceWindow

invoice_details = []
product_price_dict = {"Product 101": "100", "Product 102": "200", "Product 103": "300",
                      "Product 104": "400", "Product 105": "500", "Product 106": "600",
                      "Product 107": "700", "Product 108": "800"}

class InvoiceDetailsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Invoice_Details()
        self.ui.setupUi(self)

        #Load company logo
        self.ui.logo.setPixmap(QPixmap("tesla_logo.png"))
        self.ui.logo.setScaledContents(True)

        self.ui.addProductButton.clicked.connect(self.addRow)
        self.ui.generateInvoiceButton.clicked.connect(self.load_final_invoice)
        self.ui.productCategory.currentIndexChanged.connect(self.changePrice)

    def changePrice(self):
        current_product = self.ui.productCategory.currentText()
        self.ui.priceValue.setText(str(product_price_dict[current_product]))

    def addRow(self):
        product_name = self.ui.productCategory.currentText()
        price = product_price_dict[product_name]
        quantity = self.ui.quantityProduct.text()
        discount = self.ui.discountValue.text()

        if quantity == "" or not quantity.isdigit():
            infoBox = QMessageBox()
            infoBox.setWindowTitle("Invalid input")
            infoBox.setText("Please enter the right quantity")
            infoBox.exec()
            return

        discount = "0" if (discount == "" or not discount.isdigit()) else discount
        amount = str(int(price) * int(quantity) - int(discount))

        productsInInvoice = {details["Product Name"] for details in invoice_details}
        row_count = self.ui.tableWidget.rowCount()  # Get current row count

        if product_name not in productsInInvoice:
            self.ui.tableWidget.insertRow(row_count) #Insert a new row

            #Add sample data to the new row
            self.ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(product_name))
            self.ui.tableWidget.setItem(row_count, 1, QTableWidgetItem(price))
            self.ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(quantity))
            self.ui.tableWidget.setItem(row_count, 3, QTableWidgetItem(discount))
            self.ui.tableWidget.setItem(row_count, 4, QTableWidgetItem(amount))
            invoice_details.append({"Product Name":product_name, "Price": price, "Quantity": quantity,
                                    "Discount": discount, "Amount": int(amount)})

        else:
            for details in invoice_details:
                if details["Product Name"] == product_name:
                    cur_quantity = int(details["Quantity"])
                    cur_discount = int(details["Discount"])
                    cur_amount = details["Amount"]

                    total_quantity = cur_quantity + int(quantity)
                    total_discount = cur_discount + int(discount)
                    total_amount = cur_amount + int(amount)

                    details["Quantity"] = str(total_quantity)
                    details["Discount"] = str(total_discount)
                    details["Amount"] = total_amount

            self.ui.tableWidget.setItem(row_count - 1, 2, QTableWidgetItem(str(total_quantity)))
            self.ui.tableWidget.setItem(row_count - 1, 3, QTableWidgetItem(str(total_discount)))
            self.ui.tableWidget.setItem(row_count - 1, 4, QTableWidgetItem(str(total_amount)))


        #Generates the total sum of all the items
        self.ui.amountValue.setText(str(sum([details["Amount"] for details in invoice_details])))

    def load_final_invoice(self):
        client_name = self.ui.clientNameInfo.text()

        if not client_name:
            infoBox = QMessageBox()
            infoBox.setWindowTitle("Missing client info")
            infoBox.setText("Client name is necessary to generate invoice!")
            infoBox.exec()
            return

        self.final_invoice_window = FinalInvoiceWindow(invoice_details, client_name)

        # Load all invoice info into the final invoice window
        self.final_invoice_window.ui.companyName.setText(self.ui.companyName.text())
        self.final_invoice_window.ui.companyAddress.setText(self.ui.companyAddress.text())
        self.final_invoice_window.ui.companyEmail.setText(self.ui.companyEmail.text())
        self.final_invoice_window.ui.companyPhone.setText(self.ui.companyPhone.text())
        self.final_invoice_window.ui.clientNameValue.setText(self.ui.clientNameInfo.text())

        if self.ui.logo.pixmap():
            self.final_invoice_window.ui.logo.setPixmap(self.ui.logo.pixmap())
            self.final_invoice_window.ui.logo.setScaledContents(True)

        total_amount = 0
        total_discount = 0

        for details in invoice_details:
            row_count = self.final_invoice_window.ui.tableWidget.rowCount()
            self.final_invoice_window.ui.tableWidget.insertRow(row_count)

            self.final_invoice_window.ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(details["Product Name"]))
            self.final_invoice_window.ui.tableWidget.setItem(row_count, 1, QTableWidgetItem(details["Price"]))
            self.final_invoice_window.ui.tableWidget.setItem(row_count, 2, QTableWidgetItem(details["Quantity"]))
            self.final_invoice_window.ui.tableWidget.setItem(row_count, 3, QTableWidgetItem(details["Discount"]))
            self.final_invoice_window.ui.tableWidget.setItem(row_count, 4, QTableWidgetItem(str(details["Amount"])))

            total_amount += details["Amount"]
            total_discount += int(details["Discount"])

        self.final_invoice_window.ui.totalAmountValue.setText(str(total_amount + total_discount))
        self.final_invoice_window.ui.discountValue.setText(str(total_discount))
        self.final_invoice_window.ui.totalValue.setText(str(total_amount))

        #Resetting the window
        self.ui.clientNameInfo.setText("")
        self.ui.quantityProduct.setText("")
        self.ui.discountValue.setText("")
        self.ui.amountValue.setText("0")
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)

        self.final_invoice_window.show()