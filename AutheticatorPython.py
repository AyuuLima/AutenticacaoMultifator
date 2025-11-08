import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyCoQaqKal61BHadr-g2Vs2Nppi4fEueOMk",
  "authDomain": "fir-pucpr-145de.firebaseapp.com",
  "projectId": "fir-pucpr-145de",
  "databaseURL": "https://" + "fir-pucpr-145de" + ".firebaseio.com",
  "storageBucket": "fir-pucpr-145de.firebasestorage.app",
  "messagingSenderId": "964464187771",
  "appId": "1:964464187771:web:bee5085c281e8b992fc5de",
  "measurementId": "G-SKCPNDLLBP"
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

