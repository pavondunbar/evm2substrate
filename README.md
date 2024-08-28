# Ethereum and Substrate Key Generation Script

This script provides a simple and efficient way to generate both Ethereum and Substrate addresses from a mnemonic seed. It utilizes the `eth_keys` library for generating Ethereum keys and the `subkey` tool for generating Substrate addresses. 

## Overview

The script performs the following tasks:

1. **Generate a Mnemonic Seed:** 
   - A 24-word mnemonic seed is generated using the BIP-39 standard, which serves as the foundation for creating private keys and addresses.

2. **Derive Seed from Mnemonic:**
   - The mnemonic seed is hashed using the SHA-256 algorithm to produce a 256-bit seed. This seed is used to generate cryptographic keys.

3. **Generate secp256k1 Key and Ethereum Address:**
   - A secp256k1 private key is derived from the seed, which is then used to generate the corresponding public key and Ethereum address. The address is generated using Ethereum's checksum format.

4. **Generate sr25519 Key and Substrate Address:**
   - Using the `subkey` tool, the script generates a Substrate address (formatted with SS58) from the same mnemonic seed. The sr25519 scheme is used for key generation, ensuring compatibility with Substrate-based blockchains.

## Benefits

- **Dual-Chain Compatibility:** This script allows users to generate both Ethereum and Substrate addresses from the same mnemonic seed, making it highly versatile for developers working across different blockchain platforms.
  
- **Mnemonic-based Key Derivation:** Using a mnemonic seed offers a human-readable way to back up and restore private keys, making the process more user-friendly.

- **Secure Key Generation:** The use of SHA-256 and secp256k1 cryptography ensures the security of the generated keys, adhering to industry standards for blockchain security.

- **Automated Substrate Address Generation:** The script automatically runs `subkey` commands to generate Substrate addresses, simplifying the process for users unfamiliar with Substrate tooling.

## Drawbacks

- **External Dependency on Subkey:** The script relies on the `subkey` command-line tool for generating Substrate addresses. This adds an external dependency, which users need to have installed and configured on their system.
  
- **Limited Error Handling:** While the script includes basic error handling for the `subkey` command, it might not cover all edge cases, especially when dealing with different network configurations or unexpected output formats from `subkey`.

- **No Support for Other Key Schemes:** The script is limited to secp256k1 for Ethereum and sr25519 for Substrate. It does not support other key derivation schemes such as ed25519.

## Requirements

- Python 3.x
- `eth_keys` Python package
- `mnemonic` Python package
- `subkey` command-line tool

## Installation

To use this script, follow these steps:

1. **Install Python Packages:**
   ```
   pip install eth_keys mnemonic eth_utils
   ```

2. **Run The Script:**
   ```
   python3 evm2substrate.py
   ```

3. The script will output:
   - A generated mnemonic seed.
   - The secp256k1 private key, public key, and Ethereum address.
   - The sr25519 public key and Substrate address.
   - See example below:
     ```
     Mnemonic: race draft casual crew muscle coffee clarify oak armor airport gain heart situate nominee scout mechanic wrist special media degree duty worth deliver stone

     secp256k1 Private Key: 0x4c0883a6910395b6c0dfd7d3cdccf18c37b13b2e8723f2e1fc856a91c9e5e4a2
     secp256k1 Public Key: 0x046baf0a953d58ceee2d03c9b4b1f104bae0ea9d60fdca92e02c227ff693c2d306f0010e5a57d4fa09171a181bafe9b8a5c6d800ca2c5d2de1a44b95c19b7c6c0f
     Ethereum Address: 0x00000000219ab540356cBB839Cbe05303d7705Fa

     sr25519 Public Key: 0xf1b92bbfcb4b5bcfbb7b58c7b789bb2bbdb13e29eae0a705fbc39fa29b112061
     Substrate Address: 5GrwvaEF5zXb26Fz9rcQpDWSamgAeM789bGz7vqTzyqdC5Q
     ```

     **WARNING: DO NOT USE THESE ADDRESSES OR KEYS IN THE EXAMPLE ABOVE IN PRODUCTION!! DO NOT SEND FUNDS TO THESE ADDRESSES FOR ANY REASON!!**

## Points To Consider

1. This script provides a streamlined way to generate and manage keys across Ethereum and Substrate blockchains. While it offers great versatility and security, users should be aware of         its dependencies and the need for further error handling in more complex use cases.

2. You can add the generated Ethereum wallet address to your wallet by importing an account and using the private key provided in your output.

3. You can add the generated Substrate wallet address to your Polkadot/Kusama/Substrate wallet by importing an account and specifying the **24-word mnemonic** provided in the output.

4. Please check your wallets to see if the generated accounts imported to your wallet successfully. If so, you can safely send, receive, and transfer funds to and from these wallets on their respective networks.

5. **AS ALWAYS, DO NOT GIVE OUT YOUR PRIVATE KEY OR MNEMONIC PHRASE TO ANYONE!!**
