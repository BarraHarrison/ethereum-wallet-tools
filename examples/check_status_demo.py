from wallet_tools.transaction_status import check_transaction_status

if __name__ == "__main__":
    tx_hash = input("Enter transaction hash: ").strip()
    status = check_transaction_status(tx_hash)
    print(f"Transaction status: {status}")