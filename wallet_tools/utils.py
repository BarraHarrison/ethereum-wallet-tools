import os 
from dotenv import load_dotenv
from web3 import Web3

load_dotenv()

def get_web3():
    rpc_url = os.getenv("SEPOLIA_RPC_URL")
    if not rpc_url:
        raise ValueError("Missing SEPOLIA_RPC_URL in .env file")
    
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    if not w3.is_connected():
        raise ConnectionError("Failed to connect to the Ethereum Network.")

    return w3

def get_account():
    private_key = os.getenv("PRIVATE_KEY")
    if not private_key:
        raise ValueError("Missing PRIVATE_KEY in .env file")
    
    w3 = get_web3()
    account = w3.eth.account.from_key(private_key)
    return account.address, private_key