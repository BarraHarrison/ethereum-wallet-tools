from wallet_tools.utils import get_account, get_web3

if __name__ == "__main__":
    w3 = get_web3()
    address, _ = get_account()
    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance_wei, "ether")

    print(f"Sender address (from .env): {address}")
    print(f"Balance: {balance_eth} ETH")