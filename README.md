## Authentication Project- Created Restful API for user authentication
### This project implements a basic authentication system using MySQL as the database to store user information. Users can register, log in, and receive email verification to enhance account security.
### Features:
### Login
* Registered users can log in with their email and password.
* The system checks the entered credentials against the stored information in the database.
  
### User Registration
* Users can register by providing a username, email, and password.
* User details are stored in the MySQL database, including a unique token that is generated upon registering. This token is used for verification.

### Email Verification
* After registration, users receive a verification email containing a unique token link.
* Clicking on the verification link changes the verified_token column in the database from false to true indicating user has clicked on the verification link.



