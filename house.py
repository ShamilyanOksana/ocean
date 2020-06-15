import web3
import json


class House:
    user_address = None
    password = None

    w3 = web3.Web3(web3.HTTPProvider('http://127.0.0.1:7545'))
    w3.eth.defaultAccount = w3.eth.accounts[0]

    with open('abi.json') as abifile:
        abi = json.load(abifile)

    with open('contract.txt') as file:
        contract_address = file.read()

    cntr = w3.eth.contract(
        address=contract_address,
        abi=abi
    )




    def auth(self, login):
        try:
            login = web3.Web3.toChecksumAddress(login)
        except Exception:
            return False
        else:
            self.user_address = web3.Web3.toChecksumAddress(login)
            log = self.w3.personal.unlockAccount(self.user_address, '1')
            self.w3.eth.defaultAccount = self.user_address
        return log


    def get_accounts(self):
        return self.w3.eth.accounts

    def get_admin(self):
        return self.cntr.call().admin()

    def reg_home(self, owner, address, square, period):
        owner = str(owner)
        address = str(address)
        square = int(square)
        period = int(period)
        self.cntr.functions.reg_home(owner, address, square, period).transact()

    def create_sale(self, ID_home, price):
        ID_home = int(ID_home)
        price = int(price)
        self.cntr.functions.create_sale(ID_home, price).transact()

    def buy(self, ID_sale):
        ID_sale = int(ID_sale)
        # price = int(_____)
        # self.cntr.functions.buy(ID_sale).transact({'value':value})

    def stop_sale(self, ID_sale):
        ID_sale = int(ID_sale)
        self.cntr.functions.stop_sale(ID_sale).transact()

    def get_homes_amount(self):
        return self.cntr.call().homes

H = House()
print(H.get_homes_amount())