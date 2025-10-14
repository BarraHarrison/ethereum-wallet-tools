from web3 import Web3
from wallet_tools.utils import get_web3

def get_balance(address: str) -> float:
    w3 = get_web3()
    if not w3.is_address(address):
        raise ValueError("Invalid Ethereum address provided.")

    balance_wei = w3.eth.get_balance(address)
    balance_eth = w3.from_wei(balance_wei, "ether")
    return float(balance_eth)