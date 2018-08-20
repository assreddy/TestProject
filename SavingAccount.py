from abc import ABCMeta, abstractmethod
from random import randint

class Account:
  @abstractmethod
  def createAccount(self):
    return 0

  @abstractmethod
  def authenticate(self):
    return 0

  @abstractmethod
  def withdraw(self):
    return 0

  @abstractmethod
  def deposite(self):
    return 0

  @abstractmethod
  def displaybalance(self):
    return 0


class SavingAccount(Account):
  def __init__(self):
    self.savingAccounts = {"11111" : ["hemil",1]}

  def createAccount(self, name, initialDeposite):
    self.accountNumber = randint(10000,99999)
    self.savingAccounts[self.accountNumber] = [name, initialDeposite]
    print("Your account is successfully created:")
    print("Your account Name :  {}".format(name))
    print("Your account number : {}".format(self.accountNumber))

  def authenticate(self, name, accountNumber):
    if accountNumber in self.savingAccounts.keys():
      if self.savingAccounts[accountNumber][0] == name:
        print("Authentication Successfull.")
        self.accountNumber = accountNumber
      return True
    else:
      print("All Keys >>>" +str(self.savingAccounts.keys()))
      print("Entered Name : " +name)
      print("Name in the Database : " +self.savingAccounts.values())
      print("Authentication Failed")
      return False

  def deposite(self, depositAmount):
    self.savingAccounts[self.accountNumber][1] += depositAmount
    print("depsoit success")
    self.displaybalance(self.accountNumber)

  def withdraw(self, withDrawAmount):
    self.savingAccounts[self.accountNumber][1] -+ withDrawAmount
    print("Withdraw success")
    self.displaybalance(self.accountNumber)

  def displaybalance(self, accountNumber):
    print("Aviable balance : {}".format(self.savingAccounts[accountNumber][1]))

savingAccount = SavingAccount()

#savingAccount.createAccount('Sree',2000)

while True:
  print("Enter 1 to open an Account ")
  print("Enter 2 to access existing account")
  print("Enter 3 to Exit")
  userChoice = int(input("Enter Your Choice:"))
  if userChoice == 1:
    name = input("Enter your account Name:")
    initialDeposite = int(input("Enter initial amount :"))
    savingAccount.createAccount(name, initialDeposite)
  elif userChoice == 2:
    name = input("Enter your name")
    accountNumber = int(input("Enter account number :"))
    authenticationStatus = savingAccount.authenticate(name, accountNumber)
    if authenticationStatus is True:
      print("enter 1 to withdraw")
      print("Enter 2 to deposite")
      print("Enter 3 to displaybalance")
      print("Enter 4 to exit")
      userOption = int(input("Enter quick links: " ))
      if userOption == 1:
        withDrawlAmount =int(input("Enter amount to withdraw:"))
        savingAccount.withdraw(withDrawlAmount)
      elif userOption == 2:
        depositAmount = int(input("Enter amount to depsoit : "))
        savingAccount.deposite(depositAmount)
      elif userOption == 3:
        savingAccount.displaybalance(accountNumber)
      elif userOption == 4:
        break
  elif userChoice == 3:
    quit()


