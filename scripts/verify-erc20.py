from brownie import ERC20Basic

def main():
    erc20Basic = ERC20Basic[-1]    
    ERC20Basic.publish_source(erc20Basic)