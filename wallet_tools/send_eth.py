from wallet_tools.utils import get_web3, get_account
from web3 import Web3

def send_eth(to_address: str, amount_eth: float) -> str:
    w3 = get_web3()
    sender_address, private_key = get_account()
    amount_wei = w3.to_wei(amount_eth, "ether")

    nonce = w3.eth.get_transaction_count(sender_address)
    tx = {
        "nonce": nonce,
        "to": Web3.to_checksum_address(to_address),
        "value": amount_wei,
        "gas": 21000,
        "gasPrice": w3.to_wei("20", "gwei"),
        "chainId": 11155111,
    }

    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    return w3.to_hex(tx_hash)