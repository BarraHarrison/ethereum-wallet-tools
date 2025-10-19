### Local Blockchain (Hardhat)

For development and testing purposes, I moved to using **Hardhat** to create a local Ethereum blockchain. This allows the Ethereum Wallet Tools project to run transactions, check balances, and interact with smart contracts **without connecting to an external testnet or requiring faucets**.

**Setup:**

* A local node is launched with `npx hardhat node`.
* Hardhat generates a set of ephemeral accounts pre-funded with fake ETH (~10000 ETH each).
* The private key of the desired sender account is copied into `.env` to allow the Python scripts to sign and send transactions.
* All web3 interactions in the Python project (sending ETH, checking balances, polling transaction status) are configured to connect to this local node.

**Challenges Encountered:**

1. **Ephemeral Accounts:** Every time the Hardhat node is restarted, it generates a new set of accounts with new private keys. Accounts from previous runs no longer exist, so any private key stored from a previous session will have 0 ETH.
2. **0 ETH Errors:** Transactions will fail with `insufficient funds` if the `.env` private key doesn’t match a currently funded account from the active Hardhat node.
3. **Module Execution:** Running Python scripts sometimes required executing them as modules (e.g., `python3 -m examples.send_transaction_demo`) to correctly resolve imports from the `wallet_tools` package.
4. **Environment Synchronization:** After updating `.env` or restarting the node, Python processes need to be restarted to correctly pick up the new private key and RPC URL.

Despite these quirks, Hardhat provides a **fast, safe, and fully local environment** for testing Ethereum transactions and smart contract interactions. Future improvements could include automating account funding or switching to a persistent testnet like Sepolia for more stable testing sessions.
