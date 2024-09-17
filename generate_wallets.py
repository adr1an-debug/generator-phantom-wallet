import nacl.signing
import nacl.encoding
from mnemonic import Mnemonic
from hashlib import sha256
import base58

# Function to generate a BIP-39 mnemonic phrase
def generate_mnemonic():
    mnemo = Mnemonic("english")
    mnemonic_phrase = mnemo.generate(strength=256)
    return mnemonic_phrase

# Function to create a seed from the mnemonic phrase
def mnemonic_to_seed(mnemonic_phrase):
    mnemo = Mnemonic("english")
    seed = mnemo.to_seed(mnemonic_phrase, passphrase="")
    return seed

# Function to generate a wallet based on the seed
def generate_wallet():
    mnemonic_phrase = generate_mnemonic()
    seed = mnemonic_to_seed(mnemonic_phrase)

    seed_hash = sha256(seed).digest()[:32]
    signing_key = nacl.signing.SigningKey(seed_hash)
    verify_key = signing_key.verify_key

    private_key = signing_key.encode(encoder=nacl.encoding.HexEncoder).decode("utf-8")
    public_key = verify_key.encode(encoder=nacl.encoding.HexEncoder).decode("utf-8")

    # Generate wallet address from the public key
    wallet_address = base58.b58encode(verify_key.encode()).decode("utf-8")

    return wallet_address, public_key, private_key, mnemonic_phrase

# Generate and save wallets to the file wallets.json
with open("wallets.json", "a") as f:
    for _ in range(5):
        wallet_address, public_key, private_key, mnemonic_phrase = generate_wallet()
        # Save the data in the format: wallet_address:public_key:private_key:mnemonic_phrase
        f.write(f"{wallet_address}:{public_key}:{private_key}:{mnemonic_phrase}\n")

print("5 Wallets Generated and saved to wallets.json")
