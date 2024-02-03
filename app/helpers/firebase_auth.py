from firebase_admin import auth
from helpers.save_acces_token import encrypt_data, decrypt_data

from config.firebase_config import db 

def check_email(email):
    try:
        user = auth.get_user_by_email(email)
        if user:
            return True
        else:
            return False
    except:
        return False

def check_username(userName):
    try:
        users = db.collection(u'users').where(u'userName', u'==', userName).stream()
        for user in users:
            if user.to_dict()['userName'] == userName:
                return True
            else:
                return False
    except:
        return False

def create_user(token, userName, firstName, lastName, email):

    try:
        decoded_token = auth.verify_id_token(token)
        uid = decoded_token['uid']
        user = auth.get_user(uid)
        if user:
            if not check_username(userName):
                user_info = {
                    'userName': userName,
                    'firstName': firstName,
                    'lastName': lastName,
                    'email': email,
                    'uid': uid
                }
                db.collection(u'users').document(uid).set(user_info)
                return {
                    'user': user_info,
                    'token': encrypt_data(token)
                }
            else:
                return "Username already exists"
        else:
            return "User not found"
    except Exception as e:
        return "Error creating user: " + str(e)
    
    


def sign_in_with_email_and_password(plain_token):
    try:

        token = encrypt_data(plain_token)

        if token:
            
            decoded_token = auth.verify_id_token(plain_token)
            uid = decoded_token['uid']
            db_user = db.collection(u'users').document(uid).get()
            return {
                'user': db_user.to_dict(),
                'crypt_token': token
            }
    except Exception as e:
        return "Error signing in: " + str(e)

def verify_id_token(token):
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        return "Error verifying token: " + str(e)
    
def get_user_by_userName(userName):
    try:
        userName = userName.lower()
        users = db.collection(u'users').stream()
        for user in users:
            if user.to_dict()['userName'].lower() == userName:
                #Return the user object and the id of the document
                return {
                    'user': user.to_dict(),
                    'id': user.id
                }
    except Exception as e:
        return "Error getting user: " + str(e)    

