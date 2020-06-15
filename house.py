import web3
import json


class House:
    user_address = None
    password = None
    w3 = None
    cntr = None

    with open('abi.json') as abifile:
        abi = json.load(abifile)

    with open('contract.txt') as file:
        contract_address = file.read()

    def __init__(self):
        self.w3 = web3.Web3(web3.HTTPProvider('http://127.0.0.1:7545'))
        self.cntr = self.w3.eth.contract(
            address=self.contract_address,
            abi=self.abi
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
        self.cntr.reg_home(owner, address, square, period).transact()

    def create_sale(self, ID_home, price):
        ID_home = int(ID_home)
        price = int(price)
        self.cntr.create_sale(ID_home, price).transact()

    def buy(self, ID_sale):
        ID_sale = int(ID_sale)
        # price = int(_____)
        self.cntr.

    def stop_sale(self, ID_sale):
        pass

