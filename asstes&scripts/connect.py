account="https://github.com/natrixdev/snapchat-mass-friend/blob/main/config/account.json"
account_form="/main/config/account.json"

def __connect__:
  if account_from==Empty:
    return
  else if account_form==Invalid:
    return
  else if account_form==Valid:
    print('Informations are good, connecting...')
   
connect = connect()  

 def __parse__ && __array__:
    login = "https://accounts.snapchat.com/accounts/login"
   if login.autoComplete = False:
    return 
  else if login = True: 
    login()
