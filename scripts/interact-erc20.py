from brownie import ERC20Basic, config, accounts, network

def mintTransfer():
    account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    erc20Basic = ERC20Basic[-1]

    #Checking total supply
    print("Total supply is", erc20Basic.totalSupply({'from': account}))

    # Checking balance in a wallet
    print("Account balance is", erc20Basic.balanceOf("0xE447E5358e612De3E54f49942733484A503609f5",{'from': account}))

    # transfering tokens to that wallet 
    erc20Basic.transfer("0xE447E5358e612De3E54f49942733484A503609f5", 50000, {'from': account}) 
    
    # Checking balance in that wallet 
    print("Account balance after receiving tokens is", erc20Basic.balanceOf("0xE447E5358e612De3E54f49942733484A503609f5",{'from': account}))

    
def main():
    mintTransfer()
