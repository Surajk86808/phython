class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
        
    def menu(self):
        print("Welcome to the chatbook")
        print("Please select an option:")
        user_input = input('1. Login\n 2. Register\n 3. Exit')
        if user_input == '1':
            self.login()
        elif user_input == '2':
            self.register()
        else:
            exit()  
            
    
    def register(self):
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        self.username = email
        self.password = password
        print(f'You are logged in as {username}')
        print("\n")
        self.menu()
    
     
    def login(self):
         if self.username == '' and self.password == '':
             print('Please register first')
             self.register()
         else:
              username = input('Enter your username(email): ')
              password = input('Enter your password: ')
              if username != self.username or password != self.password:
                  print('Invalid credentials')
                  print('\n')
                  print('Do you want to try again?')
                  print('1. Yes')
                  print('2. No')
                  user_input = input('Select an option: ')
                  if user_input == '1':
                      print('Try again')
                      print('\n')
                      self.login()
                  else:
                      print('Thank you for using our service')
                      exit() 
              else:
                   print(f'You are logged in as {username}')
                   self.loggedin = True
                   self.menu()
        
obj = chatbook()                     