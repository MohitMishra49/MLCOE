import time
class Atm:

    #constructor(special function)->superpower ->dont need to call the constructor function it gets implemented with the help of object only
    def __init__(self):
      self.pin = ''
      self.balance = 0
      self.menu()

    def menu(self):
       user_input = input(""" 
            Hi how can I heLp you?
            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check balance
            4. Press 4 to withdraw
            5. press 5 to deposit             
            6. Anything other to exit
            -------------------------
            """)
                      
       if user_input == '1':
          # create pin
          self.create_pin()
       elif user_input == '2':
          # change pin
          self.change_pin()
       elif user_input == '3':
          # check balance
          self.check_balance()
       elif user_input == '4':
          # withdraw
          self.withdraw_balance()
       elif user_input == '5':
          # deposit
          self.deposit_amount()
          
       else:
          exit()  

    def verify_pin(self):
       for i in range(3):
          entered_pin = int(input("enter the pin: "))
          if entered_pin == self.pin:
            return 1
            exit()

          else:
            print(f"Wrong pin. Attempts left:{2-i}")
         
    def create_pin(self):
       user_pin = int(input("enter your pin" ))     
       self.pin = user_pin

       user_balance = int(input("enter balance" ))
       self.balance = user_balance

       print("pin created successfully")
       self.menu()

    def change_pin(self):
       old_pin = int(input("enter old pin" ))

       if old_pin == self.pin:
          new_pin = int(input("enter new pin" ))
          new_pin = self.pin
          print("Pin changed successfully")
          # let him change the pin
          self.menu()
       else:
          print("try again") 
          self.menu() 

    def check_balance(self):
       #user_pin = int(input("enter your pin"))
       if self.verify_pin():
          print("Your balance is ",self.balance)
          self.menu()
       else:
          print("wrong pin try again later")
          self.menu()

    def withdraw_balance(self):
       #user_pin = int(input("enter your pin"))
       if self.verify_pin():
          amount = int(input("enter the amount")) 
          if amount <= self.balance:
            self.balance = self.balance - amount
            print("withdrawl successful your remaining balance is", self.balance)
            self.menu()
          else:
             print("Insufficient balance")
             self.menu() 
       else:
          print("Attempts Over!!!") 
          self.menu() 

    def deposit_amount(self):
       #user_pin = int(input("enter your pin"))
       if self.verify_pin():
          depositamount = int(input("enter the amount to deposit"))
          self.balance = self.balance + depositamount
          print("amount deposited successfully your total balance is",self.balance )
          time.sleep(2)
          self.menu()

       else:
          print("wrong pin cannot deposit amnount")
             
obj = Atm()
       
                           
                      




      