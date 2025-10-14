from wallet_tools.utils import get_web3, get_account
from web3 import Web3

def send_eth(to_address: str, amount_eth: float) -> str:
    w3 = get_web3()
    sender_address, private_key = get_account()
    amount_wei = w3.to_wei(amount_eth, "ether")