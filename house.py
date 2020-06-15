import web3
import json


class House:
    w3 = web3.Web3(web3.HTTPProvider('http://127.0.0.1:7545'))

    user_address = None

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
        owner = web3.Web3.toChecksumAddress(owner)
        address = str(address)
        square = int(square)
        period = int(period)
        self.cntr.functions.reg_home(owner, address, square, period).transact()

    def create_sale(self, ID_home, price):
        ID_home = int(ID_home)
        price = int(price)*(10**18)
        print('set price: %d' %price)
        self.cntr.functions.create_sale(ID_home, price).transact()

    def buy(self, ID_sale, price):
        ID_sale = int(ID_sale)
        price = web3.Web3.toWei(int(price), 'ether')
        self.cntr.functions.buy(ID_sale).transact({'value': price})

    def stop_sale(self, ID_sale):
        ID_sale = int(ID_sale)
        self.cntr.functions.stop_sale(ID_sale).transact()

    def get_home(self, ID_home):
        ID_home = int(ID_home)
        return self.cntr.functions.get_home(ID_home).call()

    def get_sale(self, ID_sale):
        ID_sale = int(ID_sale)
        return self.cntr.functions.get_sale(ID_sale).call()

    def get_homes_amount(self):
        return self.cntr.functions.get_homes_amount().call()

    def get_sales_amount(self):
        return self.cntr.functions.get_sales_amount().call()


# h = House()
# h.auth('0x356D7630B61EC74A4562E9CA5d464B406d754a52')
# h.reg_home('0x627117c3bB529B18c50e4aFF24350C4B6deA594E', 'Петровская, 50', 70, 5)
# h.reg_home('0xA969d347ae987E66d71e55500f10b1b52A07cdc9', 'Александровская, 127', 60, 8)
# h.reg_home('0xA969d347ae987E66d71e55500f10b1b52A07cdc9', 'Чехова, 203', 230, 3)
