import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyCoQaqKal61BHadr-g2Vs2Nppi4fEueOMk",
  "authDomain": "##########",
  "projectId": "##########",
  "databaseURL": "https://" + "##########" + ".firebaseio.com",
  "storageBucket": "##########.app",
  "messagingSenderId": "##########",
  "appId": "##########",
  "measurementId": "##########"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

user = input("Digite seu e-mail: ")
password = input("Digite sua senha, com pelo menos 6 caracteres: ")
status = auth.sign_in_with_email_and_password(user,password)
idToken = status["idToken"]

print("Resultado: ", status)
print("Token: ", idToken)

info = auth.get_account_info(idToken)
print("Info: ",info)


