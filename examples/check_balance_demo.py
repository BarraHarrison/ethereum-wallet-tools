from wallet_tools.balance_checker import get_balance
from wallet_tools.utils import get_account

if __name__ == "__main__":
    address, _ = get_account()
    balance = get_balance(address)
    print(f"Address: {address}")
    print(f"Balance: {balance} ETH")