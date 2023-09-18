
class Budget:

    def __init__(self,category,initialdeposit):
        self.categoryType=category
        self.balance=initialdeposit
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        return f"Current balance is: {self.balance}"

    def withdraw(self,amount):
        if self.balance - amount > 0:
            self.balance = self.balance - amount
        else:
            return f"You do not have the available funds to withdraw {amount}. Your balance is {self.balance}"

        return f"Current balance is: {self.balance}"

    def transfer(self,targetBudget,amount):
        if self.balance - amount > 0:
            targetBudget.deposit(amount)
            self.balance = self.balance - amount
        else:
            return f"You do not have the available funds to transfer {amount} to {targetBudget.categoryType} budget . Your balance is {self.balance}"
        return f"You have succesfully transferred {amount} to your {targetBudget.categoryType} budget \n {targetBudget.categoryType} balance: {targetBudget.balance} \n {self.categoryType} balance: {self.balance}"

# create budget instances
food = Budget("Food",20)
clothing = Budget("Clothes",10)

# deposit and withdraw 
print(food.deposit(20))
print(food.withdraw(50))

# transfer
print(food.transfer(clothing,50))