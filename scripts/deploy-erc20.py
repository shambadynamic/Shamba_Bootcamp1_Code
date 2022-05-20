from brownie import ERC20Basic, config, accounts

def deployContract():
    account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    ERC20Basic.deploy(250000,{'from': account})

def main():
    deployContract()