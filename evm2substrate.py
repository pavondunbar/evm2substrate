import subprocess
import json
from eth_keys import keys as eth_keys
from mnemonic import Mnemonic
from hashlib import sha256
import eth_utils

# Generate a mnemonic seed
def generate_mnemonic():
    mnemo = Mnemonic("english")
    mnemonic = mnemo.generate(strength=256)
    return mnemonic

# Derive seed from mnemonic
def mnemonic_to_seed(mnemonic):
    return sha256(mnemonic.encode()).digest()

# Generate secp256k1 key and Ethereum address from seed
def generate_secp256k1_key_and_address(seed):
    private_key = eth_keys.PrivateKey(seed[:32])
    public_key = private_key.public_key
    ethereum_address = public_key.to_checksum_address()
    return private_key, public_key, ethereum_address

# Generate Substrate address using subkey (no changes here)
def generate_substrate_address_with_subkey(mnemonic):
    try:
        result = subprocess.run(
            ['subkey', 'inspect', '--network', 'substrate', '--scheme', 'sr25519', mnemonic],
            capture_output=True, text=True, check=True
        )
        output = result.stdout
        
        public_key_line = next(line for line in output.splitlines() if line.startswith("  Public key (SS58):"))
        address_line = next(line for line in output.splitlines() if line.startswith("  SS58 Address:"))
        
        public_key = public_key_line.split(":")[1].strip()
        ss58_address = address_line.split(":")[1].strip()
        
        return {
            'publicKey': public_key,
            'ss58Address': ss58_address
        }
    except subprocess.CalledProcessError as e:
        print(f"Error generating Substrate address with subkey: {e}")
        return None
    except StopIteration:
        print("Error: Could not find the expected output in subkey response.")
        return None

def main():
    mnemonic = generate_mnemonic()
    seed = mnemonic_to_seed(mnemonic)

    print("Mnemonic:", mnemonic)

    secp_private_key, secp_public_key, ethereum_address = generate_secp256k1_key_and_address(seed)
    print("\nsecp256k1 Private Key:", secp_private_key.to_hex())
    print("secp256k1 Public Key:", secp_public_key.to_hex())
    print("Ethereum Address:", ethereum_address)

    substrate_keypair = generate_substrate_address_with_subkey(mnemonic)
    
    if substrate_keypair:
        print("\nsr25519 Public Key:", substrate_keypair['publicKey'])
        print("Substrate Address:", substrate_keypair['ss58Address'])

if __name__ == "__main__":
    main()
