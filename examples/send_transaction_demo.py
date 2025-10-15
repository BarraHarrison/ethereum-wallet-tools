from wallet_tools.send_eth import send_eth
from wallet_tools.utils import get_account

if __name__ == "__main__":
    sender, _ = get_account()
    recipient = input("Enter recipient address: ").strip()
    amount = float(input("Enter the amount of ETH to send: "))

    print("Sending transaction...")
    tx_hash = send_eth(sender, recipient, amount)
    print(f"Transaction sent! Hash: {tx_hash}")
    print("You can view it on https://sepolia.etherscan.io/tx/" + tx_hash)