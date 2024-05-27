from function.Phone_file import Phone
import pyodbc

class PhoneDao:
    def get_phone(self):
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=GIAHANHUYNH;DATABASE=SalesPhone;Trusted_Connection=yes')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM phone")
        phone_row = cursor.fetchall()
        conn.close()
        return phone_row

    def get_phone_by_id(self, phone_id):
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=GIAHANHUYNH;DATABASE=SalesPhone;Trusted_Connection=yes')
        cursor = conn.cursor()
        cursor.execute("SELECT id, phone_name, specifications, photo FROM phone WHERE id = ?", (phone_id,))
        phone_row = cursor.fetchone()
        conn.close()
        return phone_row
