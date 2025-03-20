from invoice_details_window import InvoiceDetailsWindow
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InvoiceDetailsWindow()
    window.show()
    sys.exit(app.exec())