import requests
import sys 
import os
import time

def start():
    os.system('cls||clear')
    while True:
        try:
            ton_address = input("TON address: ")
            break
        except:
            answer = input("\nPlease check your data! Or you want exit? (yes or no): ")
            if answer in ["yes", "YES", "Yes"]:
                sys.exit()
            elif answer in ["no", "NO", "No"]:
                os.system('cls||clear')
                continue
        os.system('cls||clear')

    TonEx = TonExplorer(address=ton_address)
    while True:
        try:
            chosen = int(input("You can get:\n1) Balance\n2) Transaction\n3) Transactions\n4) Address information\n5) Address state\n6) Unpack address\n7) Pack address\n8) Block information\n9) Node time\n10) Coin price\n11) All information of your address\n12) Change address\n13) Clear screen\n14) Exit\nYou chose: "))
            if chosen > 14 or chosen == 13:
                os.system('cls||clear')
                continue
            if chosen == 14:
                break

            if chosen == 1:
                os.system('cls||clear')
                print(TonEx.get_balance())
            if chosen == 2:
                os.system('cls||clear')
                print("Input your data (Default without - press Enter): ")
                logical_time = input("Logic time: ")
                hash = input("Hash: ")
                os.system('cls||clear')
                print(TonEx.get_transaction(logical_time, hash))   
            if chosen == 3:
                os.system('cls||clear')
                print("Input your data (Default without - press Enter): ")
                logical_time = input("Logic time: ")
                hash = input("Hash: ")
                os.system('cls||clear')
                print(TonEx.get_transactions(logical_time, hash))  
            if chosen == 4:
                os.system('cls||clear')
                data = TonEx.get_address_info()
                print("Address state: {}\nBalance: {}".format(data['state'], data['balance'])) 
            if chosen == 5:
                os.system('cls||clear')
                print(TonEx.get_address_state())  
            if chosen == 6:
                os.system('cls||clear')
                print(TonEx.get_unpack_address())  
            if chosen == 7:
                os.system('cls||clear')
                raw_address = input("Raw address: ")
                os.system('cls||clear')
                print(TonEx.get_pack_address(raw_address))  
            if chosen == 8:
                os.system('cls||clear')
                block_id = input("Block ID: ")
                os.system('cls||clear')
                print(TonEx.get_block_info(block_id))  
            if chosen == 9:
                os.system('cls||clear')
                print(TonEx.get_node_time())  
            if chosen == 10:
                os.system('cls||clear')
                print(TonEx.get_coin_price())  
            if chosen == 11:
                os.system('cls||clear')
                data = TonEx.get_all()
                print("Address: {}".format(data['address']))
                print("Balance: {}".format(data['balance']))
                print("State: {}".format(data['state']))
                if data['last_transaction']:
                    print("Last transaction:")
                    print("  Transaction type: {}".format(data['last_transaction']['trans_type']))
                    if data['last_transaction']['trans_type'] == 'out':
                        print("  To: {}".format(data['last_transaction']['to']))
                    elif data['last_transaction']['trans_type'] == 'in':
                        print("  From: {}".format(data['last_transaction']['from']))
                    print("  TON: {}".format(data['last_transaction']['ton']))
                    print("  Message: {}".format(data['last_transaction']['message']))
                    print("  Fee: {}".format(data['fee']))
                    print("  Storage fee: {}".format(data['storage_fee']))
                    print("  Other fee: {}".format(data['other_fee']))
                    print("  Logical time: {}".format(data['logic_time']))
                    print("  Timestamp: {}".format(data['timestamp']))
                    print("  Hash: {}".format(data['hash']))
                print("Coin price: {}".format(data['coin_price']))
                print("TON Node time: {}".format(data['ton_node_time']))
                print("Blockchain ID: {}".format(data['blockchain_id']))
            if chosen == 12:
                os.system('cls||clear')
                TonEx.address = input("New address: ")
                continue
            back_menu = input('\nDo you want to back menu? (yes or exit. Default is yes): ')
            if back_menu in ['YES', 'yes', 'Yes'] or not back_menu:
                os.system('cls||clear')
            elif back_menu in ['EXIT', 'exit', 'Exit']:
                break
        except:
            os.system('cls||clear')
    sys.exit()



