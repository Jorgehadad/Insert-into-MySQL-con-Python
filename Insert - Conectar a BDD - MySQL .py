import pymysql
import string
import random

class DataBase:
    def __init__ (self):
        self.connection = pymysql.connect(
            host= 'localhost',
            user= 'root',
            password= 'admin',
            db = 'tpi2021'
        )

        self.cursor = self.connection.cursor()

        print ("Conexión exitosa!")

    def select_user (self,id):
        sql= 'SELECT id, username, email FROM users WHERE id = {}'.format(id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            print("Id: ", user[0])
            print("Username: ", user[1])
            print("Email: ", user[2])
        except Exception as e:
            raise

    def select_all_users(self):
        sql = 'SELECT id, username, email FROM users'
        try:
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            for user in users:
                print("Id: ", user[0])
                print("Username: ", user[1])
                print("Email: ", user[2])
                print("____ \n")
        except Exception as e:
            raise

    
    def generalizar (self):
        diaV = 1
        mesV = 1
        añoV = 2017
        hV = 0
        mV = 0
        for año in range(1,6):
            for mes in range (1,11):
                for dia in range (1,28):
                    for hora in range (0,23):
                        for i in [0,15,30,45]:
                            mV = i
                            self.anadir_elemento_ram (str(diaV), str(mesV), str(añoV), str(hV), str(mV))
                        hV += 1
                        mV = 0
                    diaV += 1
                    hV = 0
                    print ("Pasé un día", diaV)
                mesV += 1
                diaV = 1
                print ("Pasé un mes", mesV)   
            añoV += 1
            mesV = 1
            print ("pasé un año", añoV)            
        pass  


    def anadir_elemento_ram (self, diaV, mesV, añoV, hV, mV):
        fechaint = añoV +"/"+ mesV+ "/" + diaV
        hora = hV +":"+ mV
        
        # printing uppercase
        letters1 = string.ascii_uppercase
        result1=  ( ''.join(random.choice(letters1) for i in range(3)) )

        # printing digits
        letters2 = string.digits
        result2 = ( ''.join(random.choice(letters2) for i in range(3)) )

        vehiculo = "FIAT" + result1 + result2


        sql= "INSERT INTO Excursiones (fecha, hora, vehiculo) VALUES ( '{}',  '{}', '{}' )".format(fechaint, hora, vehiculo)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def update_user (self, id, username):
        sql = "UPDATE users SET username = '{}' WHERE id = {} ".format (username, id)
        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise



database= DataBase()
#database.update_user (1, 'cambiadoNombre')

#database.select_user(1)
#database.generalizar()





    