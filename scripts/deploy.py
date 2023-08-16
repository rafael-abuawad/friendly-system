from ape import project, accounts, networks 

AVALANCHE_MAINNET = 43112
AVALANCHE_FUJI = 43113
NETWORKS = [AVALANCHE_MAINNET, AVALANCHE_FUJI]

def main():
    deployer = accounts.test_accounts[0]
    if networks.active_provider.chain_id in NETWORKS:
        deployer = accounts.load("deployer")

    data = {
        "name": "Encora NFT",
        "symbol": "ENFT",
        "base_uri": "",
        "name_eip712": "encora_nft",
        "version_eip712": "0.0.1"
    }

    project.ERC721.deploy(
        data["name"],
        data["symbol"],
        data["base_uri"],
        data["name_eip712"],
        data["version_eip712"],
        sender=deployer
    )

