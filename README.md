# Ethereum and Substrate Address Generator

This Python script allows you to generate both Ethereum (H160) and Substrate (SS58) addresses from a given private key. The script is designed to work with secp256k1 private keys, which are commonly used in Ethereum and some Substrate-based blockchains.

## Features

- **Private Key to Public Key Conversion:** Converts a given secp256k1 private key into its corresponding public key.
- **Ethereum Address Generation:** Generates an Ethereum (H160) address from the public key.
- **Substrate Address Generation:** Generates a Substrate (SS58) address from the public key, using the specified prefix.

## Requirements

- Python 3.x
- The following Python libraries:
  - `substrate-interface`
  - `eth-keys`
  - `eth-utils`
  - `eth-hash`

You can install the required libraries using pip:

```bash
pip install substrate-interface eth-keys eth-utils eth-hash
```

## Install the program

```
git clone https://github.com/your-username/evm2substrate
cd evm2substrate
```

## Run the Script

```
python3 evm2substrate.py
```

## Input Your Private Key

When prompted, enter your private key in hexadecimal format (with or without the 0x prefix). 

Don't worry, your private key ins't exposed or keylogged in the terminal.

The script will then output the corresponding Ethereum and Substrate addresses.

## Key Points

- The generated Substrate wallet address will allow you to send and receive funds **only if the Substrate blockchain is EVM compatible OR the Substrate blockchain use the secp256k1 elliptic hash.**
- **DO NOT store, send, or receive funds to this generated wallet address if the blockchain supports cryptographic hashes ed25519 or sr25519. You will lose your funds.**
