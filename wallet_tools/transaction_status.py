from wallet_tools.utils import get_web3

def check_transaction_status(tx_hash: str) -> str:
    w3 = get_web3()

    try:
        receipt = w3.eth.get_transaction_receipt(tx_hash)

        if receipt is None:
            return "Pending"
        
        if receipt.status == 1:
            return "Success!"
        else:
            return "Transaction Failed"
    except Exception as e:
        pass

