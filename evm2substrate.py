from substrateinterface.utils.ss58 import ss58_encode
from eth_keys import keys
from getpass import getpass  # Import the getpass module

def private_key_to_public_key(private_key_hex):
    # Strip '0x' prefix if present
    if private_key_hex.startswith('0x'):
        private_key_hex = private_key_hex[2:]
    
    # Convert the private key to a public key (secp256k1)
    private_key = keys.PrivateKey(bytes.fromhex(private_key_hex))
    public_key = private_key.public_key
    public_key_bytes = public_key.to_bytes()
    
    # Debugging: Print the length and hex value of the public key
    print(f"Public Key (hex): {public_key_bytes.hex()}")
    print(f"Public Key Length: {len(public_key_bytes)} bytes")
    
    return public_key_bytes

def public_key_to_h160(public_key_bytes):
    # Generate the Ethereum address directly using eth_keys library
    public_key = keys.PublicKey(public_key_bytes)
    eth_address = public_key.to_checksum_address()
    
    # Debugging: Print the Ethereum address
    print(f"Ethereum Address (H160): {eth_address}")
    
    return eth_address

def public_key_to_ss58(public_key_bytes, prefix=42):
    # Adjust public key length if needed (Substrate expects 32 bytes for some key types)
    if len(public_key_bytes) > 32:
        public_key_bytes = public_key_bytes[:32]
    
    # Generate the SS58 address from the (potentially shortened) public key
    ss58_addr = ss58_encode(public_key_bytes, prefix)
    
    # Debugging: Print the SS58 address
    print(f"Substrate Address (SS58): {ss58_addr}")
    
    return ss58_addr

def main():
    # Use getpass to hide the private key input
    private_key_hex = getpass("Enter your private key in hex format: ").strip()
    
    try:
        public_key_bytes = private_key_to_public_key(private_key_hex)
        
        ss58_address = public_key_to_ss58(public_key_bytes)
        h160_address = public_key_to_h160(public_key_bytes)
        
        print(f"\nFinal Addresses:\nSS58 Address: {ss58_address}\nH160 Address: {h160_address}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
