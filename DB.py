# ###########################################
#       Data Base SQL Class                 #
#       used mysql.comnector library        #
# ###########################################
import mysql.connector

class Database:
    def __init__(self,):
        self.connect_db()
    
    # Connect DB           
    def connect_db(self):
        try:
            self.db = mysql.connector.connect(
                host="localhost",
                user="root",
                password="raspberry",
                #password="p@ssw0rd",
                database="meekorat5dow"
                )     
            self.cursor = self.db.cursor()
            #print("#: Connect SQL Database complete")
        except:
            print("#: Error connecting Database")   
        
    def select_all(self):
        cmd = "SELECT * FROM dataLoger"
        self.cursor.execute(cmd)
        for row in self.cursor.fetchall():
            print (row)
    
    def query(self,cmd):
        self.cursor.execute(cmd)
        return self.cursor.fetchall()
    
    def record(self,val):
        # (`orderID`, `weight`, `basketNumber`, `grade`, `materialType`, `staffID`, `customerID`, `building`, `container`) VALUES ('20250304002', '21', '02', 'B', 'buriram', '0010', '102', 'A', 'basket');
        sql = "INSERT INTO dataLoger (start_time, total_product, preformance, power,energy) VALUES " + str(val)
        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor.fetchall()
    
    
if __name__ == "__main__":
    db = Database()
    
    val = ("13:55:00","12","8.1","8.1","0.0")
    #sql = "INSERT INTO dataLoger (start_time, total_product, preformance, power,energy) VALUES " + str(val)
    #db.query(sql)  
    db.record(val)     
    db.select_all()
    
    