import bcrypt
from database import cursor

def login_user(email, password):

    cursor.execute(
        "SELECT password FROM users WHERE email=?",
        (email,)
    )

    data = cursor.fetchone()

    if data:

        stored_password = data[0]

        if bcrypt.checkpw(password.encode(), stored_password):

            return True

    return False