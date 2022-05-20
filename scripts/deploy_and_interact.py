from brownie import MyFirstContract, config, accounts
 
def deployContract():
    account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    myFirstContract = MyFirstContract.deploy({'from': account})
    tx = myFirstContract.setNumber(123456,{'from': account})
    tx.wait(1)
    print("Number is", myFirstContract.getNumber({'from': account}))
 
def main():
    deployContract()
