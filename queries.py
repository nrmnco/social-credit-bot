import mysql.connector
from datetime import datetime


class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="host",
            user="user",
            password="password",
            database="db"
            )
        self.cursor = self.connection.cursor()
        

    def subtract_point(self, chat_id):
        with self.connection.cursor() as cursor:

            cursor.execute('update users set social_credit = social_credit - 5 where user_id = %s',(chat_id,))

            if cursor.rowcount > 0:
                self.connection.commit()
                return None
            
            else:
                cursor.execute('insert into users (user_id, social_credit) values(%s, 299)', (chat_id,))
                self.connection.commit()
            

    def add_point(self, chat_id):
        with self.connection.cursor() as cursor:

            cursor.execute('update users set social_credit = social_credit + 5 where user_id = %s',(chat_id,))

            if cursor.rowcount > 0:
                self.connection.commit()
                return None
            
            else:
                cursor.execute('insert into users (user_id, social_credit) values(%s, 301)', (chat_id,))
                self.connection.commit()

    
    def get_point(self, chat_id):
        with self.connection.cursor() as cursor:
            cursor.execute('select social_credit from users where user_id = %s', (chat_id,))
            res = cursor.fetchall()
            
            if res == []:
                cursor.execute('insert into users (user_id, social_credit) values(%s, 300)', (chat_id,))
                self.connection.commit()
                return [['300'],]
            else:
                return res


    def add_last_sticker_time(self, chat_id):
        with self.connection.cursor() as cursor:
            now = datetime.now()
            cursor.execute('select last_sticker_time from time_restriction where  user_id = %s', (chat_id,))
            time = cursor.fetchone()
            if time == None:
                cursor.execute('insert into time_restriction (user_id, last_sticker_time) values(%s, %s)', (chat_id, now,))
                self.connection.commit()
            else:
                cursor.execute('update time_restriction set last_sticker_time = %s where user_id = %s', (now, chat_id))
                self.connection.commit()    


    def get_last_sticker_time(self, chat_id):
        with self.connection.cursor() as cursor:
            cursor.execute('select last_sticker_time from time_restriction where  user_id = %s', (chat_id,))
            time = cursor.fetchone()
            if time == None:
                return datetime(1000, 1, 1, 0, 0, 0)
            else:
                return time[0]
        


