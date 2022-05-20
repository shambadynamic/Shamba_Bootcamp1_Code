from brownie import MyFirstContract

def main():
    erc20Basic = MyFirstContract[-1]    
    MyFirstContract.publish_source(erc20Basic)