from audioop import add
from brownie import accounts, config, SimpleStorage, network
import os


def simple_storage_deploy():
    account = get_network()
    # account = accounts.load("rashid-test-account")
    # print(account)
    # account = accounts.add(os.getenv("rashid-test-account"))
    print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)
    simple_storage_value = simple_storage.retrieve()
    print(simple_storage_value)
    transaction = simple_storage.store(42, {"from": account})
    simple_storage_value = simple_storage.retrieve()
    print(simple_storage_value)
    pass

def get_network():
    if(network.show_active() == "development"):
       return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    simple_storage_deploy()