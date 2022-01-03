from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates


class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String(50), nullable=False)
  email = Column(String(50), nullable=False, unique=True)
  password = Column(String(100), nullable=False)
  def verify_password(self, password):
   return bcrypt.checkpw(
    password.encode('utf-8'),
    self.password.encode('utf-8')
  )

  @validates('email')
  def validate_email(self, key, email):
    # make sure email address contains @ character
    assert '@' in email

    return email

  @validates('password')
  def validate_password(self, key, password):
   assert len(password) > 4

   # encrypt password
   return bcrypt.hashpw(password.encode('utf-8'), salt)

import bcrypt
salt = bcrypt.gensalt()




#   We just created a User class that inherits from the Base class. 
#   Remember that earlier, we created Base as part of the db package. 
#   In the User class, we declare several properties that the parent Base class will use to make the table. 
#   We use classes from the sqlalchemy module to define the table columns and their data types. 
#   We can also give options to each column, like nullable=False, which will become a SQL NOT NULL.

# We add a new validate_email() method to the class that a @validates('email') decorator wraps. 
# The validate_email() method returns what the value of the email column should be, and the @validates() decorator internally handles the rest. 
# This decorator is similar to the @bp.routes() decorator that we used previously to handle the route functions.

# The validate_email() method uses the assert keyword to check if an email address contains an at-sign character (@). 
# The assert keyword automatically throws an error if the condition is false, thus preventing the return statement from happening.

# Set Up Password Encryption
# We should never store passwords as is in a database, however, because that's not very secure. For that reason, we need to encrypt every password during the insert process. Let's install more libraries to help accomplish that goal.

# From the command line, run the following command:

# Copy
# pip install bcrypt cryptography
# In the User.py file, use the following code to import bcrypt:

# Copy
# import bcrypt
# We want to directly use the bcrypt module, so this time, the import syntax differs a bit. The first thing we need to do is create a salt to hash passwords against.

# Before creating the User class, add the following line:

# Copy
# salt = bcrypt.gensalt()
# Then update the validate_password() method in the User class to resemble the following code:

# Copy
# @validates('password')
# def validate_password(self, key, password):
#   assert len(password) > 4
#   # encrypt password
#   return bcrypt.hashpw(password.encode('utf-8'), salt)
# The validate_password() function now returns an encrypted version of the password, if the assert doesn't throw an error.

# Test the Validation
# Let's test it. Run the seeds.py script again, then check the table in the MySQL shell. 

