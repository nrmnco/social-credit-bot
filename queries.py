import mysql.connector



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
            
    def adding_point(self, chat_id):
        with self.connection.cursor() as cursor:

            cursor.execute('update users set social_credit = social_credit + 5 where user_id = %s',(chat_id,))

            if cursor.rowcount > 0:
                self.connection.commit()
                return None
            
            else:
                cursor.execute('insert into users (user_id, social_credit) values(%s, 301)', (chat_id,))
                self.connection.commit()


    
    def show_point(self, chat_id):
        with self.connection.cursor() as cursor:
            cursor.execute('select social_credit from users where user_id = %s', (chat_id,))
            res = cursor.fetchall()
            
            if res == []:
                cursor.execute('insert into users (user_id, social_credit) values(%s, 300)', (chat_id,))
                self.connection.commit()
                return [['300'],]
            else:
                return res