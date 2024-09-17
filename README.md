# Phantom Wallet Generator

![image](https://github.com/user-attachments/assets/9f2084b4-93bf-468d-bd17-ec701df482ac)


A Python script for generating Phantom cryptocurrency wallets using BIP-39 mnemonics and NaCl for cryptographic operations.

## Table of Contents

- [Introducing](#introducing)
    - [Features](#features)
    - [Quick Info](#quick-info)
- [Getting Started](#getting-started)
    - [Script Installation](#script-installation)
    - [Script Usage](#script-usage)
    - [Package Installation](#package-installation)
    - [Package Usage Example](#package-usage-example)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Introducing

### Features

- **Mnemonic Phrase Generation:** Generates a BIP-39 mnemonic phrase for wallet creation.
- **Wallet Creation:** Generates a Phantom wallet using the mnemonic seed.
- **Address Generation:** Derives a Phantom wallet address from the generated keys.
- **File Output:** Saves the generated wallets to a `wallets.json` file.

### Quick Info

Ensure you have Python 3.7+ installed on your system for the script to work. This script uses the `nacl`, `mnemonic`, `hashlib`, and `base58` libraries for cryptographic operations and wallet generation.

## Getting Started

> **Note** Python 3.7+ is required

### Script Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/phantom-wallet-generator.git
    cd phantom-wallet-generator
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Script Usage

1. Open the `generate_wallets.py` file and ensure that your script is set up as desired. The script will generate Phantom wallets and save them to `wallets.json`.

2. Run the script:

    ```bash
    python generate_wallets.py
    ```

3. The script will generate five Phantom wallets and save them in `wallets.json` in the following format:

    ```
    wallet_address:public_key:private_key:mnemonic_phrase
    ```

### Package Installation

There are two ways to install the required libraries:

- **Installation using pip (a Python package manager):**

    ```bash
    pip install nacl mnemonic base58
    ```

- **Installation from source (requires git):**

    ```bash
    git clone https://github.com/yourusername/phantom-wallet-generator.git
    cd phantom-wallet-generator
    pip install .
    ```

### Package Usage Example

```python
import nacl.signing
import nacl.encoding
from mnemonic import Mnemonic
from hashlib import sha256
import base58

# Function to generate BIP-39 mnemonic phrase
def generate_mnemonic():
    mnemo = Mnemonic("english")
    mnemonic_phrase = mnemo.generate(strength=256)
    return mnemonic_phrase

# Function to create seed from mnemonic phrase
def mnemonic_to_seed(mnemonic_phrase):
    mnemo = Mnemonic("english")
    seed = mnemo.to_seed(mnemonic_phrase, passphrase="")
    return seed

# Function to generate wallet from seed
def generate_wallet():
    mnemonic_phrase = generate_mnemonic()
    seed = mnemonic_to_seed(mnemonic_phrase)

    seed_hash = sha256(seed).digest()[:32]
    signing_key = nacl.signing.SigningKey(seed_hash)
    verify_key = signing_key.verify_key

    private_key = signing_key.encode(encoder=nacl.encoding.HexEncoder).decode("utf-8")
    public_key = verify_key.encode(encoder=nacl.encoding.HexEncoder).decode("utf-8")

    # Generate wallet address from public key
    wallet_address = base58.b58encode(verify_key.encode()).decode("utf-8")

    return wallet_address, public_key, private_key, mnemonic_phrase

# Generating and saving wallets to wallets.json
with open("wallets.json", "a") as f:
    for _ in range(5):
        wallet_address, public_key, private_key, mnemonic_phrase = generate_wallet()
        # Save data in the format: wallet_address:public_key:private_key:mnemonic_phrase
        f.write(f"{wallet_address}:{public_key}:{private_key}:{mnemonic_phrase}\n")

print("done wygenerowane")
```

### Requirements
- Python 3.7+
- nacl
- mnemonic
- base58

### Contributing

Contributions to this project are welcome! Feel free to open issues or submit pull requests.

### License

This project is licensed under the MIT License.

---

**Disclaimer:** This script is intended for educational purposes and responsible use only. Ensure you comply with all relevant legal and regulatory requirements regarding cryptocurrency and wallet management. The creator and maintainers of this project are not responsible for any misuse or damages caused by its usage.
