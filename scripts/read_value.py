from brownie import SimpleStorage, accounts, network

def read_contract():
    print(SimpleStorage[0])

def main():
    read_contract()