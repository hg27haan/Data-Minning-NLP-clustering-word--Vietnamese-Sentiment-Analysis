import pyodbc
from function.Phone_file import Phone
class PhoneDao:
    def get_phone_name(self):
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=GIAHANHUYNH;DATABASE=SalesPhone;Trusted_Connection=yes')
        cursor = conn.cursor()
        cursor.execute(f"select phone_name From phone")
        phone_row = cursor.fetchall()
        conn.close()
        return phone_row