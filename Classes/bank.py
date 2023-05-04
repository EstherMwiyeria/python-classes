# class Bank_Account:
#     account_name = "Studio_Myrtle"


class Bank_account:
    def __init__(self,account_name,account_number,account_type):
        self.account_name = account_name
        self.account_number = account_number
        self.account_type = account_type
        

    def confirm_statement(self):
        return f"The account name {self.account_name} is valid"
    def withdraw(self):
        return f"Hello you confirm your bank account_name{self.account_name} please"
    def deposit(self):
        return f"The account name {self.account_name} is missing"