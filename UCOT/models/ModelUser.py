from .entries.User import User
class ModelUser():
    @classmethod
    def login(self,db,user):
        
        try:
            sql="SELECT id, username, password, fullname FROM user WHERE username = '{}'".format(user.username)
            conn=db.connect()
            cursor=conn.cursor()
            cursor.execute(sql)
            fila=cursor.fetchone()
            if fila != None:
                user=User(fila[0], fila[1], User.check_password(fila[2], user.password),fila[3])
                return user
            else:
                return None           
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_by_id(self,db,id):
        
        try:
            sql="SELECT id, username, fullname FROM user WHERE id = '{}'".format(id)
            conn=db.connect()
            cursor=conn.cursor()
            cursor.execute(sql)
            fila=cursor.fetchone()
            if fila != None:
                return User(fila[0], fila[1], None,fila[2])
                
            else:
                return None           
        except Exception as ex:
            raise Exception(ex)