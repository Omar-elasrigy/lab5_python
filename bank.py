class Customer:
    def __init__(self,customer_id,customer_name,accounts_list):
        self.customer_id=customer_id
        self.customer_name=customer_name
        self.__objaccounts=accounts_list

    def transfer(self,amount):
        self.__objaccounts[0].money=amount
        deduct_amount=-amount
        self.__objaccounts[1].money=deduct_amount
    def number_of_accounts(self):
        each_account=f"{self.customer_name} has accounts with ids: "
        for account in self.__objaccounts: 
            each_account+=f"{account.account_id} "
        return each_account
            
class Account:
    def __init__(self,account_id,balance,customer_id):
        self.account_id=account_id
        self.__balance=float(balance)
        self.customer_id=customer_id
    @property
    def money(self):
        return f"{self.__balance}"
    @money.setter
    def money(self,new_balance):
        self.__balance+=float(new_balance)

    def balance(self,amount=0):
        self.amount=float(amount)
        if amount<0: #(user will put negative input for withdraw)
            if float(self.__balance)>float(self.amount):
                self.__balance+=amount
                return (f"""Amount Withdrawn is {amount}. your Account with id {self.account_id} Current Balance 
                        now is {self.__balance}""")
            else:
                return (f"Can't Withdraw this Amount.your Account with id {self.account_id} has a Balance of {self.__balance}")
        elif amount>0: #(user will put positive input for deposit)
                self.__balance+=amount
                return (f"""Amount Deposited is {amount}. your Account with id {self.account_id} Current Balance 
                        now is {self.__balance}""")
class Bank:
    number_of_customers_in_bank=0
    def __init__(self,obj_of_customers):
        self.objofcustomers=obj_of_customers
        Bank.number_of_customers_in_bank=len(self.objofcustomers)
        
    
    @classmethod
    def count (cls):
        
        return f"number of customers is {cls.number_of_customers_in_bank}"

    
obj_account1=Account(12,1000,1)
obj_account1.money=400
obj_account2=Account(10,500,2)
l1=[obj_account1,obj_account2]
obj_customer=Customer(1,"omar",l1)

obj_account1b=Account(15,7000,3)
obj_account1b.money=1000
obj_account2b=Account(16,20000,4)
l2=[obj_account1b,obj_account2b]
obj_customer2=Customer(2,"Ahmed",l2)
list_of_customers=[obj_customer,obj_customer2]
Cib=Bank(list_of_customers)
print(obj_account1.money)
print(obj_account2.money)
# print(obj_customer.number_of_accounts())
obj_customer.transfer(100)
print(obj_account1.money)
print(obj_account2.money)
print(obj_account1.balance(-500))
print(obj_account2.balance(7000000))
print(Cib.count())
