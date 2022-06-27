from multiprocessing import Value
from brownie import accounts, config, SimpleStorage
import os


def simple_storage_deploy():
    account = accounts[0]
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

def main():
    simple_storage_deploy()