class TonExplorer:

    def __init__(self, address=str, host='api.ton.sh', method='GET', https=True, timeout=False, 
                    balance=True, trans_type=True, trans_message=True, trans_limit=10, 
                    last_trans=True, wallet_state=True, coin_price=True, ton_node_time=True, blockchain_id='mainnet',
                    method_address_info='getAddressInformation', method_transaction='getTransactions', 
                    method_balance='getAddressBalance', method_state='getAddressState', 
                    method_unpack='unpackAddress', method_pack='packAddress', method_block='getBlockInformation', 
                    method_node_time='getServerTime', method_price='getCoinPrice', post_header={'content-type' : 'application/x-www-form-urlencoded'}):
        """This is option for TonExplorer class

        Args:
            address (str, required): Wallet address of TON
            range_addresses (int, required): Range of wallets
            balance (bool, optional): 
            time_out (int, optional): TON node timeout for requests (30 req/min or 2 sec)
            trans_type (bool, optional): IN or OUT transation
            trans_message (bool, optional): Message from transaction
            last_action (bool, optional): 
            wallet_type (bool, optional): unitialized, active or frozen
            coin_price (bool, optional): Price TON at now
            ton_node_time (bool, optional): TON node time
            blockchain_id (str, required): Blockchain ID - mainnet or test
        """
        self.address = address
        self.host = host
        self.method = method
        self.https = https
        self.timeout = timeout
        self.balance = balance
        self.trans_type = trans_type
        self.trans_message = trans_message
        self.trans_limit = trans_limit
        self.last_trans = last_trans
        self.wallet_state = wallet_state
        self.coin_price = coin_price
        self.ton_node_time = ton_node_time
        self.blockchain_id = blockchain_id
        self.method_address_info = method_address_info
        self.method_transaction = method_transaction
        self.method_balance = method_balance
        self.method_state = method_state
        self.method_unpack = method_unpack
        self.method_pack = method_pack
        self.method_block = method_block
        self.method_node_time = method_node_time
        self.method_price = method_price
        self.post_header = post_header


    def make_request(self, method_send, method, data_to_send, header=False):
        """Function for send requests

        Args:
            method_send (str): GET or POST
            method (str): Func name on the TON node 
            data_to_send (dict): Data to send 
            header (bool, optional): You can made custom POST header

        Returns:
            object: Return answer from TON node
        """
        post_header = self.post_header if not header else header
        data_to_send['blockchain_id'] = self.blockchain_id
        if self.timeout != False:
            time.sleep(self.timeout)
        if method_send == 'GET':
            return requests.get(('https://' if self.https else 'http://') + self.host + '/' + method, 
                                    params=data_to_send)
        elif self.method == 'POST':   
            return requests.post(('https://' if self.https else 'http://') + self.host + '/' + method, 
                                    data=data_to_send, headers=post_header)


    def get_balance(self):
        data_to_send = {'address' : self.address}
        r = TonExplorer.make_request(self, self.method, self.method_balance, data_to_send)
        
        if r.json()['ok']:
            return TonExplorer.correct_balance(r.json()['result'])

        return False if not r else r.json()  


    def correct_balance(balance=int):
        if len(str(balance)) < 9:
            return '0.' + (9 - len(str(balance))) * '0' + str(balance)
        elif len(str(balance)) == 9:
            return '0.' + str(balance)
        elif len(str(balance)) > 9:
            return str(balance)[:-9] + '.' + str(balance)[-9:]

        return False


    def get_transactions(self, logical_time=False, hash=False):
        data_to_send = {'address' : self.address, 
                        'limit' : self.trans_limit}
        if logical_time and hash:
            data_to_send['lt'] = logical_time
            data_to_send['hash'] = hash

        r = TonExplorer.make_request(self, self.method, self.method_transaction, data_to_send)
        
        if r.json()['ok']:
            return r.json()['result']

        return False if not r else r.json()  


    def get_transaction(self, logical_time=False, hash=False):
        data_to_send = {'address' : self.address, 
                        'limit' : 1}
        if logical_time and hash:
            data_to_send['lt'] = logical_time
            data_to_send['hash'] = hash

        r = TonExplorer.make_request(self, self.method, self.method_transaction, data_to_send)
        
        if r.json()['ok']:
            return r.json()['result']

        return False if not r else r.json()


    def get_address_info(self): 
        data_to_send = {'address' : self.address}
        data = 0
        r = TonExplorer.make_request(self, self.method, self.method_address_info, data_to_send)

        if r.json()['ok']:
            data = r.json()
            data['result']['balance'] = TonExplorer.correct_balance(data['result']['balance'])
            return data['result']

        return False if not r else data


    def get_address_state(self):
        data_to_send = {'address' : self.address}
        r = TonExplorer.make_request(self, self.method, self.method_state, data_to_send)

        if r.json()['ok']:
            return r.json()['result']

        return False if not r else r.json() 


    def get_unpack_address(self):
        data_to_send = {'address' : self.address}
        r = TonExplorer.make_request(self, self.method, self.method_unpack, data_to_send)

        if r.json()['ok']:
            return r.json()['result']

        return False if not r else r.json() 


    def get_pack_address(self, raw_address):
        data_to_send = {'address' : raw_address}
        r = TonExplorer.make_request(self, self.method, self.method_pack, data_to_send)

        if r.json()['ok']:
            return r.json()['result']

        return False if not r else r.json()


    def get_block_info(self, block_id):
        data_to_send = {'address' : self.address, 'seqno' : block_id}
        r = TonExplorer.make_request(self, self.method, self.method_block, data_to_send)

        if r.json()['ok']:
            return r.json()['result']

        return False if not r else r.json()

    
    def get_node_time(self):
        data_to_send = {'address' : self.address}
        r = TonExplorer.make_request(self, self.method, self.method_node_time, data_to_send)

        if r.json()['ok']:
            return r.json()['result']

        return False if not r else r.json()

    
    def get_coin_price(self):
        data_to_send = {'address' : self.address}
        r = TonExplorer.make_request(self, self.method, self.method_price, data_to_send)

        if r.json()['ok']:
            return r.json()['result']

        return False if not r else r.json()


    def get_all(self):
        result = dict()

        result['address'] = self.address 
        result['balance'] = TonExplorer.get_balance(self) if self.balance else False 
        result['state'] = TonExplorer.get_address_state(self) if self.wallet_state else False

        if self.last_trans:
            data = dict()
            last_tr = TonExplorer.get_transaction(self) if self.last_trans else False
            for trans in last_tr:
                if not trans['sent']:
                    data['trans_type'] = 'in' if self.trans_type else False
                    data['from'] = trans['received']['from'] 
                    data['ton'] = TonExplorer.correct_balance(trans['received']['nanoton']) if self.balance else False
                    data['message'] = trans['received']['message'] if self.trans_message else False
                else:
                    data['trans_type'] = 'out' if self.trans_type else False
                    data['to'] = trans['sent'][0]['to']
                    data['ton'] = TonExplorer.correct_balance(trans['sent'][0]['nanoton']) if self.balance else False
                    data['message'] = trans['sent'][0]['message'] if self.trans_message else False
            result['logic_time'] = trans['lt']
            result['timestamp'] = trans['timestamp']
            result['hash'] = trans['hash']
            result['fee'] = trans['fee']
            result['storage_fee'] = trans['storage_fee']
            result['other_fee'] = trans['other_fee']
        result['last_transaction'] = data if self.last_trans else False
        result['coin_price'] = TonExplorer.get_coin_price(self) if self.coin_price else False
        result['ton_node_time'] = TonExplorer.get_node_time(self) if self.ton_node_time else False
        result['blockchain_id'] = self.blockchain_id

        return False if not result else result


if __name__ == '__main__':
    start()