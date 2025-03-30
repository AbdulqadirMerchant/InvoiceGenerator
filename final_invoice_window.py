from PyQt6.QtWidgets import QMessageBox
from PySide6.QtWidgets import QDialog

from final_invoice import Ui_Final_Invoice
from retrieve_invoice_window import RetrieveInvoiceWindow
import mysql.connector

"""
The table name is named 'customer_data'
It has the following definition:
client_name: VARCHAR(30)
ID: SMALLINT
Product_name: VARCHAR(30)
Price: INT
Quantity: INT
Discount: INT
Amount: INT
PRIMARY KEY(client_name, ID, Product_name)

Each client_name and its respective id represents one unique invoice
The same client_name with a different id represents a different invoice of the same customer
"""

class FinalInvoiceWindow(QDialog):
    def __init__(self, invoice_details, client_name):
        super().__init__()
        self.ui = Ui_Final_Invoice()
        self.ui.setupUi(self)
        self.invoice_details = invoice_details
        self.client_name = client_name
        client_list = []

        try:
            self.connection = mysql.connector.connect(host="localhost", user="root", password="<dbpassword>",
                                                 database="<dbname>")
            self.cursor = self.connection.cursor()

        except ConnectionError as e:
            print("Connection to Database Failed!")
            return

        self.cursor.execute("SELECT client_name FROM customer_data")
        for client in self.cursor.fetchall():
            client_list.append(client[0])
        client_list = list(set(client_list))
        self.client_data = {key:[] for key in client_list}

        self.cursor.execute("SELECT * FROM customer_data")
        data = self.cursor.fetchall()
        for client, value in self.client_data.items():
            index = 0
            for row in data:
                if row[0] == client:
                    value.append([row[1], row[2], row[3], row[4], row[5], row[6]])

        self.ui.retrieveInvoiceButton.clicked.connect(self.getInvoicesFromDB)
        self.ui.uploadToDBButton.clicked.connect(self.sendToDatabase)

    def getInvoicesFromDB(self):
        if len(self.client_data) == 0:
            infobox = QMessageBox()
            infobox.setWindowTitle("Empty Database")
            infobox.setText("Please add something to the database first")
            infobox.exec()
            return
        self.retrieve_invoice_window = RetrieveInvoiceWindow(self.client_data)
        
        self.retrieve_invoice_window.ui.companyName.setText(self.ui.companyName.text())
        self.retrieve_invoice_window.ui.companyAddress.setText(self.ui.companyAddress.text())
        self.retrieve_invoice_window.ui.companyEmail.setText(self.ui.companyEmail.text())
        self.retrieve_invoice_window.ui.companyPhone.setText(self.ui.companyPhone.text())

        if self.ui.logo.pixmap():
            self.retrieve_invoice_window.ui.logo.setPixmap(self.ui.logo.pixmap())
            self.retrieve_invoice_window.ui.logo.setScaledContents(True)

        self.retrieve_invoice_window.show()
        self.close()

    def sendToDatabase(self):
        if self.client_name in self.client_data:
            #Retrieves the id of the last invoice of the customer and adds + 1 to it to represent a new invoice
            invoice_id = self.client_data[self.client_name][-1][0] + 1

        else:
            self.client_data[self.client_name] = []
            invoice_id = 1

        for details in self.invoice_details:
            self.cursor.execute("INSERT INTO customer_data VALUES(%s, %s, %s, %s, %s, %s, %s)",
                                (self.client_name, invoice_id, details["Product Name"],
                                int(details["Price"]), int(details["Quantity"]), int(details["Discount"]),
                                details["Amount"]))

            #Adding it to the client data dictionary as well
            self.client_data[self.client_name].append([invoice_id, details["Product Name"],
                                int(details["Price"]), int(details["Quantity"]), int(details["Discount"]),
                                details["Amount"]])
        try:
            self.connection.commit()
            infobox = QMessageBox()
            infobox.setWindowTitle("Info")
            infobox.setText("Commit Successful. Data Uploaded to database successfully!")
            infobox.exec()
        except ConnectionError as e:
            infobox = QMessageBox()
            infobox.setWindowTitle("Error")
            infobox.setText("Failed to commit to database. Please try again")
            infobox.exec()
            return

        self.ui.uploadToDBButton.setEnabled(False)
        self.invoice_details.clear()
    
    #So that the information is cleared even if the changes are not committed to the database
    def closeEvent(self, event):
        self.invoice_details.clear()

    def __del__(self):
        self.connection.close()
        self.cursor.close()
