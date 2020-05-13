from flask_login import UserMixin

import psycopg2

from db import get_db

class User(UserMixin):
    def __init__(self, id_, classid, name, email, profile_pic, admin):
        self.id = id_
        self.classid = classid
        self.name = name
        self.email = email
        self.profile_pic = profile_pic
        self.admin = admin

    @staticmethod
    def get(user_id):
        '''
        db = get_db()
        
        db.execute(
            "SELECT * FROM user WHERE id = ?", (user_id,)
        )
        user = db.fetchone()
        print(user)
        '''
        connection = psycopg2.connect(user = "ehguposgnxoqgt",
                                    password = "4ae2a7ab4f8c57aef3a1141e4969c89586bf2c34bf4e26eb1b57032299f9da04",
                                    host = "ec2-3-222-30-53.compute-1.amazonaws.com",
                                    port = "5432",
                                    database = "dd6ron4p756nq6")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE id = '{}'".format(user_id))
        '''
        if cursor.fetchone() is not None:
            return None
        user = cursor.fetchone()
        print("A", user)
        if user is not None:
            print("A")
        '''
        user = cursor.fetchone()
        connection.commit()
        connection.close()
        
        if not user:
            return None
        


        user = User(
            id_=user[0], classid=user[1], name=user[2], email=user[3], profile_pic=user[4], admin=user[5]
        )
        return user

    @staticmethod
    def create(id_, classid, name, email, profile_pic, admin):
        '''
        db = get_db()
        db.execute(
            "INSERT INTO users (id, classid, name, email, profile_pic, admin) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (id_, classid, name, email, profile_pic, admin),
        )
        db.commit()
        '''
         
        connection = psycopg2.connect(user = "ehguposgnxoqgt",
                                    password = "4ae2a7ab4f8c57aef3a1141e4969c89586bf2c34bf4e26eb1b57032299f9da04",
                                    host = "ec2-3-222-30-53.compute-1.amazonaws.com",
                                    port = "5432",
                                    database = "dd6ron4p756nq6")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (id, classid, name, email, profile_pic, admin) VALUES ({}, '{}', '{}', '{}', '{}', {});".format(id_, classid, name, email, profile_pic, admin))
        connection.commit()
        cursor.close()
        connection.close()