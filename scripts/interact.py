from brownie import MyFirstContract, config, accounts, network
 
def main():
    account = accounts.add(config["wallets"]["from_key"])
    myFirstContract = MyFirstContract[-1]
    tx = myFirstContract.setNumber(56879,{'from': account})
    tx.wait(1)
    print("Stored number is", myFirstContract.getNumber({'from': account}))
    print("Sum of numbers is", myFirstContract.addNumber(97234,{'from': account}))
