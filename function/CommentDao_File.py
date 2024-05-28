import pyodbc
from function.Comment_file import Comment
from function.User_file import User
class CommentDao:
    def insert_comment(self,user:User,comment:Comment):
            if user.getUserId !=None:
                conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO comment (user_id, comment) VALUES (?, ?)",(user.getUserId,comment.getComment))
                conn.commit() 
                conn.close()
            else:
                print("User not found.")
    def get_comment_by_user(self):
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes')
        cursor = conn.cursor()
        cursor.execute("SELECT comment FROM comment")
        comments = cursor.fetchall()
        return comments
    def get_comment_id_by_user(self,comment:Comment):
        conn=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes')
        cursor=conn.cursor()
        query=f"select distinct(id) From comment where comment=N'{comment.getComment}'"
        print(query)
        cursor.execute(f"select distinct(id) From comment where comment=N'{comment.getComment}'")
        comment_id=cursor.fetchone()
        return comment_id [0] if comment_id else None
    def update_comment(self,comment:Comment,user:User):
        if user !=None:
            comment_id=self.get_comment_id_by_user(comment)
            conn=pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=MSI;DATABASE=SalesPhone;Trusted_Connection=yes")
            cursor=conn.cursor()
            cursor.execute("Update Comment set predict = ? where id= ?",(comment.getPredict,comment_id))
            conn.commit()
            conn.close()
        else: 
            print("User not found")