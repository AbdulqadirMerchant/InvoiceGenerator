from PySide6.QtWidgets import QDialog, QTableWidgetItem
from retrieve_invoice import Ui_Retrieve_Invoice

class RetrieveInvoiceWindow(QDialog):
    def __init__(self, client_data):
        super().__init__()
        self.ui = Ui_Retrieve_Invoice()
        self.ui.setupUi(self)
        self.client_data = client_data

        #Retrieve all the present customer names
        self.ui.customerNameCombo.addItems(list(self.client_data.keys()))
        self.ui.customerNameCombo.currentIndexChanged.connect(self.changeInvoices)

        invoices = [str(row[0]) for row in self.client_data[self.ui.customerNameCombo.currentText()]]
        self.ui.invoiceIdCombo.addItems(list(set(invoices)))
        self.ui.invoiceIdCombo.currentIndexChanged.connect(self.loadTable)
        self.ui.invoiceIdCombo.setCurrentText("1")
        self.loadTable()

    def changeInvoices(self):
        #Retrieve the invoices of each customer
        #list(set()) makes the items of the list unique
        self.ui.invoiceIdCombo.clear()
        invoices = [str(row[0]) for row in self.client_data[self.ui.customerNameCombo.currentText()]]
        self.ui.invoiceIdCombo.addItems(list(set(invoices)))
        self.ui.invoiceIdCombo.currentIndexChanged.connect(self.loadTable)

    def loadTable(self):
        self.ui.invoiceTable.clearContents()
        self.ui.invoiceTable.setRowCount(0)

        row_count = self.ui.invoiceTable.rowCount()

        client_name = self.ui.customerNameCombo.currentText()
        id = self.ui.invoiceIdCombo.currentText()

        for key, value in self.client_data.items():
            for row in value:
                if client_name == key and str(row[0]) == id:
                    self.ui.invoiceTable.insertRow(row_count)

                    self.ui.invoiceTable.setItem(row_count, 0, QTableWidgetItem(str(row[1])))
                    self.ui.invoiceTable.setItem(row_count, 1, QTableWidgetItem(str(row[2])))
                    self.ui.invoiceTable.setItem(row_count, 2, QTableWidgetItem(str(row[3])))
                    self.ui.invoiceTable.setItem(row_count, 3, QTableWidgetItem(str(row[4])))
                    self.ui.invoiceTable.setItem(row_count, 4, QTableWidgetItem(str(row[5])))

            row_count = self.ui.invoiceTable.rowCount()



