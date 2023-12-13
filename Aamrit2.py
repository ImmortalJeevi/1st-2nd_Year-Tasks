import re

def validating_address(address):

    pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')


    if re.match(pattern, address):
        return True
    else:
        return False


ethereum_addresses = [
    "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
    "0x6B175474E89094C44Da98b954EedeAC495271d0F",
    "0x1234567890123456789012345678901234567890"
]

# Check validity of each Ethereum address
for address in ethereum_addresses:
    if validating_address(address):
        print(f"{address}: true")
    else:
        print(f"{address}: false")
